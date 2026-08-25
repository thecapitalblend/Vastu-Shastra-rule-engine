from pathlib import Path

def export_obj(project, path):
    # Simple massing model: plot/building envelope extruded by floor count.
    w,d,h = project.plot_width_mm, project.plot_depth_mm, project.floor_height_mm*project.floors
    verts=[(0,0,0),(w,0,0),(w,d,0),(0,d,0),(0,0,h),(w,0,h),(w,d,h),(0,d,h)]
    faces=[(1,2,3,4),(5,8,7,6),(1,5,6,2),(2,6,7,3),(3,7,8,4),(4,8,5,1)]
    lines=['# Vastu Architect AI basic massing OBJ']
    lines += [f'v {x} {y} {z}' for x,y,z in verts]
    lines += ['f '+' '.join(map(str,f)) for f in faces]
    Path(path).write_text('\n'.join(lines)+'\n', encoding='utf-8')
