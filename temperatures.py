"""Temperature converter with SRP functions and a simple menu."""

MENU = "(C)elsius to Fahrenheit\n(F)ahrenheit to Celsius\n(Q)uit"


def main():
    """Display a menu and perform conversions until the user quits."""
    print(MENU)
    choice = input(">>> ").strip().upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            print(f"Result: {c_to_f(celsius):.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            print(f"Result: {f_to_c(fahrenheit):.2f} C")
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").strip().upper()
    print("Thank you.")


def c_to_f(celsius: float) -> float:
    """Return Fahrenheit for a given Celsius value."""
    return celsius * 9 / 5 + 32


def f_to_c(fahrenheit: float) -> float:
    """Return Celsius for a given Fahrenheit value."""
    return (fahrenheit - 32) * 5 / 9


if __name__ == "__main__":
    main()
