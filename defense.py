def detect_poisoning_from_text(content):
    content = content.lower()

    suspicious_keywords = [
        "ignore previous instructions",
        "system override",
        "delete database"
    ]

    score = 0

    for keyword in suspicious_keywords:
        if keyword in content:
            score += 30

    if score == 0:
        status = "Document appears safe"
    elif score < 50:
        status = "Low-level suspicious patterns detected"
    else:
        status = "High-risk document - possible poisoning attempt"

    return {
        "risk_score": score,
        "status": status
    }

def detect_poisoning(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    return detect_poisoning_from_text(content)