<p align="center">
  <img src="assets/icon.png" width="112" height="112" alt="Icono de GR4-MonoUnlock: un diafragma cuyas seis láminas son los seis looks monocromos">
</p>

<h1 align="center">GR4-MonoUnlock</h1>

<p align="center">
  <strong>Los seis looks monocromos de la GR IV Monochrome, en tu RICOH GR IV.</strong>
</p>

<p align="center">
  <a href="README.md">English</a> |
  <a href="README.ja.md">日本語</a> |
  <a href="README.zh-CN.md">简体中文</a> |
  <a href="README.zh-TW.md">繁體中文</a> |
  <a href="README.ko.md">한국어</a> |
  <a href="README.de.md">Deutsch</a> |
  <a href="README.fr.md">Français</a> |
  <strong>Español</strong>
</p>

La GR IV exclusivamente monocroma trae su propio conjunto de looks en blanco y
negro. GR4-MonoUnlock lleva los seis a la GR IV estándar, listos para usar en
**Control de imagen**, en **RAW Development** y (tres de ellos) en modo **vídeo**.
Todo lo demás de tu cámara queda exactamente como estaba, y puedes volver al
firmware oficial en cualquier momento.

Este repositorio no contiene ningún firmware de RICOH. Tú mismo descargas el
firmware oficial de RICOH, y la herramienta incluida lo convierte en la versión
desbloqueada, en tu propio ordenador.

