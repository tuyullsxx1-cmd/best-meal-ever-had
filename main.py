"""One-line entry for the Best Meal You Ever Had bounty.

A single sentence, at most 200 characters, about the best meal
ever had. The sentence has to stand alone: concrete, personal, and
worth remembering — a grandmother's rendang, eaten by hand off a
banana leaf in the small hours, the house still smelling of coconut
milk and woodsmoke, everyone too full and too happy to move. The
program writes the line to /output/entry.txt.
"""
import os

LINE = "My grandmother's rendang, eaten by hand off a banana leaf at 2 a.m. after a wedding, while the whole house still smelled of coconut milk and woodsmoke."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
