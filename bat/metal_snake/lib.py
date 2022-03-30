from .rust import hello_rust


def hello(input_text: str) -> None:
    hello_rust(input_text)
