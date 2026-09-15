"""Training loop du U-Net.

Phase 2 de la roadmap. Squelette de signature, pas de logique.
"""

from pathlib import Path


def train(config_path: Path) -> None:
    """Lance l'entraînement à partir d'un fichier de config (hyperparamètres, chemins).

    Raises:
        ValueError: si config_path n'existe pas ou config invalide.
    """
    raise NotImplementedError


if __name__ == "__main__":
    raise NotImplementedError("Entrypoint à définir une fois le training loop écrit.")
