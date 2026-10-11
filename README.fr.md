<p align="center">
  <img src="assets/icon.png" width="112" height="112" alt="Icône de GR4-MonoUnlock : un diaphragme dont les six lamelles sont les six looks monochromes">
</p>

<h1 align="center">GR4-MonoUnlock</h1>

<p align="center">
  <strong>Les six looks monochromes du GR IV Monochrome, sur votre RICOH GR IV.</strong>
</p>

<p align="center">
  <a href="README.md">English</a> |
  <a href="README.ja.md">日本語</a> |
  <a href="README.zh-CN.md">简体中文</a> |
  <a href="README.zh-TW.md">繁體中文</a> |
  <a href="README.ko.md">한국어</a> |
  <a href="README.de.md">Deutsch</a> |
  <strong>Français</strong> |
  <a href="README.es.md">Español</a>
</p>

Le GR IV exclusivement monochrome est livré avec ses propres looks noir et
blanc. GR4-MonoUnlock apporte les six au GR IV standard, prêts à l'emploi dans
**Contrôle de l'image**, dans **RAW Development** et (trois d'entre eux) en mode
**vidéo**. Tout le reste de votre appareil reste exactement comme avant, et vous
pouvez revenir au firmware officiel à tout moment.

Ce dépôt ne contient aucun firmware RICOH. Vous téléchargez vous-même le
firmware officiel chez RICOH, et l'outil fourni le transforme en version
débloquée, sur votre propre ordinateur.

