import re

def check_password_strength(password):
    strength = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase and lowercase
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should include both uppercase and lowercase letters.")

    # Check for digits
    if re.search(r'\d', password):
        strength += 1
    else:
        feedback.append("Password should include at least one number.")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one special character.")

    # Determine strength
    if strength == 4:
        return "Strong password!", []
    elif strength == 3:
        return "Moderate password.", feedback
    else:
        return "Weak password.", feedback

if __name__ == "__main__":
    print("Welcome to the Password Strength Checker!")
    user_password = input("Enter a password to test its strength: ")
    result, suggestions = check_password_strength(user_password)
    print(f"\nResult: {result}")
    if suggestions:
        print("Suggestions:")
        for suggestion in suggestions:
            print(f"- {suggestion}")
