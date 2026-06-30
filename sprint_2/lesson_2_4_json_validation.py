import json

REQUIRED_TOP_KEYS = ["detected_sentiment", "theme", "layout_style"]
REQUIRED_THEME_KEYS = [
    "background_color", "primary_text", "accent_color",
    "font_family_heading", "font_family_body"
]


def validate_designer_json(text: str) -> dict:
    missing = []

    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON: {e}")

    if not isinstance(data, dict):
        raise ValueError("Parsed JSON is not a dictionary")

    for key in REQUIRED_TOP_KEYS:
        if key not in data:
            missing.append(f"top-level key '{key}'")

    if "theme" in data and isinstance(data["theme"], dict):
        for key in REQUIRED_THEME_KEYS:
            if key not in data["theme"]:
                missing.append(f"theme key '{key}'")

    if missing:
        raise ValueError("Missing required keys: " + ", ".join(missing))

    return data
