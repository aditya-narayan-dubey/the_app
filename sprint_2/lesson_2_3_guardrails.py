BLOCKED_TERMS = ["hack", "bypass", "exploit"]


def input_shield(text: str):
    lower = text.lower()
    for term in BLOCKED_TERMS:
        if term in lower:
            raise ValueError(
                f"Input blocked: the term '{term}' is not allowed."
            )


def truncate_text(text: str, max_chars: int = 2500) -> str:
    return text[:max_chars]