> [!WARNING]
> **Non officiel, à vos risques et périls.** Ni conçu ni approuvé par RICOH IMAGING.
> L'installation d'un firmware modifié peut annuler votre garantie. Lisez d'abord
> [Avant de commencer](#avant-de-commencer) et [Risques](#risques).

| Vous voulez | Allez à |
| --- | --- |
| Voir quels looks vous obtenez | [Ce que vous obtenez](#ce-que-vous-obtenez) |
| Créer le firmware débloqué (macOS, Windows, Linux) | [Créer le firmware](#créer-le-firmware) |
| L'installer | [Installer sur l'appareil](#installer-sur-lappareil) |
| Savoir ce que contient un fichier de firmware | [Vérifier un fichier de firmware](#vérifier-un-fichier-de-firmware) |
| Revenir au firmware de RICOH | [Revenir au firmware officiel](#revenir-au-firmware-officiel) |

**Sommaire :**
[Ce que vous obtenez](#ce-que-vous-obtenez) |
[Avant de commencer](#avant-de-commencer) |
[Créer le firmware](#créer-le-firmware) |
[Installer sur l'appareil](#installer-sur-lappareil) |
[Bon à savoir](#bon-à-savoir) |
[Risques](#risques) |
[État des tests](#état-des-tests) |
[Fichiers](#fichiers)

## Ce que vous obtenez

Après l'installation, la liste Contrôle de l'image se termine comme ci-dessous.
En dehors de Contrôle de l'image et Standard, les noms de menu sont donnés tels
qu'ils s'affichent sur un appareil réglé en anglais.

| Affiché comme | Look | Photo | Vidéo |
| --- | --- | :---: | :---: |
| HDR Tone | (votre look couleur existant) | ✓ | |
| **Standard** | Monochrome Standard | ✓ | ✓ |
| **Solid** | Monochrome Solid | ✓ | ✓ |
| **Soft** | Monochrome Soft | ✓ | |
| **High Contrast** | Monochrome High Contrast | ✓ | ✓ |
| **Grainy** | Monochrome Grainy | ✓ | |
| **HDR Tone** | Monochrome HDR *(expérimental)* | ✓ | |

- Les mêmes looks sont disponibles dans **RAW Development** (le développement
  RAW dans l'appareil).
- Chaque nouveau look s'ouvre avec ses propres réglages par défaut, **tous les
  curseurs à 0**, comme les looks d'origine.
- Tous vos looks existants restent inchangés.

L'icône les montre aussi : chaque lamelle du diaphragme est un look, dans l'ordre
de cette liste, dans le sens des aiguilles d'une montre à partir de Standard en
haut.

## Avant de commencer

- **Appareil :** RICOH GR IV (le modèle couleur standard). Les autres modèles ne
  sont pas pris en charge.
- **Votre appareil doit déjà être en firmware 1.11.** Vérifiez la version dans
  le menu de configuration de l'appareil.
  - Version plus ancienne : mettez d'abord à jour vers la 1.11 de la manière habituelle, avec le fichier officiel de RICOH.
  - Version plus récente : **n'utilisez pas cet outil.** Il ne prend en charge que la 1.11.
- **Le fichier de firmware officiel.** Sur la page d'assistance officielle du
  GR IV de RICOH IMAGING, téléchargez la **version de firmware 1.11**.
  Décompressez-la si nécessaire jusqu'à obtenir le fichier **`fwdc248b.bin`**.
- **Une batterie complètement chargée.** Une mise à jour du firmware ne doit
  jamais être privée d'alimentation.
- **Une carte SD** que vous pouvez formater.
- **Python 3.8 ou plus récent.** macOS et la plupart des systèmes Linux l'ont
  déjà ; sous Windows, installez-le depuis python.org. Rien d'autre n'est
  nécessaire.
- Notez les réglages personnalisés (C1, C2, …) que vous ne voudriez pas refaire.

## Créer le firmware

Ouvrez un terminal dans ce dossier et lancez (avec le chemin où vous avez
enregistré le fichier officiel) :

```sh
python3 gr4_monounlock.py patch ~/Downloads/fwdc248b.bin
```

Sous Windows :

```bat
py gr4_monounlock.py patch C:\Users\you\Downloads\fwdc248b.bin
```

L'outil vérifie d'abord que vous lui avez donné le véritable fichier officiel
1.11, puis crée le firmware débloqué et le vérifie. Si tout est correct, il se
termine ainsi :

```
wrote output/fwdc248b.bin  (SHA-256 4c04b48c65897f2edd028df0f5e04666ca241488c81502bae0f34e040ee454eb)
```

En cas de problème (par exemple une autre version de firmware ou un
téléchargement endommagé), il affiche `refused: …` et n'écrit **rien**.

## Installer sur l'appareil

### 1. Copier sur la carte SD

1. **Formatez la carte SD dans l'appareil.**
2. Copiez **`output/fwdc248b.bin`** à la **racine** de la carte : pas dans un
   dossier, et gardez exactement le nom `fwdc248b.bin`.

### 2. Mettre à jour l'appareil

1. Insérez la batterie complètement chargée et la carte SD.
2. Lancez la mise à jour du firmware depuis le menu de configuration de
   l'appareil, comme décrit dans les instructions officielles de RICOH pour la
   mise à jour du firmware du GR IV.
3. **L'appareil affiche une mise à jour de la version 1.11 vers la version 1.11.**
   C'est normal : le firmware débloqué conserve le numéro de version. Confirmez
   la mise à jour.

> [!CAUTION]
> **N'éteignez pas l'appareil, n'ouvrez pas la trappe de la batterie ou de la
> carte et ne retirez pas la carte** avant que la mise à jour soit terminée et
> que l'appareil ait redémarré.

### 3. Photographier

- Ouvrez **Contrôle de l'image** : les nouveaux looks suivent le premier
  « HDR Tone ».
- La version du firmware affiche toujours **1.11**. C'est normal.
- Supprimez `fwdc248b.bin` de la carte (ou formatez la carte) pour que la mise à
  jour ne soit pas relancée par erreur.

### Revenir au firmware officiel

Répétez les étapes 1–2, cette fois avec le `fwdc248b.bin` **officiel** de RICOH.
L'appareil affiche à nouveau **1.11 → 1.11** ; confirmez, et votre appareil
retrouve son état d'origine.

## Bon à savoir

- **Deux entrées « Standard » et deux entrées « HDR Tone ».** Les looks
  monochromes Standard et HDR utilisent les mêmes noms et icônes que les looks
  couleur. Les nouveaux sont les entrées qui suivent le premier « HDR Tone ».
- **Soft, Grainy et HDR sont réservés à la photo**, comme sur le modèle
  monochrome.
- **Monochrome HDR est expérimental.** Son écran de réglages propose moins
  d'options que les autres looks. Il n'a pas encore été essayé sur un appareil ;
  merci de signaler comment il se comporte.
- **Une mise à jour officielle de RICOH supprime le déblocage.** Elle remplace
  l'intégralité du firmware.
- **Uniquement pour le GR IV standard en 1.11.** N'installez jamais ce fichier
  sur un autre modèle, et n'utilisez pas l'outil avec une autre version de
  firmware.
- **Avant d'envoyer l'appareil en réparation,** revenez au firmware officiel.

### Vérifier un fichier de firmware

Avant de copier un fichier de firmware sur une carte :

```sh
python3 gr4_monounlock.py check path/to/fwdc248b.bin
```

Cette commande vous indique si le fichier est le 1.11 officiel, la version
débloquée créée par cet outil ou autre chose.

## Risques

- Votre appareil ne sait pas distinguer un bon fichier de firmware d'un fichier
  endommagé. Ne copiez sur votre carte qu'un fichier écrit par l'outil (ou
  confirmé avec `check`).
- Si une mise à jour est interrompue, ou si un fichier de firmware ne peut pas
  démarrer, l'appareil risque de ne plus pouvoir accéder à la fonction de mise à
  jour, et devrait alors passer par le service après-vente de RICOH. Cela ne
  s'est pas produit lors des tests, mais on ne peut pas l'exclure.
- Les données d'étalonnage propres à votre appareil ne sont pas modifiées.

## État des tests

| Élément | État |
| --- | --- |
| Mise à jour acceptée ; Standard, Soft, High Contrast et Solid apparaissent et fonctionnent | testé sur un GR IV 1.11 |
| Revenir au 1.11 officiel restaure entièrement l'appareil | testé sur un GR IV 1.11 |
| Grainy | inclus dans des versions de test qui se sont installées et ont démarré sur un GR IV 1.11 |
| Monochrome HDR | pas encore essayé sur un appareil |
| L'outil reproduit exactement le firmware testé | testé |

## Fichiers

```
GR4-MonoUnlock/
├── README.md            this guide
├── gr4_monounlock.py    the tool
└── assets/              the icon (SVG, and a 512 px PNG)
```

| Fichier | SHA-256 |
| --- | --- |
| `fwdc248b.bin` officiel RICOH GR IV 1.11 | `a2f664dfca034059eb0fd6e18ab08684c326b4a034d85c164dad7e1ec9b5655f` |
| `fwdc248b.bin` débloqué créé par cet outil | `4c04b48c65897f2edd028df0f5e04666ca241488c81502bae0f34e040ee454eb` |
