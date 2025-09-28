"""Menu-driven score program using functions."""

MENU = "(G)et score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    """Run the score menu program."""
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").strip().upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(get_result(score))
        elif choice == "S":
            print("*" * int(score))
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").strip().upper()
    print("Finished.")


def get_valid_score() -> float:
    """Prompt until the user enters a valid score 0..100 inclusive; return it."""
    score = float(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid score (must be 0–100).")
        score = float(input("Score: "))
    return score


def get_result(score: float) -> str:
    """Return the classification for a score (assumes 0..100)."""
    if score >= 90:
        return "Excellent"
    if score >= 50:
        return "Passable"
    return "Bad"


if __name__ == "__main__":
    main()
