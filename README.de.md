<p align="center">
  <img src="assets/icon.png" width="112" height="112" alt="GR4-MonoUnlock-Symbol: eine Blende, deren sechs Lamellen die sechs Monochrom-Looks sind">
</p>

<h1 align="center">GR4-MonoUnlock</h1>

<p align="center">
  <strong>Die sechs Monochrom-Looks der GR IV Monochrome, auf Ihrer RICOH GR IV.</strong>
</p>

<p align="center">
  <a href="README.md">English</a> |
  <a href="README.ja.md">日本語</a> |
  <a href="README.zh-CN.md">简体中文</a> |
  <a href="README.zh-TW.md">繁體中文</a> |
  <a href="README.ko.md">한국어</a> |
  <strong>Deutsch</strong> |
  <a href="README.fr.md">Français</a> |
  <a href="README.es.md">Español</a>
</p>

Die GR IV, die nur in Schwarzweiß aufnimmt, bringt eigene Schwarzweiß-Looks mit.
GR4-MonoUnlock bringt alle sechs auf die normale GR IV, bereit zur Verwendung in
**Bildsteuerung**, in **RAW Development** und (drei davon) im **Videomodus**.
Alles andere an Ihrer Kamera bleibt genau so, wie es war, und Sie können
jederzeit zur offiziellen Firmware zurückkehren.

Dieses Repository enthält keine RICOH-Firmware. Sie laden die offizielle
Firmware selbst von RICOH herunter, und das enthaltene Werkzeug macht daraus auf
Ihrem eigenen Computer die freigeschaltete Version.

