from app.models import Project
from app.vastu import check_project

def test_validate():
    p=Project(plot_width_mm=9000,plot_depth_mm=12000)
    r=check_project(p)
    assert r['rules_loaded'] >= 1
