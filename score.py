"""Read a score, print its result, then do the same for a random score."""

import random


def main():
    """Ask for a score, print its classification, then classify a random score."""
    score = float(input("Score: "))
    print(get_result(score))

    random_score = random.uniform(0, 100)
    print(f"Random score: {random_score:.2f} -> {get_result(random_score)}")


def get_result(score: float) -> str:
    """Return the classification for a score (0..100 inclusive)."""
    if score < 0 or score > 100:
        return "Invalid score"
    if score >= 90:
        return "Excellent"
    if score >= 50:
        return "Passable"
    return "Bad"


if __name__ == "__main__":
    main()
