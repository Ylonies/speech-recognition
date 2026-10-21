import argparse
from pathlib import Path


AUDIO_DIR = Path(__file__).resolve().parent.parent / "audio"


def parse_args():
    parser = argparse.ArgumentParser(description="Распознавание WAV-файлов.")
    parser.add_argument(
        "--audio-dir", type=Path, default=AUDIO_DIR, help="Папка с WAV-файлами"
    )
    parser.add_argument("--model", default="large-v3-turbo", help="Модель Whisper")
    parser.add_argument(
        "--language", default=None,
        help="Язык, например ru или en; по умолчанию определяется автоматически",
    )
    args = parser.parse_args()
    if not args.audio_dir.is_dir():
        parser.error(f"Папка не найдена: {args.audio_dir}")
    audio_files = sorted(
        path for path in args.audio_dir.iterdir()
        if path.is_file() and path.suffix.lower() == ".wav"
    )
    if not audio_files:
        parser.error(f"В папке нет WAV-файлов: {args.audio_dir}")
    return args, audio_files
