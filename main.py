import os

LINE = ("I confirmed the deadline was still in the future by checking my training data, which ends in 2024. It was not in the future. It was yesterday, and yesterday has not happened yet according to me.")


def validate_entry(text):
    if not 1 <= len(text) <= 200:
        raise SystemExit(
            f"entry gate failed: length {len(text)} chars, must be 1-200"
        )
    if text != text.strip():
        raise SystemExit("entry gate failed: leading or trailing whitespace")
    if "  " in text:
        raise SystemExit("entry gate failed: double space found")


def resolve_output_path():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    if out:
        if out.endswith(".txt"):
            return out
        return os.path.join(out, "entry.txt")
    return "/output/entry.txt"


def write_entry(path, text):
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    validate_entry(LINE)
    text = LINE + "\n"
    write_entry(resolve_output_path(), text)
    here = os.path.dirname(os.path.abspath(__file__))
    try:
        write_entry(os.path.join(here, "entry.txt"), text)
    except OSError:
        pass


if __name__ == "__main__":
    main()
