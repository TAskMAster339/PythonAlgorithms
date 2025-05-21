import argparse
import re
from pathlib import Path

file_lines = []

HEADER_PATTERN = re.compile(r"\d+\) \w+")

WORDS_PATTERN = re.compile(r"\w+|\W+")

ENGLISH_WORD_PATTERN = re.compile(r"[a-zA-Z0-9]+")

BLOCK_WORDS = ("Условие:", "Идея:", "Реализация:", "Оценка:")

FILE_INPUT_NAME = "text.txt"
FILE_OUTPUT_NAME = "README.md"  # for github


def bold_english_words(string: str) -> str:
    words = WORDS_PATTERN.findall(string)
    for i in range(len(words)):
        if words[i] and ENGLISH_WORD_PATTERN.search(words[i]):
            words[i] = wrap_with(words[i], "**")
    return "".join(words)


def wrap_with(string: str, wrapper: str) -> str:
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
        dir_path = get_path_from_regex(args.regex_path)

        with Path.open(
            dir_path / FILE_INPUT_NAME,
            "r",
            encoding="UTF-8",
        ) as file:
            file_lines = file.readlines()
            for i in range(len(file_lines)):
                file_lines[i] = file_lines[i].removesuffix("\n")

        format_file(file_lines)

        with Path.open(
            dir_path / FILE_OUTPUT_NAME,
            "w",
            encoding="UTF-8",
        ) as file:
            lines = [line + "\n" for line in file_lines]
            file.writelines(lines)

        print(f"Created {FILE_OUTPUT_NAME} in {dir_path}")
    except FileNotFoundError:
        print("Directory not found")
    except Exception as e:
        print(e)
