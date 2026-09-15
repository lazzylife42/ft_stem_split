"""Architecture U-Net convolutif from scratch pour le masking spectral.

Phase 2 de la roadmap (v1 : un seul stem, mono). Squelette de signature, pas de logique
(référence : Jansson et al., "Singing Voice Separation with Deep U-Net Convolutional
Networks").
"""

import keras


def build_unet(input_shape: tuple[int, int, int]) -> keras.Model:
    """Construit le modèle U-Net (encoder/decoder + skip connections) prédisant un
    masque spectral appliqué à la magnitude log du mix.

    Args:
        input_shape: (n_freq_bins, n_time_frames, n_channels).

    Raises:
        ValueError: si input_shape a un nombre de dimensions incorrect.
    """
    raise NotImplementedError
