from speech_recognition.audio import test_asr
from speech_recognition.cli import parse_args
from speech_recognition.runtime import model_settings

from faster_whisper import WhisperModel

def main():
    args, audio_files = parse_args()
    settings = model_settings()


    model_size = args.model
    print(
        f"Загрузка модели {model_size} ({settings['device']}, {settings['compute_type']}). "
        "При первом запуске модель скачивается из интернета.", flush=True,
    )
    model = WhisperModel(model_size, **settings)
    for audio_file_path in audio_files:
        test_asr(model, audio_file_path, language=args.language)


if __name__ == "__main__":
    main()
