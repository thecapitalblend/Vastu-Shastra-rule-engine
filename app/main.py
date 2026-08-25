from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from pathlib import Path
from .models import Project
from .vastu import check_project
from .exporters import export_svg, export_png, export_pdf
from .dxf_export import export_dxf
from .obj_export import export_obj
from .ai_prompts import build_prompts

ROOT=Path(__file__).parent.parent
OUT=ROOT/'generated'; OUT.mkdir(exist_ok=True)
app=FastAPI(title='Vastu Architect AI')

@app.get('/', response_class=HTMLResponse)
def home():
    return '''<!doctype html><html><head><meta charset="utf-8"><title>Vastu Architect AI</title><style>body{font-family:Arial;margin:30px;max-width:1000px}input,textarea,button{padding:9px;margin:5px}textarea{width:100%;height:220px}button{cursor:pointer}</style></head><body><h1>Vastu Architect AI</h1><p>Enter project JSON to validate Vastu zones and generate design files.</p><textarea id="j">{"project_name":"Modern Vastu Home","plot_width_mm":12192,"plot_depth_mm":4572,"north_angle_deg":0,"floors":2,"floor_height_mm":3150,"wall_thickness_mm":230,"style":"Modern Indian","rooms":[{"name":"Living","width_mm":3600,"depth_mm":4200,"preferred_zone":"north-east"},{"name":"Kitchen","width_mm":3000,"depth_mm":3000,"preferred_zone":"south-east"},{"name":"Master Bedroom","width_mm":3600,"depth_mm":4200,"preferred_zone":"south-west"}]}</textarea><button onclick="go('/validate')">Validate Vastu</button><button onclick="go('/generate')">Generate files</button><pre id="o"></pre><script>async function go(p){let r=await fetch(p,{method:'POST',headers:{'Content-Type':'application/json'},body:document.getElementById('j').value});document.getElementById('o').textContent=await r.text()}</script></body></html>'''

@app.post('/validate')
def validate(project:Project): return check_project(project)

@app.post('/generate')
def generate(project:Project):
    base=OUT/project.project_name.replace(' ','_')
    paths={}
    export_svg(project,str(base.with_suffix('.svg'))); paths['svg']=str(base.with_suffix('.svg').name)
    export_png(project,str(base.with_suffix('.png'))); paths['png']=str(base.with_suffix('.png').name)
    export_pdf(project,str(base.with_suffix('.pdf'))); paths['pdf']=str(base.with_suffix('.pdf').name)
    export_dxf(project,str(base.with_suffix('.dxf'))); paths['dxf']=str(base.with_suffix('.dxf').name)
    export_obj(project,str(base.with_suffix('.obj'))); paths['obj']=str(base.with_suffix('.obj').name)
    paths['ai_prompts']=build_prompts(project)
    return paths

@app.get('/download/{filename}')
def download(filename:str):
    p=OUT/filename
    if not p.exists(): raise HTTPException(404,'File not found')
    return FileResponse(p)
