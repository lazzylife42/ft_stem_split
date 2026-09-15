"""Évaluation SDR/SIR/SAR via museval.

Phase 2+ de la roadmap. Squelette de signature, pas de logique.
"""

from pathlib import Path


def evaluate_model(model_path: Path, test_set_path: Path) -> dict:
    """Évalue un modèle entraîné sur le test set MUSDB18 et retourne les métriques
    SDR/SIR/SAR (museval) par stem.

    Raises:
        ValueError: si model_path ou test_set_path n'existent pas.
    """
    raise NotImplementedError
