# Roadmap ft_stem_split

Rythme visé : ~12h/semaine sur la fenêtre projets perso.

- [ ] **1. Prépro** : charger MUSDB18-HQ, STFT log-magnitude, pipeline `tf.data`,
      augmentation (pitch/time/remix aléatoire de stems).
- [ ] **2. Modèle v1** : U-Net Keras from scratch, un seul stem (vocals), mono. Loss
      L1/L2 sur spectrogramme, éval SDR via `museval`.
- [ ] **3. Extension multi-stem** : drums/bass/other, stéréo, si v1 est concluant.
- [ ] **4. Optimisation déploiement** : quantization TFLite, export ONNX, benchmark
      latence/taille sur Raspberry Pi 5 (réutilise le hardware mappy).
- [ ] **5. CLI standalone** intégré à `music_daemon`.
- [ ] **6. Plugin JUCE** (standalone + VST3/AU), traitement offline/batch, charge le
      modèle ONNX/TFLite.
- [ ] **7. (stretch)** Device Max for Live et/ou Extension Ableton (Live Suite
      12.4.5+, bêta) pour l'intégrer dans Live 12.

## État actuel

Repo initialisé (structure, deps, stubs archi). Rien d'implémenté. Prochaine étape :
Phase 1, télécharger MUSDB18-HQ dans `data/` et écrire `data/preprocessing.py`
(STFT/ISTFT round-trip) en premier, avant le loader (le round-trip sans perte est le
prérequis testable indépendamment du dataset).

## Compute

Training sur RTX 3060 (12GB VRAM) : suffisant pour v1 (mono, un stem). Réduire le
batch size si besoin en passant en stéréo multi-stem (phase 3).

## Ressources

- Jansson et al., "Singing Voice Separation with Deep U-Net Convolutional Networks"
- [MUSDB18-HQ (Zenodo)](https://zenodo.org/records/3338373)
- `museval` pour l'évaluation SDR/SIR/SAR
- [JUCE framework](https://juce.com)
- [Max for Live](https://www.ableton.com/en/live-manual/12/max-for-live/)
- [Ableton Extensions (bêta)](https://cdm.link/ableton-extensions-beta)
