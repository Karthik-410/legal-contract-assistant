risk_terms = {
    "High": ["penalty", "terminate immediately", "lawsuit", "liable"],
    "Medium": ["indemnify", "arbitration", "auto renew"],
    "Low": ["notice period", "renewal option"]
}

def detect_risks(text):
    detected = []

    for level, words in risk_terms.items():
        for w in words:
            if w in text.lower():
                detected.append((w, level))

    return detected

def contract_risk_score(risks):
    score = 0

    for _, level in risks:
        if level == "High":
            score += 3
        elif level == "Medium":
            score += 2
        else:
            score += 1

    if score >= 6:
        return "High Risk"
    elif score >= 3:
        return "Medium Risk"
    else:
        return "Low Risk"
