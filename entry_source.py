import os
from pathlib import Path

ENTRY_FILENAME = "entry.txt"
OUTPUT_ENV_VAR = "MAKEFUN_OUTPUT_DIR"
DEFAULT_OUTPUT_DIR = "/output"
MAX_WORD_LENGTH = 111
CANDIDATE_WORD = "Expired"
FALLBACK_WORD = "Unknown"


def choose_word() -> str:
    raw_word = CANDIDATE_WORD.strip()
    parts = raw_word.split()
    cleaned = parts[0] if parts else FALLBACK_WORD
    if not cleaned:
        cleaned = FALLBACK_WORD
    if len(cleaned) > MAX_WORD_LENGTH:
        cleaned = cleaned[:MAX_WORD_LENGTH]
    return cleaned


def resolve_output_dir() -> Path:
    raw_dir = os.environ.get(OUTPUT_ENV_VAR, DEFAULT_OUTPUT_DIR)
    output_dir = Path(raw_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


def write_entry(word: str) -> Path:
    output_path = resolve_output_dir() / ENTRY_FILENAME
    output_path.write_text(word, encoding="utf-8")
    return output_path


def main() -> None:
    selected_word = choose_word()
    write_entry(selected_word)


if __name__ == "__main__":
    main()
