from pathlib import Path
from reportlab.pdfgen import canvas
from PIL import Image, ImageDraw


def export_svg(project, path):
    w, d = project.plot_width_mm, project.plot_depth_mm
    scale = 0.2
    W, H = int(w*scale)+100, int(d*scale)+100
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">', '<rect width="100%" height="100%" fill="white"/>']
    svg.append(f'<rect x="50" y="50" width="{w*scale}" height="{d*scale}" fill="none" stroke="black" stroke-width="3"/>')
    svg.append(f'<text x="55" y="35" font-size="16">N ↑ | {project.project_name}</text>')
    y = 65
    for r in project.rooms:
        rw, rd = r.width_mm*scale, r.depth_mm*scale
        if 50+rw > W-10: rw = W-60
        if y+rd > H-10: rd = max(30, H-y-10)
        svg.append(f'<rect x="55" y="{y}" width="{rw}" height="{rd}" fill="none" stroke="#555"/>')
        svg.append(f'<text x="60" y="{y+16}" font-size="11">{r.name} {r.width_mm:.0f}×{r.depth_mm:.0f} mm</text>')
        y += min(rd+10, 80)
    svg.append('</svg>')
    Path(path).write_text('\n'.join(svg), encoding='utf-8')


def export_png(project, path):
    img = Image.new('RGB', (1200, 900), 'white')
    dr = ImageDraw.Draw(img)
    margin = 80
    sx = (1200-2*margin)/project.plot_width_mm
    sy = (900-2*margin)/project.plot_depth_mm
    s = min(sx, sy)
    pw, ph = project.plot_width_mm*s, project.plot_depth_mm*s
    dr.rectangle((margin, margin, margin+pw, margin+ph), outline='black', width=4)
    dr.text((margin, 30), f'N ↑  {project.project_name}', fill='black')
    y = margin+20
    for r in project.rooms:
        rw, rh = r.width_mm*s, r.depth_mm*s
        if rw > pw-20: rw = pw-20
        if y+rh > margin+ph-10: rh = 40
        dr.rectangle((margin+10, y, margin+10+rw, y+rh), outline='gray', width=2)
        dr.text((margin+15, y+5), f'{r.name} {r.width_mm:.0f}×{r.depth_mm:.0f}', fill='black')
        y += min(rh+15, 100)
    img.save(path)


def export_pdf(project, path):
    c = canvas.Canvas(str(path), pagesize=(595,842))
    c.setFont('Helvetica-Bold', 16)
    c.drawString(40, 800, project.project_name)
    c.setFont('Helvetica', 10)
    c.drawString(40, 780, f'Plot: {project.plot_width_mm:.0f} × {project.plot_depth_mm:.0f} mm | Floors: {project.floors} | Style: {project.style}')
    y=750
    c.drawString(40,y,'Rooms / program')
    y-=20
    for r in project.rooms:
        c.drawString(55,y,f'{r.name}: {r.width_mm:.0f} × {r.depth_mm:.0f} mm | zone={r.preferred_zone or "not specified"}')
        y-=16
    c.showPage(); c.save()
