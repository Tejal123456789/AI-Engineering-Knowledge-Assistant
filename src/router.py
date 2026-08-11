def get_task(user_input):
    user_input = user_input.lower()

    if "summarize" in user_input or "summary" in user_input:
        return "summarize"

    if "compare" in user_input:
        return "compare"

    if "notes" in user_input or "note" in user_input:
        return "notes"

    return "answer"