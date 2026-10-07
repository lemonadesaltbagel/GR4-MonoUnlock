#!/usr/bin/env python3
"""GR4-MonoUnlock: unlock the hidden monochrome looks on a RICOH GR IV (firmware 1.11).

Turns the official RICOH firmware file you downloaded yourself into the unlocked
version. A file is written only if every check passes.

Usage
  python3 gr4_monounlock.py patch  OFFICIAL_fwdc248b.bin  [-o OUTPUT_DIR]
  python3 gr4_monounlock.py check  ANY_fwdc248b.bin

Python 3.8 or newer, no extra packages.
"""
import argparse
import hashlib
import struct
import sys
from pathlib import Path

VERSION = '1.0.0'

OFFICIAL_SHA256 = 'a2f664dfca034059eb0fd6e18ab08684c326b4a034d85c164dad7e1ec9b5655f'
OFFICIAL_BYTES = 38648776

UNLOCKED_SHA256 = '4c04b48c65897f2edd028df0f5e04666ca241488c81502bae0f34e040ee454eb'

CHANGES = [
    (0x3e43f0, '000052e3', '180051e3', 'look visibility check: test look number > 24 instead of camera model'),
    (0x3e43f4, '1900001a', '1900008a', 'look visibility check: send looks > 24 to the monochrome-look branch'),
    (0xdd7091, '00', '01', 'make look 25 (Monochrome Standard) available'),
    (0xdd7098, '00', '01', 'make look 26 (Monochrome Soft) available'),
    (0xdd709f, '00', '01', 'make look 27 (Monochrome High Contrast) available'),
    (0xdd70a6, '00', '01', 'make look 28 (Monochrome Grainy) available'),
    (0xdd70ad, '00', '01', 'make look 29 (Monochrome Solid) available'),
    (0xdd70b4, '00', '01', 'make look 30 (Monochrome HDR, experimental) available'),
]

HEADER, MAGIC, FOOTER_MAGIC = 128, b'RICOH\0\0\0', b'\xa5\x5a\x5a\xa5'
MAX_DISTANCE = 0x2000
LITERAL_CHUNK = 0x6000


class Refused(Exception):
    pass


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def word_sum(data):
    if len(data) % 4:
        raise Refused('data is not 4-byte aligned')
    return sum(w for (w,) in struct.iter_unpack('<I', data)) & 0xffffffff


