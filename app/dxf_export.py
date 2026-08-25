from pathlib import Path
try:
    import ezdxf
except ImportError:
    ezdxf = None

def export_dxf(project, path):
    if ezdxf is None:
        raise RuntimeError('Install ezdxf first')
    doc = ezdxf.new('R2018')
    msp = doc.modelspace()
    w, d = project.plot_width_mm, project.plot_depth_mm
    msp.add_lwpolyline([(0,0),(w,0),(w,d),(0,d),(0,0)])
    x, y = 0, d
    for r in project.rooms:
        rw, rd = r.width_mm, r.depth_mm
        if x+rw > w: x=0; y-=rd
        if y-rd < 0: break
        pts=[(x,y),(x+rw,y),(x+rw,y-rd),(x,y-rd),(x,y)]
        msp.add_lwpolyline(pts)
        msp.add_text(f'{r.name} {rw:.0f}x{rd:.0f}', dxfattribs={'height':100}).set_placement((x+50,y-150))
        x += rw
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    doc.saveas(path)
