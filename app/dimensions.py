def mm(feet: float) -> int:
    return round(float(feet) * 304.8)

def feet(mm_value: float) -> float:
    return float(mm_value) / 304.8

def room_area(length_mm: float, width_mm: float) -> float:
    return (float(length_mm) * float(width_mm)) / 1_000_000.0
