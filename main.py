import os
import sys
import site
import ctypes

packages_paths = site.getsitepackages() + [site.getusersitepackages()]

nvidia_libs = []
for base_path in packages_paths:
    nvidia_dir = os.path.join(base_path, "nvidia")
    if os.path.exists(nvidia_dir):
        for sub in ["cublas", "cudnn"]:
            sub_path = os.path.join(nvidia_dir, sub, "lib")
            if os.path.exists(sub_path):
                nvidia_libs.append(sub_path)

loaded_libs = []
for lib_dir in nvidia_libs:
    if os.path.exists(lib_dir):
        for file in os.listdir(lib_dir):
            if "libcublas.so.12" in file or "libcudnn.so.9" in file:
                full_path = os.path.join(lib_dir, file)
                try:
                    ctypes.CDLL(full_path)
                    loaded_libs.append(file)
                except Exception as e:
                    print(f"Not loaded {file}: {e}")

print("Loaded:", loaded_libs)


import sys
if 'av' in sys.modules:
    del sys.modules['av']

from faster_whisper import WhisperModel
import time



model_size = "large-v3-turbo"
model = WhisperModel(model_size, device="cuda", compute_type="float16")



def test_asr(audio_file_path):
    start_time = time.time()
    
    segments, info = model.transcribe(audio_file_path, language="en", beam_size=5)
    
    print(f"Language: {info.language} p = {info.language_probability:.2f}")
    
    for segment in segments:
        print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")
        
    end_time = time.time()
    print(f"Time: {end_time - start_time:.2f} сек.")

test_asr("audio.wav")