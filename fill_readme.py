#!/usr/bin/env -S uv run --script

import math
import re
from pathlib import Path

questions_names = []

QUESTION_PATTERN = re.compile(r"\d+")
GITHUB_PATH = "https://github.com/TAskMAster339/PythonAlgorithms/tree/main/"
ROOT_DIR = Path(__file__).resolve().parent
TOTAL_QUESTIONS = 150


def generate_progress_bar(
    current: int,
    total: int,
    bar_length: int = 40,
) -> str:
    percent = current / total
    filled = math.floor(bar_length * percent)
    bar = "█" * filled + "-" * (bar_length - filled)

    percent_str = f"{percent:.0%}".rjust(4)
    return f"Прогресс: [{bar}] {percent_str}\n"


try:
    for path in Path.iterdir(ROOT_DIR):
        if path.is_dir() and QUESTION_PATTERN.match(path.name):
            questions_names += [path.name]

    questions_names.sort(key=lambda s: int(s.split(".")[0]))

    with Path.open("README.md", "w", encoding="UTF-8") as file:
        file.write(
            "# Решаю [150 топовых задач для интервью]"
            "(https://leetcode.com/studyplan/top-interview-150/) на Python\n\n",
        )
        file.write(
            ">[!TIP]\n>Вот [тут](https://t.me/TAskMAster3399) "
            "я поясняю за решение\n\n",
        )
        file.write(generate_progress_bar(len(questions_names), 150))
        file.write("\n## Список задач:\n\n")
        for line in questions_names:
            number, name = line.split(".")
            path = GITHUB_PATH + line.replace(" ", "%20")
            file.write(
                f"{number}. [{name}]({path})\n\n",
            )
    print("README.md updated successfuly")
except Exception as e:
    print(e)
