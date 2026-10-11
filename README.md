<p align="center">
  <img src="assets/icon.png" width="112" height="112" alt="GR4-MonoUnlock icon: an aperture whose six blades are the six monochrome looks">
</p>

<h1 align="center">GR4-MonoUnlock</h1>

<p align="center">
  <strong>The six monochrome looks of the GR IV Monochrome, on your RICOH GR IV.</strong>
</p>

<p align="center">
  <strong>English</strong> |
  <a href="README.ja.md">日本語</a> |
  <a href="README.zh-CN.md">简体中文</a> |
  <a href="README.zh-TW.md">繁體中文</a> |
  <a href="README.ko.md">한국어</a> |
  <a href="README.de.md">Deutsch</a> |
  <a href="README.fr.md">Français</a> |
  <a href="README.es.md">Español</a>
</p>

The monochrome-only GR IV comes with its own set of black-and-white looks.
GR4-MonoUnlock brings all six of them to the standard GR IV, ready to use in
**Image Control**, in **RAW Development**, and (three of them) in **movie** mode.
Everything else on your camera stays exactly as it was, and you can go back to
the official firmware at any time.

This repository contains no RICOH firmware. You download the official firmware
from RICOH yourself, and the included tool turns it into the unlocked version,
on your own computer.

> [!WARNING]
> **Unofficial, at your own risk.** Not made or endorsed by RICOH IMAGING.
> Installing modified firmware may void your warranty. Please read
> [Before you start](#before-you-start) and [Risks](#risks) first.

| You want to | Go to |
| --- | --- |
| See which looks you get | [What you get](#what-you-get) |
| Make the unlocked firmware (macOS, Windows, Linux) | [Make the firmware](#make-the-firmware) |
| Install it | [Put it on the camera](#put-it-on-the-camera) |
| Find out what a firmware file contains | [Check a firmware file](#check-a-firmware-file) |
| Go back to RICOH's firmware | [Going back to the official firmware](#going-back-to-the-official-firmware) |

**Contents:**
[What you get](#what-you-get) |
[Before you start](#before-you-start) |
[Make the firmware](#make-the-firmware) |
[Put it on the camera](#put-it-on-the-camera) |
[Good to know](#good-to-know) |
[Risks](#risks) |
[Testing status](#testing-status) |
[Files](#files)

## What you get

After installing, the Image Control list ends like this:

| Shown as | Look | Still | Movie |
| --- | --- | :---: | :---: |
| HDR Tone | (your existing colour look) | ✓ | |
| **Standard** | Monochrome Standard | ✓ | ✓ |
| **Solid** | Monochrome Solid | ✓ | ✓ |
| **Soft** | Monochrome Soft | ✓ | |
| **High Contrast** | Monochrome High Contrast | ✓ | ✓ |
| **Grainy** | Monochrome Grainy | ✓ | |
| **HDR Tone** | Monochrome HDR *(experimental)* | ✓ | |

- The same looks are available in **RAW Development** (in-camera RAW
  processing).
- Each new look opens at its own default settings, with **every slider at 0**,
  just like the stock looks.
- All your existing looks are unchanged.

The icon shows them too: each blade of the aperture is one look, in the order
of this list, clockwise from Standard at the top.

## Before you start

- **Camera:** RICOH GR IV (the standard colour model). Other models are not
  supported.
- **Your camera must already be on firmware 1.11.** Check the version in the
  camera's setup menu.
  - Older version: first update to 1.11 the normal way, with RICOH's official file.
  - Newer version: **do not use this tool.** It only supports 1.11.
- **The official firmware file.** From RICOH IMAGING's official GR IV support
  page, download **firmware version 1.11**. Unpack it if needed until you have
  the file **`fwdc248b.bin`**.
- **A fully charged battery.** A firmware update must never lose power.
- **An SD card** you can format.
- **Python 3.8 or newer.** macOS and most Linux systems already have it; on
  Windows, install it from python.org. Nothing else is needed.
- Note down any custom settings (C1, C2, …) you would not want to set up again.

## Make the firmware

Open a terminal in this folder and run (use the path where you saved the
official file):

```sh
python3 gr4_monounlock.py patch ~/Downloads/fwdc248b.bin
```

On Windows:

```bat
py gr4_monounlock.py patch C:\Users\you\Downloads\fwdc248b.bin
```

The tool first makes sure you gave it the genuine official 1.11 file, then
creates the unlocked firmware and checks it. When everything is right, it ends
with:

```
wrote output/fwdc248b.bin  (SHA-256 4c04b48c65897f2edd028df0f5e04666ca241488c81502bae0f34e040ee454eb)
```

If something is wrong (for example a different firmware version, or a damaged
download), it prints `refused: …` and writes **nothing**.

## Put it on the camera

### 1. Copy it to the SD card

1. **Format the SD card in the camera.**
2. Copy **`output/fwdc248b.bin`** to the **top level** of the card: not into a
   folder, and keep the name exactly `fwdc248b.bin`.

### 2. Update the camera

1. Insert the fully charged battery and the SD card.
2. Start the firmware update from the camera's setup menu, as described in
   RICOH's official GR IV firmware update instructions.
3. **The camera shows an update from version 1.11 to version 1.11.** This is
   expected: the unlocked firmware keeps the version number. Confirm the update.

> [!CAUTION]
> **Do not turn the camera off, open the battery or card door, or remove the
> card** until the update has finished and the camera has restarted.

### 3. Shoot

- Open **Image Control**: the new looks follow the first "HDR Tone".
- The firmware version still shows **1.11**. That is normal.
- Delete `fwdc248b.bin` from the card (or format the card) so the update is not
  started again by accident.

### Going back to the official firmware

Repeat steps 1–2 with the **official** `fwdc248b.bin` from RICOH instead. The
camera again shows **1.11 → 1.11**; confirm it, and your camera is back to stock.

## Good to know

- **Two "Standard" and two "HDR Tone" entries.** The monochrome Standard and HDR
  looks use the same names and icons as the colour ones. The new ones are the
  entries after the first "HDR Tone".
- **Soft, Grainy and HDR are still-only**, as on the monochrome model.
- **Monochrome HDR is experimental.** Its settings screen offers fewer options
  than the other looks. It has not been tried on a camera yet; please report how
  it behaves.
- **An official RICOH update removes the unlock.** It replaces the whole
  firmware.
- **Only for the standard GR IV on 1.11.** Never install the file on another
  model, and do not use the tool with another firmware version.
- **Before sending the camera for service,** go back to the official firmware.

### Check a firmware file

Before copying any firmware file to a card:

```sh
python3 gr4_monounlock.py check path/to/fwdc248b.bin
```

It tells you whether the file is the official 1.11, the unlocked version made
by this tool, or something else.

## Risks

- Your camera cannot tell a good firmware file from a damaged one. Only copy a
  file the tool has written (or confirmed with `check`) to your card.
- If an update is interrupted, or a firmware file cannot start, the camera may
  not reach the update function again, and it would then need RICOH service.
  This did not happen in testing, but it cannot be ruled out.
- Your camera's own calibration data is not touched.

## Testing status

| What | Status |
| --- | --- |
| Update accepted; Standard, Soft, High Contrast and Solid appear and work | tested on a GR IV 1.11 |
| Going back to the official 1.11 restores the camera completely | tested on a GR IV 1.11 |
| Grainy | included in test builds that installed and started on a GR IV 1.11 |
| Monochrome HDR | not yet tried on a camera |
| The tool reproduces the tested firmware exactly | tested |

## Files

```
GR4-MonoUnlock/
├── README.md            this guide
├── gr4_monounlock.py    the tool
└── assets/              the icon (SVG, and a 512 px PNG)
```

| File | SHA-256 |
| --- | --- |
| official RICOH GR IV 1.11 `fwdc248b.bin` | `a2f664dfca034059eb0fd6e18ab08684c326b4a034d85c164dad7e1ec9b5655f` |
| unlocked `fwdc248b.bin` made by this tool | `4c04b48c65897f2edd028df0f5e04666ca241488c81502bae0f34e040ee454eb` |
