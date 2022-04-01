from .rust import (
    rfib,
    hello_rust,
)


def fib(n: int) -> int:
    return rfib(n)


def hello(input_text: str) -> None:
    hello_rust(input_text)
