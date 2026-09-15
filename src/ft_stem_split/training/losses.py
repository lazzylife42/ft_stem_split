"""Fonctions de loss pour l'entraînement (L1/L2 sur spectrogramme).

Phase 2 de la roadmap. Squelette de signatures, pas de logique.
"""

import tensorflow as tf


def spectral_l1_loss(y_true: tf.Tensor, y_pred: tf.Tensor) -> tf.Tensor:
    """Erreur absolue moyenne entre magnitude log prédite et cible."""
    raise NotImplementedError
