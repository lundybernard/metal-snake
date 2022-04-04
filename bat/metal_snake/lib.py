from .rust import (
    rfib,
    busy_fib,
    hello_rust,
)


def fib(n: int) -> int:
    return rfib(n)


def hello(input_text: str) -> None:
    hello_rust(input_text)
