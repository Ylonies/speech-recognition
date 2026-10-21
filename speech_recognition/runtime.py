import ctypes
import platform
import site
from pathlib import Path


_loaded_libraries = []


def model_settings():
    if platform.system() == "Darwin":
        return {"device": "cpu", "compute_type": "int8"}
    if platform.system() == "Linux":
        load_nvidia_libraries()
        return {"device": "cuda", "compute_type": "float16"}
    return {"device": "cpu", "compute_type": "int8"}


def load_nvidia_libraries():
    packages_paths = site.getsitepackages() + [site.getusersitepackages()]
    loaded_names = []
    for base_path in packages_paths:
        for library, pattern in (
            ("cublas", "libcublas.so.12*"),
            ("cudnn", "libcudnn.so.9*"),
        ):
            lib_dir = Path(base_path) / "nvidia" / library / "lib"
            for path in sorted(lib_dir.glob(pattern)):
                try:
                    _loaded_libraries.append(ctypes.CDLL(str(path)))
                    loaded_names.append(path.name)
                except OSError as error:
                    print(f"Not loaded {path.name}: {error}")
    print("Loaded:", loaded_names)
