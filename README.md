# ft_stem_split

Séparateur de sources audio (voix, batterie, basse, autre) dans un mix, avec un modèle
de deep learning implémenté from scratch, entraîné sur MUSDB18-HQ, optimisé pour
tourner sur hardware contraint (Raspberry Pi 5 / ARM), et utilisable en prod dans un
setup DJ/Ableton Live 12 (CLI standalone, plugin JUCE offline).

Pas de lien technique avec le projet ISO-3 (EQ analogique) : même axe audio/DJ, projets
indépendants.

## Objectif

- Projet vitrine pour combler le gap Audio ML (TensorFlow/Keras, curation/augmentation
  de dataset audio, déploiement ML sur plateforme contrainte) sur les offres tier-1.
- Outil utilisé réellement en DJ/prod : extraction acapella/instru pour mashups,
  isolation d'un stem pour un edit.

## Règles

- Zéro génération IA : tout le code (modèle, training loop, plugin, intégration
  Ableton) est écrit et compris par l'auteur, pas généré. Claude sert de prof/reviewer,
  pas d'auteur.
- From scratch : pas de `spleeter` / `demucs` comme solution. Archi U-Net Keras,
  pipeline de prépro et reconstruction ISTFT maison. Papers/librairies en référence
  uniquement.
- PEP8, gestion d'erreurs explicite (`raise ValueError`), jamais de fallback silencieux.
- Pas de dataset ni de poids de modèle commités (`.gitignore`), secrets en `.env`.

## Stack

**Cœur ML (Python)**
- TensorFlow / Keras : U-Net convolutif from scratch, masking spectral
- librosa / numpy : STFT/ISTFT, prépro spectrogrammes log-magnitude
- Dataset : [MUSDB18-HQ](https://zenodo.org/records/3338373) + augmentation maison
  (pitch shift, time stretch, remix aléatoire de stems)
- `museval` : évaluation SDR/SIR/SAR

**Outil standalone**
- CLI Python (Click/Rich, même stack que `music_daemon`) : `ft_stem_split split
  track.wav`

**Plugin**
- JUCE (C++) : standalone + VST3/AU depuis un seul projet
- Modèle exporté ONNX/TFLite, chargé côté C++ (ONNX Runtime / TFLite C++ API)
- Traitement offline/batch (pas de streaming temps réel, contexte multi-secondes
  nécessaire au modèle)

**Intégration Ableton Live 12**
- Max for Live (device audio natif) et/ou Ableton Extensions (stretch goal, bêta)

## Structure du repo

```
ft_stem_split/
├── src/ft_stem_split/
│   ├── data/          # chargement MUSDB18, STFT/ISTFT, augmentation
│   ├── models/         # archi U-Net
│   ├── training/        # training loop, losses
│   ├── evaluation/       # éval SDR/SIR/SAR (museval)
│   └── cli/            # CLI ft_stem_split
├── tests/
├── configs/           # hyperparamètres training
├── data/              # MUSDB18 téléchargé (gitignored)
├── models_weights/     # poids entraînés (gitignored)
└── notebooks/          # exploration
```

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Dataset MUSDB18-HQ à télécharger dans `data/` (voir `configs/`).

## Roadmap

Voir [ROADMAP.md](./ROADMAP.md).
