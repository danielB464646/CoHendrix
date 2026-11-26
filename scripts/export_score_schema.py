import json
from pathlib import Path

from cohendrix.schemas.score import Score


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    output = root / "src" / "contracts" / "score.schema.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(Score.model_json_schema(), indent=2) + "\n", encoding="utf-8", newline="\n"
    )


if __name__ == "__main__":
    main()
