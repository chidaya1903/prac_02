"""Password check using functions (no globals)."""

MIN_LENGTH = 5


def main():
    """Run the password checker and print stars equal to the password length."""
    password = get_password(MIN_LENGTH)
    print_stars(password)


def get_password(min_length: int) -> str:
    """Return a password string that is at least min_length characters."""
    password = input("Password: ")
    while len(password) < min_length:
        print(f"Password must be at least {min_length} characters.")
        password = input("Password: ")
    return password


def print_stars(text: str) -> None:
    """Print stars equal to the length of text."""
    print("*" * len(text))


if __name__ == "__main__": 
    main()
