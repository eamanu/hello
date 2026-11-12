def greet(name: str = "world") -> str:
    return f"hello {name}"


def main() -> None:
    print(greet())
