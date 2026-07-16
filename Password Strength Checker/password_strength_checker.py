import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one uppercase letter.")

    # Lowercase Check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one lowercase letter.")

    # Number Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number.")

    # Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one special character.")

    # Strength Rating
    if score == 5:
        strength = "🟢 Very Strong"
    elif score == 4:
        strength = "🟢 Strong"
    elif score == 3:
        strength = "🟡 Medium"
    elif score == 2:
        strength = "🟠 Weak"
    else:
        strength = "🔴 Very Weak"

    return strength, feedback


def main():
    print("=" * 40)
    print("      PASSWORD STRENGTH CHECKER")
    print("=" * 40)

    password = input("Enter your password: ")

    strength, feedback = check_password_strength(password)

    print("\nPassword Strength:", strength)

    if feedback:
        print("\nSuggestions:")
        for item in feedback:
            print(item)
    else:
        print("✅ Excellent password!")


if __name__ == "__main__":
    main()