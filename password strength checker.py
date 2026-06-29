import re

def check_password_strength(password):
    score = 0
    suggestions = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    # Number check
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add at least one number.")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add at least one special character.")

    # Strength rating
    if score == 5:
        strength = "Very Strong 💪"
    elif score == 4:
        strength = "Strong ✅"
    elif score == 3:
        strength = "Medium ⚠️"
    elif score == 2:
        strength = "Weak ❌"
    else:
        strength = "Very Weak 🚨"

    return strength, suggestions


def main():
    print("=" * 40)
    print("      PASSWORD STRENGTH CHECKER")
    print("=" * 40)

    password = input("Enter your password: ")

    strength, suggestions = check_password_strength(password)

    print("\nPassword Strength:", strength)

    if suggestions:
        print("\nSuggestions:")
        for suggestion in suggestions:
            print(f"- {suggestion}")
    else:
        print("\nExcellent! Your password follows all recommended practices.")


if __name__ == "__main__":
    main()