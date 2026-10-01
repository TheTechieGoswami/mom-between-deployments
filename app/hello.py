def hello(name: str = "Mom Between Deployments") -> str:
    return f"Hello from {name}!"


if __name__ == "__main__":
    print(hello())