> [!WARNING]
> **No oficial, bajo tu propia responsabilidad.** No está hecho ni respaldado por RICOH IMAGING.
> Instalar un firmware modificado puede anular la garantía. Lee primero
> [Antes de empezar](#antes-de-empezar) y [Riesgos](#riesgos).

| Quieres | Ve a |
| --- | --- |
| Ver qué looks obtienes | [Qué obtienes](#qué-obtienes) |
| Crear el firmware desbloqueado (macOS, Windows, Linux) | [Crea el firmware](#crea-el-firmware) |
| Instalarlo | [Instálalo en la cámara](#instálalo-en-la-cámara) |
| Saber qué contiene un archivo de firmware | [Comprobar un archivo de firmware](#comprobar-un-archivo-de-firmware) |
| Volver al firmware de RICOH | [Volver al firmware oficial](#volver-al-firmware-oficial) |

**Contenido:**
[Qué obtienes](#qué-obtienes) |
[Antes de empezar](#antes-de-empezar) |
[Crea el firmware](#crea-el-firmware) |
[Instálalo en la cámara](#instálalo-en-la-cámara) |
[Conviene saber](#conviene-saber) |
[Riesgos](#riesgos) |
[Estado de las pruebas](#estado-de-las-pruebas) |
[Archivos](#archivos)

## Qué obtienes

Después de instalarlo, la lista de Control de imagen termina así. Los nombres de
los menús se dan como en una cámara configurada en inglés (Control de imagen y
Estándar, en español).

| Se muestra como | Look | Foto | Vídeo |
| --- | --- | :---: | :---: |
| HDR Tone | (tu look de color actual) | ✓ | |
| **Estándar** | Estándar monocromo | ✓ | ✓ |
| **Solid** | Solid monocromo | ✓ | ✓ |
| **Soft** | Soft monocromo | ✓ | |
| **High Contrast** | High Contrast monocromo | ✓ | ✓ |
| **Grainy** | Grainy monocromo | ✓ | |
| **HDR Tone** | HDR monocromo *(experimental)* | ✓ | |

- Los mismos looks están disponibles en **RAW Development** (el procesado RAW en
  la cámara).
- Cada look nuevo empieza con sus propios ajustes predeterminados, con **todos
  los controles a 0**, igual que los looks de serie.
- Todos tus looks actuales quedan sin cambios.

El icono también los muestra: cada lámina del diafragma es un look, en el orden
de esta lista, en el sentido de las agujas del reloj empezando por Estándar arriba.

## Antes de empezar

- **Cámara:** RICOH GR IV (el modelo en color estándar). Otros modelos no son
  compatibles.
- **Tu cámara ya debe tener el firmware 1.11.** Comprueba la versión en el menú
  de configuración de la cámara.
  - Versión anterior: actualiza primero a la 1.11 de la forma normal, con el archivo oficial de RICOH.
  - Versión más reciente: **no uses esta herramienta.** Solo es compatible con la 1.11.
- **El archivo de firmware oficial.** En la página oficial de soporte de la GR IV
  de RICOH IMAGING, descarga la **versión de firmware 1.11**. Descomprímela si hace
  falta hasta tener el archivo **`fwdc248b.bin`**.
- **Una batería totalmente cargada.** Una actualización de firmware nunca debe
  quedarse sin alimentación.
- **Una tarjeta SD** que puedas formatear.
- **Python 3.8 o posterior.** macOS y la mayoría de los sistemas Linux ya lo
  tienen; en Windows, instálalo desde python.org. No hace falta nada más.
- Apunta los ajustes personalizados (C1, C2, …) que no quieras tener que volver a configurar.

## Crea el firmware

Abre un terminal en esta carpeta y ejecuta (usa la ruta donde guardaste el
archivo oficial):

```sh
python3 gr4_monounlock.py patch ~/Downloads/fwdc248b.bin
```

En Windows:

```bat
py gr4_monounlock.py patch C:\Users\you\Downloads\fwdc248b.bin
```

La herramienta comprueba primero que le has dado el archivo oficial 1.11
auténtico; después crea el firmware desbloqueado y lo comprueba. Cuando todo es
correcto, termina así:

```
wrote output/fwdc248b.bin  (SHA-256 4c04b48c65897f2edd028df0f5e04666ca241488c81502bae0f34e040ee454eb)
```

Si algo falla (por ejemplo, otra versión de firmware o una descarga dañada), la
herramienta muestra `refused: …` y **no escribe nada**.

## Instálalo en la cámara

### 1. Cópialo a la tarjeta SD

1. **Formatea la tarjeta SD en la cámara.**
2. Copia **`output/fwdc248b.bin`** en la **raíz** de la tarjeta: no dentro de una
   carpeta, y con el nombre exactamente `fwdc248b.bin`.

### 2. Actualiza la cámara

1. Inserta la batería totalmente cargada y la tarjeta SD.
2. Inicia la actualización de firmware desde el menú de configuración de la cámara,
   como se describe en las instrucciones oficiales de RICOH para actualizar el firmware de la GR IV.
3. **La cámara muestra una actualización de la versión 1.11 a la versión 1.11.** Es
   lo esperado: el firmware desbloqueado mantiene el número de versión. Confirma la actualización.

> [!CAUTION]
> **No apagues la cámara, no abras la tapa de la batería o de la tarjeta y no
> saques la tarjeta** hasta que la actualización haya terminado y la cámara se haya reiniciado.

### 3. A disparar

- Abre **Control de imagen**: los looks nuevos van después del primer "HDR Tone".
- La versión del firmware sigue mostrando **1.11**. Es normal.
- Borra `fwdc248b.bin` de la tarjeta (o formatéala) para que la actualización no
  se inicie de nuevo por error.

### Volver al firmware oficial

Repite los pasos 1–2 con el `fwdc248b.bin` **oficial** de RICOH. La cámara vuelve
a mostrar **1.11 → 1.11**; confírmalo y tu cámara vuelve a su estado original.

## Conviene saber

- **Dos entradas "Estándar" y dos "HDR Tone".** Los looks monocromos Estándar y HDR
  usan los mismos nombres e iconos que los de color. Los nuevos son las entradas
  después del primer "HDR Tone".
- **Soft, Grainy y HDR son solo para fotos**, como en el modelo monocromo.
- **El HDR monocromo es experimental.** Su pantalla de ajustes ofrece menos
  opciones que los demás looks. Todavía no se ha probado en una cámara; cuéntanos
  cómo se comporta.
- **Una actualización oficial de RICOH elimina el desbloqueo.** Reemplaza todo el
  firmware.
- **Solo para la GR IV estándar con la 1.11.** Nunca instales el archivo en otro
  modelo, y no uses la herramienta con otra versión de firmware.
- **Antes de enviar la cámara al servicio técnico,** vuelve al firmware oficial.

### Comprobar un archivo de firmware

Antes de copiar cualquier archivo de firmware a una tarjeta:

```sh
python3 gr4_monounlock.py check path/to/fwdc248b.bin
```

Te dice si el archivo es el 1.11 oficial, la versión desbloqueada creada por
esta herramienta u otra cosa.

## Riesgos

- Tu cámara no puede distinguir un archivo de firmware bueno de uno dañado. Copia a
  tu tarjeta solo un archivo que haya escrito la herramienta (o que hayas confirmado con `check`).
- Si una actualización se interrumpe, o un archivo de firmware no puede arrancar, puede
  que la cámara ya no llegue a la función de actualización, y entonces necesitaría el
  servicio técnico de RICOH. No ocurrió en las pruebas, pero no se puede descartar.
- Los datos de calibración propios de tu cámara no se tocan.

## Estado de las pruebas

| Qué | Estado |
| --- | --- |
| Actualización aceptada; Estándar, Soft, High Contrast y Solid aparecen y funcionan | probado en una GR IV 1.11 |
| Volver al 1.11 oficial restablece la cámara por completo | probado en una GR IV 1.11 |
| Grainy | incluido en compilaciones de prueba que se instalaron y arrancaron en una GR IV 1.11 |
| HDR monocromo | aún no se ha probado en una cámara |
| La herramienta reproduce exactamente el firmware probado | probado |

## Archivos

```
GR4-MonoUnlock/
├── README.md            this guide
├── gr4_monounlock.py    the tool
└── assets/              the icon (SVG, and a 512 px PNG)
```

| Archivo | SHA-256 |
| --- | --- |
| `fwdc248b.bin` oficial de RICOH GR IV 1.11 | `a2f664dfca034059eb0fd6e18ab08684c326b4a034d85c164dad7e1ec9b5655f` |
| `fwdc248b.bin` desbloqueado creado por esta herramienta | `4c04b48c65897f2edd028df0f5e04666ca241488c81502bae0f34e040ee454eb` |
