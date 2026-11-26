import json
from pathlib import Path

import pytest
from pydantic import ValidationError

from cohendrix.schemas.score import Score

ROOT = Path(__file__).resolve().parents[2]
FIXTURES = ROOT / "tests" / "fixtures" / "contracts"


@pytest.mark.parametrize("filename", ["score-drums.json", "score-crossing-bar.json"])
def test_examples_validate_and_round_trip(filename: str) -> None:
    payload = (FIXTURES / filename).read_text(encoding="utf-8")
    score = Score.model_validate_json(payload)
    assert json.loads(score.model_dump_json()) == json.loads(payload)


def test_committed_json_schema_matches_model() -> None:
    schema = ROOT / "src" / "contracts" / "score.schema.json"
    assert json.loads(schema.read_text(encoding="utf-8")) == Score.model_json_schema()


def test_score_rejects_duplicate_note_ids_and_unknown_tracks() -> None:
    data = json.loads((FIXTURES / "score-drums.json").read_text(encoding="utf-8"))
    data["notes"][0]["id"] = data["notes"][1]["id"]
    with pytest.raises(ValidationError, match="Note IDs must be unique"):
        Score.model_validate(data)
    data["notes"][0]["id"] = "new-id"
    data["notes"][0]["track_id"] = "absent"
    with pytest.raises(ValidationError, match="nonexistent track"):
        Score.model_validate(data)
