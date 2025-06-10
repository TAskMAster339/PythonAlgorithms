#!/usr/bin/env -S uv run --script
import argparse
import re
import subprocess
from pathlib import Path

ROOT_DIR = Path(__file__).parent.resolve()
FILE_OUTPUT_NAME = "text.txt"
TXT_EDITOR_PATH = Path(r"/mnt/c/Program\ Files/Sublime\ Text/sublime_text.exe")


def get_path_from_regex(path_regex: str) -> Path:
    dir_pattern = re.compile(path_regex)
    parent_dir = Path(__file__).resolve().parent
    for path in Path.iterdir(parent_dir):
        if dir_pattern.match(path.name):
            return path
    raise FileNotFoundError


def get_deafult_txt_template(dir_path: Path) -> list[str]:
    lines = []
    number, name = dir_path.name.split(".")
    lines.append(f"{number}) {name}\n\n")
    lines.append("Условие:\n\n")
    lines.append("Идея:\n\n")
    lines.append("Реализация:\n    \n\n")
    lines.append("Оценка:\n    ")

    return lines


parser = argparse.ArgumentParser()
parser.add_argument(
    "regex_path",
    type=str,
    help=f"Directory with {FILE_OUTPUT_NAME} to parse regex path",
)

if __name__ == "__main__":
    args = parser.parse_args()
    try:
        dir_path = get_path_from_regex(args.regex_path)
        try:
            with Path.open(
                dir_path / FILE_OUTPUT_NAME,
                "w",
                encoding="UTF-8",
            ) as file:
                file.writelines(get_deafult_txt_template(dir_path))
            path = str(dir_path / FILE_OUTPUT_NAME).replace(" ", r"\ ")[6:]
            subprocess.run(
                [str(TXT_EDITOR_PATH), path],
                check=True,
                shell=True,
            )
        except FileNotFoundError:
            print(f"file {path} not found")

    except FileNotFoundError:
        print("Directory not found")
    except Exception as e:
        print(e)
