from typing import Callable, Any


def test_case(function: Callable, result: Any, *args, **kwargs):
    call = function(*args, **kwargs)
    print(f'Output is {call}')
    assert call == result
    print("OK")
