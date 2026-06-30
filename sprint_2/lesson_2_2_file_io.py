import os


OUTPUT_DIR = os.path.abspath("output")


def write_file(file_path: str, content: str):
    resolved = os.path.abspath(file_path)

    if not resolved.startswith(OUTPUT_DIR + os.sep) and resolved != OUTPUT_DIR:
        raise ValueError(
            f"Security violation: writing to '{resolved}' is not allowed. "
            f"Files must be inside '{OUTPUT_DIR}'."
        )

    os.makedirs(os.path.dirname(resolved), exist_ok=True)

    with open(resolved, "w", encoding="utf-8") as f:
        f.write(content)
