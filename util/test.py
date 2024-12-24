from typing import Callable, Any


def test_case(function: Callable, result: Any, *args, **kwargs):
    call = function(*args, **kwargs)
    if call == result:
        print_green("Test case - OK")
    else:
        print_red(f'Test case - not OK\n\tOutput: {call}\n\tExpected: {result}')


def print_green(text: str) -> None:
    print("\033[3m\033[32m{}\033[0m".format(text))


def print_red(text: str) -> None:
    print("\033[3m\033[31m{}\033[0m".format(text))
