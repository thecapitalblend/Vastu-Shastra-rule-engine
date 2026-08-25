from pathlib import Path
from .models import Project, Room
from .exporters import export_svg, export_png, export_pdf
from .dxf_export import export_dxf
from .obj_export import export_obj

p=Project(project_name='Sample_Vastu_Home',plot_width_mm=12192,plot_depth_mm=4572,floors=2,rooms=[
 Room(name='Living',width_mm=3600,depth_mm=4200,preferred_zone='north'),
 Room(name='Kitchen',width_mm=3000,depth_mm=3000,preferred_zone='south-east'),
 Room(name='Master Bedroom',width_mm=3600,depth_mm=4200,preferred_zone='south-west')])
out=Path(__file__).parent.parent/'generated'; out.mkdir(exist_ok=True)
export_svg(p,out/'sample.svg'); export_png(p,out/'sample.png'); export_pdf(p,out/'sample.pdf'); export_dxf(p,out/'sample.dxf'); export_obj(p,out/'sample.obj')
print('Generated sample outputs in generated/')
