import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))
from dimensions import mm, feet, room_area

def test_conversion():
    assert mm(10) == 3048
    assert round(feet(3048), 2) == 10.00

def test_area():
    assert room_area(3000, 4000) == 12.0
