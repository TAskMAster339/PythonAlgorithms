__all__ = ["test_case"]

from typing import Any, Callable


def test_case(function: Callable, result: Any, *args, **kwargs) -> None:
    call = function(*args, **kwargs)
    if call == result:
        print_green("Test case - OK")
    else:
        print_red(
            f"Test case - not OK\n\tOutput: {call}\n\tExpected: {result}",
        )


def print_green(text: str) -> None:
    print(f"\033[3m\033[32m{text}\033[0m")


def print_red(text: str) -> None:
    print(f"\033[3m\033[31m{text}\033[0m")
