import time


def test_asr(model, audio_file_path, language=None):
    start_time = time.perf_counter()
    print(f"\nФайл: {audio_file_path.name}", flush=True)
    segments, info = model.transcribe(
        str(audio_file_path), language=language, beam_size=5
    )
    print(f"Language: {info.language} p = {info.language_probability:.2f}")
    for segment in segments:
        print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}", flush=True)
    print(f"Time: {time.perf_counter() - start_time:.2f} сек.")
