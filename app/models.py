from pydantic import BaseModel, Field
from typing import List, Literal, Optional

class Room(BaseModel):
    name: str
    width_mm: float = Field(gt=0)
    depth_mm: float = Field(gt=0)
    preferred_zone: Optional[str] = None

class Project(BaseModel):
    project_name: str = "Vastu Home"
    plot_width_mm: float = Field(gt=0)
    plot_depth_mm: float = Field(gt=0)
    north_angle_deg: float = 0.0
    floors: int = Field(default=2, ge=1, le=10)
    floor_height_mm: float = 3150
    wall_thickness_mm: float = 230
    rooms: List[Room] = []
    style: str = "Modern Indian"
