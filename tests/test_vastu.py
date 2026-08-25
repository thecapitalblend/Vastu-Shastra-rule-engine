import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))
from vastu_rules import validate_room

def test_se_kitchen_pass():
    assert validate_room("South-East", "Kitchen")["status"] == "PASS"

def test_ne_toilet_review():
    assert validate_room("North-East", "Toilet")["status"] == "REVIEW"
