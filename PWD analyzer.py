import re

def evaluate_password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"\W", password):
        score += 1
    return score

def detect_password_weakness(password):
    weaknesses = []
    if len(password) < 8:
        weaknesses.append("Password is too short (should be at least 8 characters).")
    if re.search(r"(\w)\1{2,}", password):
        weaknesses.append("Password contains repeated characters.")
    # Add more weakness checks as needed
    return weaknesses

def recommend_security_practices(password):
    recommendations = []
    if len(password) < 12:
        recommendations.append("Consider using a longer password (at least 12 characters).")
    if len(password) >= 8 and len(password) < 12:
        recommendations.append("Consider adding more characters to increase password strength.")
    if not re.search(r"[A-Z]", password):
        recommendations.append("Consider using at least one uppercase letter.")
    # Add more recommendations based on the weaknesses detected
    return recommendations

if __name__ == "__main__":
    password = input("Enter your password: ")
    strength_score = evaluate_password_strength(password)
    print(f"Password strength score: {strength_score}/5")
    weaknesses = detect_password_weakness(password)
    if weaknesses:
        print("Weaknesses found:")
        for weakness in weaknesses:
            print(f"- {weakness}")
    else:
        print("No weaknesses found.")
    recommendations = recommend_security_practices(password)
    if recommendations:
        print("Recommendations:")
        for recommendation in recommendations:
            print(f"- {recommendation}")
    else:
        print("No recommendations.")
