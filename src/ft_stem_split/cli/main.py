"""CLI ft_stem_split (Click/Rich, même stack que music_daemon).

Phase 5 de la roadmap. Squelette de signature, pas de logique.

Usage prévu :
    ft_stem_split split track.wav --output-dir ./stems
"""

import click


@click.group()
def cli():
    """ft_stem_split : séparation de sources audio (voix/batterie/basse/autre)."""


@cli.command()
@click.argument("track_path", type=click.Path(exists=True))
@click.option("--output-dir", type=click.Path(), default="./stems")
def split(track_path: str, output_dir: str) -> None:
    """Sépare TRACK_PATH en stems isolés dans OUTPUT_DIR."""
    raise NotImplementedError


if __name__ == "__main__":
    cli()
