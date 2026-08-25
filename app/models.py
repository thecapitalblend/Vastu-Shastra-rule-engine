from dataclasses import dataclass, field
from typing import Any

@dataclass
class Room:
    name: str
    zone: str
    length_mm: float
    width_mm: float

    @property
    def area_sqm(self) -> float:
        return (self.length_mm * self.width_mm) / 1_000_000

@dataclass
class Project:
    name: str = "Vastu Home Project"
    plot_length_mm: float = 15240.0
    plot_width_mm: float = 12192.0
    floors: int = 2
    facing: str = "North"
    rooms: list[Room] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
