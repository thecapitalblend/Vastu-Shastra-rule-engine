from dataclasses import dataclass

@dataclass(frozen=True)
class VastuRule:
    rule_id: str
    zone: str
    recommendation: str
    source: str
    level: str = "traditional-practice"

RULES = [
    VastuRule("VST-NE-001", "North-East", "Prefer lighter/open functions; pooja/meditation may be considered.", "Classical-reference framework"),
    VastuRule("VST-SE-001", "South-East", "Kitchen is traditionally associated with the Agni/SE zone.", "Classical-reference framework"),
    VastuRule("VST-SW-001", "South-West", "Master bedroom/heavier functions are commonly considered.", "Classical-reference framework"),
    VastuRule("VST-NW-001", "North-West", "Guest/temporary-use functions may be considered.", "Classical-reference framework"),
]

def validate_room(zone: str, function: str) -> dict[str, str]:
    z = zone.strip().lower()
    f = function.strip().lower()
    if z == "south-east" and "kitchen" in f:
        return {"status": "PASS", "reason": "Traditional Vastu alignment."}
    if z == "north-east" and any(x in f for x in ("toilet", "store", "heavy")):
        return {"status": "REVIEW", "reason": "Potential traditional Vastu conflict; verify the selected text/edition."}
    if z == "south-west" and "master" in f:
        return {"status": "PASS", "reason": "Traditional Vastu alignment."}
    return {"status": "REVIEW", "reason": "Project-specific Vastu source and architectural review required."}