def decode(data, limit=256 * 1024 * 1024):
    if len(data) < 160 or data[:8] != MAGIC:
        raise Refused('not a RICOH firmware container')
    out = bytearray()
    frames = []
    cursor = HEADER
    while True:
        start = cursor
        if cursor + 2 > len(data):
            raise Refused('container: missing frame terminator')
        descriptor = int.from_bytes(data[cursor:cursor + 2], 'big')
        cursor += 2
        if descriptor == 0:
            return bytes(out), frames, cursor
        size = descriptor & 0x7fff
        end = cursor + size
        if not size or end > len(data):
            raise Refused(f'container: invalid frame at {start:#x}')
        output_start = len(out)
        if descriptor & 0x8000:
            out += data[cursor:end]
            cursor = end
        else:
            while cursor < end:
                if cursor + 2 > end:
                    raise Refused(f'container: truncated flags at {cursor:#x}')
                flags = int.from_bytes(data[cursor:cursor + 2], 'big')
                cursor += 2
                for bit in range(15, -1, -1):
                    if cursor == end:
                        break
                    if not flags & (1 << bit):
                        out.append(data[cursor])
                        cursor += 1
                        continue
                    if cursor + 2 > end:
                        raise Refused('container: truncated reference')
                    a, b = data[cursor], data[cursor + 1]
                    cursor += 2
                    distance = ((a >> 3) << 8) | b
                    length = a & 7
                    if length == 7:
                        while True:
                            if cursor >= end:
                                raise Refused('container: truncated length')
                            extension = data[cursor]
                            cursor += 1
                            length += extension
                            if extension != 255:
                                break
                    if distance == 0:
                        break
                    if distance > len(out):
                        raise Refused('container: reference before start of output')
                    count = length + 3
                    if distance >= count:
                        out += out[-distance:len(out) - distance + count]
                    else:
                        pattern = bytes(out[-distance:])
                        out += (pattern * ((count + distance - 1) // distance))[:count]
                if len(out) > limit:
                    raise Refused('container: decoded size limit exceeded')
        frames.append((start, end, output_start, len(out)))


def check_container(data, payload=None, consumed=None):
    if payload is None:
        payload, _, consumed = decode(data)
    if data[-20:-16] != FOOTER_MAGIC:
        raise Refused('container: footer magic missing')
    enc, dec = struct.unpack_from('<II', data, len(data) - 12)
    if enc != consumed - HEADER or dec != len(payload):
        raise Refused('container: size fields do not match the content')
    if word_sum(data) or word_sum(payload):
        raise Refused('container: checksum mismatch')
    return payload


def sections(payload):
    out, pos = [], 0
    while pos + 16 <= len(payload):
        tag = payload[pos:pos + 8].rstrip(b'\0')
        if not tag or not tag.isalnum() or not tag.isupper():
            break
        size = struct.unpack_from('<I', payload, pos + 12)[0]
        if pos + 16 + size > len(payload):
            break
        out.append((tag.decode(), pos + 16, pos + 16 + size))
        pos += 16 + size
    return out


def differences(a, b, block=1 << 16):
    if len(a) != len(b):
        raise Refused('length mismatch')
    out = []
    for pos in range(0, len(a), block):
        x, y = a[pos:pos + block], b[pos:pos + block]
        if x != y:
            out += [pos + i for i in range(len(x)) if x[i] != y[i]]
    return out


def rezero(payload):
    buf = bytearray(payload)
    last = struct.unpack_from('<I', buf, len(buf) - 4)[0]
    struct.pack_into('<I', buf, len(buf) - 4, (last - word_sum(buf)) & 0xffffffff)
    return bytes(buf)


def literal_frames(data):
    out = bytearray()
    for pos in range(0, len(data), LITERAL_CHUNK):
        chunk = data[pos:pos + LITERAL_CHUNK]
        out += struct.pack('>H', 0x8000 | len(chunk)) + chunk
    return bytes(out)


def rebuild(source, frames, consumed, patched, changed):
    body = bytearray()
    reemitted = 0
    for (c0, c1, d0, d1) in frames:
        if any(d0 <= c < d1 or c < d0 < c + MAX_DISTANCE for c in changed):
            body += literal_frames(patched[d0:d1])
            reemitted += 1
        else:
            body += source[c0:c1]
    body += b'\0\0'
    trailer = bytearray(source[consumed:])
    struct.pack_into('<II', trailer, len(trailer) - 12, len(body), len(patched))
    struct.pack_into('<I', trailer, len(trailer) - 4, 0)
    padding = bytes((-HEADER - len(body) - len(trailer)) % 4)
    out = bytearray(source[:HEADER] + body + padding + trailer)
    struct.pack_into('<I', out, len(out) - 4, (-word_sum(out)) & 0xffffffff)
    return bytes(out), reemitted


def patch(source, log=print):
    digest = sha256(source)
    if digest != OFFICIAL_SHA256 or len(source) != OFFICIAL_BYTES:
        if digest == UNLOCKED_SHA256:
            raise Refused('this file is already unlocked; use the official RICOH file')
        raise Refused('input is not the official RICOH GR IV 1.11 fwdc248b.bin '
                      f'(SHA-256 {digest}, expected {OFFICIAL_SHA256})')
    log('input: official RICOH GR IV 1.11 firmware (SHA-256 verified)')

    log('decoding container ...')
    payload, frames, consumed = decode(source)
    check_container(source, payload, consumed)
    secs = sections(payload)
    rtos = next((s for s in secs if s[0] == 'RTOS'), None)
    if rtos is None:
        raise Refused('payload: RTOS section not found')

    buf = bytearray(payload)
    items = CHANGES
    for off, old, new, what in items:
        old, new = bytes.fromhex(old), bytes.fromhex(new)
        have = bytes(buf[off:off + len(old)])
        if have != old:
            raise Refused(f'unexpected original bytes at {off:#x}: {have.hex()} (expected {old.hex()})')
        if not (rtos[1] <= off and off + len(new) <= rtos[2]):
            raise Refused(f'change at {off:#x} is outside the RTOS section')
        buf[off:off + len(new)] = new
        log(f'  {off:#09x}  {old.hex():>8s} -> {new.hex():<8s}  {what}')
    patched = rezero(bytes(buf))

    log('rebuilding container ...')
    changed = differences(payload, patched)
    out, reemitted = rebuild(source, frames, consumed, patched, changed)

    log('verifying result ...')
    again, _, used = decode(out)
    if again != patched:
        raise Refused('verification: rebuilt container does not decode to the patched firmware')
    check_container(out, again, used)
    if out[:HEADER] != source[:HEADER]:
        raise Refused('verification: header changed')
    allowed = {i for off, old, _, _ in items for i in range(off, off + len(bytes.fromhex(old)))}
    allowed |= set(range(len(payload) - 4, len(payload)))
    stray = [i for i in changed if i not in allowed]
    if stray:
        raise Refused(f'verification: unexpected changes at {[hex(i) for i in stray[:8]]}')
    if [s for s in sections(again)] != secs:
        raise Refused('verification: section layout changed')
    if sha256(out) != UNLOCKED_SHA256:
        raise Refused('verification: result differs from the research-verified image '
                      f'(got {sha256(out)}, expected {UNLOCKED_SHA256})')
    log(f'verified: {len(changed)} payload bytes changed, {reemitted} frames re-encoded, '
        f'all other sections identical, SHA-256 matches the verified build')
    return out


def write_atomic(data, out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / 'fwdc248b.bin'
    if target.exists():
        raise Refused(f'{target} already exists; choose another output directory or remove it')
    tmp = target.with_name('.fwdc248b.bin.tmp')
    tmp.write_bytes(data)
    if sha256(tmp.read_bytes()) != sha256(data):
        tmp.unlink()
        raise Refused('write verification failed')
    tmp.rename(target)
    return target


def identify(data, log=print):
    digest = sha256(data)
    names = {OFFICIAL_SHA256: 'official RICOH GR IV 1.11 (unmodified)',
             UNLOCKED_SHA256: f'GR4-MonoUnlock {VERSION} (monochrome looks unlocked)'}
    log(f'SHA-256  {digest}')
    log(f'bytes    {len(data)}')
    log(f'file     {names.get(digest, "unknown - not produced by this tool and not the official 1.11 file")}')
    try:
        check_container(data)
        log('container: valid (size fields, footer, both checksums)')
    except Refused as exc:
        log(f'container: INVALID - {exc}')
        return 2
    return 0 if digest in names else 1


def main(argv=None):
    ap = argparse.ArgumentParser(prog='gr4_monounlock.py', description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--version', action='version', version=VERSION)
    sub = ap.add_subparsers(dest='cmd', required=True)
    p = sub.add_parser('patch', help='make the unlocked firmware from the official file')
    p.add_argument('input', type=Path, help='official RICOH fwdc248b.bin (GR IV 1.11)')
    p.add_argument('-o', '--output-dir', type=Path, default=Path('output'),
                   help='directory for the result (default: ./output); the file is named fwdc248b.bin')
    c = sub.add_parser('check', help='identify a fwdc248b.bin and validate its container')
    c.add_argument('input', type=Path)
    a = ap.parse_args(argv)
    sys.stdout.reconfigure(line_buffering=True)
    if sys.version_info < (3, 8):
        print('Python 3.8 or newer is required', file=sys.stderr)
        return 2
    try:
        data = a.input.read_bytes()
        if a.cmd == 'check':
            return identify(data)
        if (a.output_dir / 'fwdc248b.bin').exists():
            raise Refused(f'{a.output_dir / "fwdc248b.bin"} already exists; '
                          'choose another output directory or remove it')
        print(f'GR4-MonoUnlock {VERSION}')
        out = patch(data)
        target = write_atomic(out, a.output_dir)
        print(f'wrote {target}  (SHA-256 {sha256(out)})')
        print('Copy this file to the root of the SD card and run the camera\'s firmware update.')
        return 0
    except Refused as exc:
        print(f'refused: {exc}', file=sys.stderr)
        print('nothing was written.', file=sys.stderr)
        return 1
    except OSError as exc:
        print(f'error: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())