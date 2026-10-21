# Распознавание речи на macOS и Linux

На macOS используется faster-whisper на CPU с `compute_type="int8"`.
На Linux сохраняется исходный режим: NVIDIA CUDA с `compute_type="float16"`.

`main.py` содержит загрузку модели и цикл обработки файлов.
Вспомогательная логика находится в `speech_recognition/`:

- `runtime.py` — выбор режима по ОС и загрузка NVIDIA-библиотек на Linux;
- `cli.py` — аргументы командной строки и поиск WAV-файлов;
- `audio.py` — распознавание, временные метки и замер времени.

## Установка

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Аудиофайлы

Поместите WAV-файлы в папку `audio/` рядом с `main.py`.
Скрипт последовательно обрабатывает все WAV-файлы непосредственно в этой папке
в алфавитном порядке, включая расширение `.WAV`.
В неё перенесены `sample_1.wav` и `sample_2.wav`.

## Запуск

Из корня проекта:

```sh
.venv/bin/python main.py
```

По умолчанию используется `large-v3-turbo`, язык определяется автоматически.
Модель скачивается при первом запуске, поэтому потребуется интернет
и свободное место на диске. Следующие запуски используют локальный кеш.
Результаты с временными метками выводятся в терминал.

Можно выбрать язык, другую папку или меньшую модель для экономии памяти:

```sh
.venv/bin/python main.py --language ru
.venv/bin/python main.py --audio-dir /path/to/wav
.venv/bin/python main.py --model small
```
