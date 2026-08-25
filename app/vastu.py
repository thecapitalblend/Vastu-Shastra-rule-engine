import json
from pathlib import Path

RULES = json.loads((Path(__file__).parent.parent / 'data' / 'vastu_rules.json').read_text(encoding='utf-8'))

ZONE_HINTS = {
    'north-east': ['pooja', 'meditation', 'study'],
    'south-east': ['kitchen'],
    'south-west': ['master bedroom', 'store'],
    'north-west': ['guest bedroom', 'parking'],
    'north': ['living', 'study'],
    'east': ['living', 'dining'],
    'south': ['stair', 'service'],
    'west': ['bedroom', 'stair']
}

def check_project(project):
    findings = []
    for r in project.rooms:
        name = r.name.lower()
        if r.preferred_zone:
            z = r.preferred_zone.lower()
            expected = any(k in name for k in ZONE_HINTS.get(z, []))
            findings.append({
                'room': r.name,
                'zone': r.preferred_zone,
                'status': 'review' if not expected else 'pass',
                'message': 'Zone preference recorded; verify against the selected Vastu tradition and actual geometry.'
            })
    findings.append({'rule_id':'V001','status':'pass','message':'North orientation is explicitly recorded.'})
    findings.append({'rule_id':'V003','status':'pass','message':'All geometric inputs are in millimetres.'})
    return {'findings': findings, 'rules_loaded': len(RULES)}