> [!WARNING]
> **Inoffiziell, auf eigenes Risiko.** Nicht von RICOH IMAGING erstellt oder
> unterstützt. Die Installation veränderter Firmware kann Ihre Garantie
> ungültig machen. Bitte lesen Sie zuerst [Bevor Sie beginnen](#bevor-sie-beginnen)
> und [Risiken](#risiken).

| Sie möchten | Weiter zu |
| --- | --- |
| Sehen, welche Looks Sie bekommen | [Was Sie bekommen](#was-sie-bekommen) |
| Die freigeschaltete Firmware erstellen (macOS, Windows, Linux) | [Die Firmware erstellen](#die-firmware-erstellen) |
| Sie installieren | [Auf die Kamera bringen](#auf-die-kamera-bringen) |
| Herausfinden, was eine Firmware-Datei enthält | [Firmware-Datei prüfen](#firmware-datei-prüfen) |
| Zur Firmware von RICOH zurückkehren | [Zurück zur offiziellen Firmware](#zurück-zur-offiziellen-firmware) |

**Inhalt:**
[Was Sie bekommen](#was-sie-bekommen) |
[Bevor Sie beginnen](#bevor-sie-beginnen) |
[Die Firmware erstellen](#die-firmware-erstellen) |
[Auf die Kamera bringen](#auf-die-kamera-bringen) |
[Gut zu wissen](#gut-zu-wissen) |
[Risiken](#risiken) |
[Teststand](#teststand) |
[Dateien](#dateien)

## Was Sie bekommen

Nach der Installation endet die Liste der Bildsteuerung so. Menünamen außer
Bildsteuerung und Standard sind so angegeben, wie sie auf einer auf Englisch
eingestellten Kamera erscheinen.

| Angezeigt als | Look | Foto | Video |
| --- | --- | :---: | :---: |
| HDR Tone | (Ihr bisheriger Farb-Look) | ✓ | |
| **Standard** | Monochrom Standard | ✓ | ✓ |
| **Solid** | Monochrom Solid | ✓ | ✓ |
| **Soft** | Monochrom Soft | ✓ | |
| **High Contrast** | Monochrom High Contrast | ✓ | ✓ |
| **Grainy** | Monochrom Grainy | ✓ | |
| **HDR Tone** | Monochrom HDR *(experimentell)* | ✓ | |

- Dieselben Looks sind auch in **RAW Development** (RAW-Entwicklung in der
  Kamera) verfügbar.
- Jeder neue Look startet mit seinen eigenen Standardeinstellungen, mit
  **allen Reglern auf 0**, genau wie die werkseitigen Looks.
- Alle Ihre bisherigen Looks bleiben unverändert.

Auch das Symbol zeigt sie: Jede Lamelle der Blende ist ein Look, in der
Reihenfolge dieser Liste, im Uhrzeigersinn ab Standard oben.

## Bevor Sie beginnen

- **Kamera:** RICOH GR IV (das normale Farbmodell). Andere Modelle werden nicht
  unterstützt.
- **Ihre Kamera muss bereits Firmware 1.11 haben.** Prüfen Sie die Version im
  Einstellungsmenü der Kamera.
  - Ältere Version: Aktualisieren Sie zuerst auf dem üblichen Weg mit der
    offiziellen Datei von RICOH auf 1.11.
  - Neuere Version: **Verwenden Sie dieses Werkzeug nicht.** Es unterstützt nur 1.11.
- **Die offizielle Firmware-Datei.** Laden Sie auf der offiziellen
  GR-IV-Supportseite von RICOH IMAGING die **Firmware-Version 1.11** herunter.
  Entpacken Sie sie bei Bedarf, bis Sie die Datei **`fwdc248b.bin`** haben.
- **Ein voll geladener Akku.** Während eines Firmware-Updates darf der Strom
  niemals ausfallen.
- **Eine SD-Karte**, die Sie formatieren können.
- **Python 3.8 oder neuer.** macOS und die meisten Linux-Systeme haben es
  bereits; unter Windows installieren Sie es von python.org. Mehr wird nicht
  benötigt.
- Notieren Sie sich eigene Einstellungen (C1, C2, …), die Sie nicht noch einmal
  einrichten möchten.

## Die Firmware erstellen

Öffnen Sie ein Terminal in diesem Ordner und führen Sie aus (verwenden Sie den
Pfad, unter dem Sie die offizielle Datei gespeichert haben):

```sh
python3 gr4_monounlock.py patch ~/Downloads/fwdc248b.bin
```

Unter Windows:

```bat
py gr4_monounlock.py patch C:\Users\you\Downloads\fwdc248b.bin
```

Das Werkzeug stellt zuerst sicher, dass Sie ihm die echte offizielle Datei 1.11
gegeben haben, erstellt dann die freigeschaltete Firmware und prüft sie. Wenn
alles stimmt, endet es mit:

```
wrote output/fwdc248b.bin  (SHA-256 4c04b48c65897f2edd028df0f5e04666ca241488c81502bae0f34e040ee454eb)
```

Wenn etwas nicht stimmt (zum Beispiel eine andere Firmware-Version oder ein
beschädigter Download), gibt es `refused: …` aus und schreibt **nichts**.

## Auf die Kamera bringen

### 1. Auf die SD-Karte kopieren

1. **Formatieren Sie die SD-Karte in der Kamera.**
2. Kopieren Sie **`output/fwdc248b.bin`** in die **oberste Ebene** der Karte:
   nicht in einen Ordner, und der Name muss genau `fwdc248b.bin` bleiben.

### 2. Kamera aktualisieren

1. Setzen Sie den voll geladenen Akku und die SD-Karte ein.
2. Starten Sie das Firmware-Update im Einstellungsmenü der Kamera, wie in der
   offiziellen Anleitung von RICOH zum Firmware-Update der GR IV beschrieben.
3. **Die Kamera zeigt ein Update von Version 1.11 auf Version 1.11.** Das ist
   so gewollt: Die freigeschaltete Firmware behält die Versionsnummer.
   Bestätigen Sie das Update.

> [!CAUTION]
> **Schalten Sie die Kamera nicht aus, öffnen Sie weder Akku- noch
> Kartenfach, und nehmen Sie die Karte nicht heraus**, bis das Update
> abgeschlossen ist und die Kamera neu gestartet hat.

### 3. Fotografieren

- Öffnen Sie **Bildsteuerung**: Die neuen Looks folgen auf das erste
  „HDR Tone“.
- Die Firmware-Version zeigt weiterhin **1.11**. Das ist normal.
- Löschen Sie `fwdc248b.bin` von der Karte (oder formatieren Sie die Karte),
  damit das Update nicht versehentlich erneut startet.

### Zurück zur offiziellen Firmware

Wiederholen Sie die Schritte 1–2 stattdessen mit der **offiziellen** `fwdc248b.bin`
von RICOH. Die Kamera zeigt wieder **1.11 → 1.11**; bestätigen Sie, und Ihre
Kamera ist wieder im Originalzustand.

## Gut zu wissen

- **Zwei Einträge „Standard“ und zwei „HDR Tone“.** Die monochromen Looks
  Standard und HDR verwenden dieselben Namen und Symbole wie die farbigen. Die
  neuen sind die Einträge nach dem ersten „HDR Tone“.
- **Soft, Grainy und HDR gibt es nur für Fotos**, wie beim Monochrom-Modell.
- **Monochrom HDR ist experimentell.** Sein Einstellungsbildschirm bietet
  weniger Optionen als die anderen Looks. Es wurde noch nicht auf einer Kamera
  ausprobiert; bitte berichten Sie, wie es sich verhält.
- **Ein offizielles Update von RICOH entfernt die Freischaltung.** Es ersetzt
  die gesamte Firmware.
- **Nur für die normale GR IV mit 1.11.** Installieren Sie die Datei nie auf
  einem anderen Modell, und verwenden Sie das Werkzeug nicht mit einer anderen
  Firmware-Version.
- **Bevor Sie die Kamera zum Service schicken,** kehren Sie zur offiziellen
  Firmware zurück.

### Firmware-Datei prüfen

Bevor Sie eine Firmware-Datei auf eine Karte kopieren:

```sh
python3 gr4_monounlock.py check path/to/fwdc248b.bin
```

Es sagt Ihnen, ob die Datei die offizielle 1.11, die mit diesem Werkzeug
erstellte freigeschaltete Version oder etwas anderes ist.

## Risiken

- Ihre Kamera kann eine gute Firmware-Datei nicht von einer beschädigten
  unterscheiden. Kopieren Sie nur eine Datei auf Ihre Karte, die das Werkzeug
  geschrieben (oder mit `check` bestätigt) hat.
- Wenn ein Update unterbrochen wird oder eine Firmware-Datei nicht starten kann,
  erreicht die Kamera die Update-Funktion eventuell nicht mehr und müsste dann
  zum RICOH-Service. Das ist in den Tests nicht passiert, lässt sich aber nicht
  ausschließen.
- Die eigenen Kalibrierungsdaten Ihrer Kamera werden nicht angetastet.

## Teststand

| Was | Stand |
| --- | --- |
| Update akzeptiert; Standard, Soft, High Contrast und Solid erscheinen und funktionieren | getestet auf einer GR IV 1.11 |
| Die Rückkehr zur offiziellen 1.11 stellt die Kamera vollständig wieder her | getestet auf einer GR IV 1.11 |
| Grainy | enthalten in Test-Builds, die sich auf einer GR IV 1.11 installieren ließen und starteten |
| Monochrom HDR | noch nicht auf einer Kamera ausprobiert |
| Das Werkzeug reproduziert die getestete Firmware exakt | getestet |

## Dateien

```
GR4-MonoUnlock/
├── README.md            this guide
├── gr4_monounlock.py    the tool
└── assets/              the icon (SVG, and a 512 px PNG)
```

| Datei | SHA-256 |
| --- | --- |
| offizielle `fwdc248b.bin` 1.11 der RICOH GR IV | `a2f664dfca034059eb0fd6e18ab08684c326b4a034d85c164dad7e1ec9b5655f` |
| freigeschaltete `fwdc248b.bin`, mit diesem Werkzeug erstellt | `4c04b48c65897f2edd028df0f5e04666ca241488c81502bae0f34e040ee454eb` |
