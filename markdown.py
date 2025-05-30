#!/usr/bin/env -S uv run --script

import argparse
import re
from pathlib import Path

file_lines = []
code_lines = []

QUESTION_PATTERN = re.compile(r"\d+")
HEADER_PATTERN = re.compile(r"\d+\) \w+")
WORDS_PATTERN = re.compile(r"\w+|\W+")
ENGLISH_WORD_PATTERN = re.compile(r"[a-zA-Z0-9]+")

GITHUB_PATH = "https://github.com/TAskMAster339/PythonAlgorithms/tree/main/"
ROOT_DIR = Path(__file__).resolve().parent

FILE_OUTPUT_NAME = "tg.md"
CODE_FILE_NAME = "main.py"
FILE_INPUT_NAME = "text.txt"

BLOCK_WORDS = ("Условие:", "Идея:", "Реализация:", "Оценка:")


def parse_bool_from_str(string: str) -> bool:
    if not string:
        return False
    bools = ("true", "t", "1", "y", "yes")
    return string.lower() in bools


def bold_english_words(string: str) -> str:
    words = WORDS_PATTERN.findall(string)
    for i in range(len(words)):
        if words[i] and ENGLISH_WORD_PATTERN.search(words[i]):
            words[i] = wrap_with(words[i], "**")
    return "".join(words)


def wrap_with(string: str, wrapper: str) -> str:
    if wrapper.startswith("<") and wrapper.endswith(">"):
        wrapper = wrapper.strip("<").strip(">")
        return f"<{wrapper}>{string}</{wrapper}>"
    return wrapper + string + wrapper


def format_file(file_lines: list[str]) -> None:
    header = file_lines[0]  # header is the first, second is the link
    if HEADER_PATTERN.match(header):
        header = wrap_with(header, "**")
        file_lines[0] = header
    for i in range(2, len(file_lines)):
        line = file_lines[i]
        if line in BLOCK_WORDS:
            file_lines[i] = wrap_with(line, "**")
        else:
            file_lines[i] = bold_english_words(line)


def format_file_for_git(file_lines: list[str], code_lines: list[str]) -> None:
    for i in range(len(file_lines)):
        file_lines[i] = file_lines[i].strip()
        if file_lines[i].strip("*") in BLOCK_WORDS:
            file_lines[i] = f"## {file_lines[i]}"
    link = file_lines.pop(1)
    file_lines[0] = (
        f"<div align='center'>\n<h1><a href='{link}'>"
        f"<strong>{file_lines[0].replace('*', '')}</strong></a></h1>\n</div>"
    )

    # add code
    try:
        with Path.open(
            dir_path / CODE_FILE_NAME,
            "r",
            encoding="UTF-8",
        ) as file:
            code_lines.append("## Код:\n```python")
            for line in file.readlines():
                code_lines += [line.removesuffix("\n")]
            code_lines.append("\n```\n")
    except FileNotFoundError:
        print("e")


def get_link_to_next_and_prev_questions(dir_path: Path) -> str:
    string = ""
    next_question = prev_question = ""
    number, _ = dir_path.name.split(".")
    for path in Path.iterdir(ROOT_DIR):
        if path.is_dir() and QUESTION_PATTERN.match(path.name):
            num, name = path.name.split(".")
            if int(number) + 1 == int(num):
                next_question = (
                    f"<a href='{GITHUB_PATH + path.name.replace(' ', '%20')}'>"
                    f"следующая задача ➡️</a>"
                )
            if int(number) - 1 == int(num):
                prev_question = (
                    f"<a href='{GITHUB_PATH + path.name.replace(' ', '%20')}'>"
                    f"⬅️ предыдущая задача</a>"
                )
    all_questions = f"<a href='{GITHUB_PATH + 'README.md'}'>Все задачи</a>"
    if not prev_question:
        string = (
            f"<div align='center'><h3>{all_questions}"
            f"&nbsp;|&nbsp;{next_question}</h3></div>"
        )
    elif not next_question:
        string = (
            f"<div align='center'><h3>{prev_question}"
            f"&nbsp;|&nbsp;{all_questions}</h3></div>"
        )
    else:
        string = (
            f"<div align='center'><h3>{prev_question}"
            f"&nbsp;|&nbsp;{all_questions}"
            f"&nbsp;|&nbsp;{next_question}</h3></div>"
        )
    if string:
        return string
    return ""


def get_prev_dir(dir_path: Path) -> Path | None:
    number, _ = dir_path.name.split(".")
    for path in Path.iterdir(ROOT_DIR):
        if path.is_dir() and QUESTION_PATTERN.match(path.name):
            num, name = path.name.split(".")
            if int(number) - 1 == int(num):
                return path
    return None


def get_path_from_regex(path_regex: str) -> Path:
    dir_pattern = re.compile(path_regex)
    parent_dir = Path(__file__).resolve().parent
    for path in Path.iterdir(parent_dir):
        if dir_pattern.match(path.name):
            return path
    raise FileNotFoundError


parser = argparse.ArgumentParser()
parser.add_argument(
    "regex_path",
    type=str,
    help=f"Directory with {FILE_INPUT_NAME} to parse regex path",
)
if __name__ == "__main__":
    args = parser.parse_args()
    try:
        # read data from txt file
        dir_path = get_path_from_regex(args.regex_path)
        try:
            with Path.open(
                dir_path / FILE_INPUT_NAME,
                "r",
                encoding="UTF-8",
            ) as file:
                file_lines = file.readlines()
                for i in range(len(file_lines)):
                    file_lines[i] = file_lines[i].removesuffix("\n")
        except FileNotFoundError:
            print(f"file {dir_path / FILE_INPUT_NAME} not found")
        # create md file for tg post
        format_file(file_lines)

        with Path.open(
            dir_path / FILE_OUTPUT_NAME,
            "w",
            encoding="UTF-8",
        ) as file:
            lines = [line + "\n" for line in file_lines]
            file.writelines(lines)

        print(f"Created {FILE_OUTPUT_NAME} in {dir_path}")
        # create README.md for github
        format_file_for_git(file_lines, code_lines)

        with Path.open(
            dir_path / "README.md",
            "w",
            encoding="UTF-8",
        ) as file:
            file.writelines([line + "\n\n" for line in file_lines])

            file.writelines([line + "\n" for line in code_lines])
            file.write(get_link_to_next_and_prev_questions(dir_path))

        print(f"Created README.md in {dir_path}")

        # updat next link in previus README.md question
        prev_dir_path = get_prev_dir(dir_path)
        try:
            with Path.open(
                prev_dir_path / "README.md",
                "r",
                encoding="UTF-8",
            ) as file:
                file_lines = file.readlines()
            with Path.open(
                prev_dir_path / "README.md",
                "w",
                encoding="UTF-8",
            ) as file:
                if "следующая задача" not in file_lines[-1]:
                    file_lines[-1] = get_link_to_next_and_prev_questions(
                        prev_dir_path,
                    )
                file.writelines(file_lines)

            print(f"Updated README.md in {prev_dir_path}")
        except FileNotFoundError as e:
            print(e)

    except FileNotFoundError:
        print("Directory not found")
    except Exception as e:
        print(e)
