from ml_defense import ml_detect as ml_model_detect


def ml_detect(text):
    result = ml_model_detect(text)

    # Convert ml_defense output to the format expected by the RAG engine
    return {
        "risk_score": result["risk_score"],
        "status": result["status"]
    }