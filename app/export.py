from pathlib import Path
from io import BytesIO


def make_pdf(project_name: str, rows: list[dict]) -> bytes:
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas
    from reportlab.lib.units import mm
    buf = BytesIO()
    c = canvas.Canvas(buf, pagesize=A4)
    width, height = A4
    y = height - 22 * mm
    c.setFont("Helvetica-Bold", 16)
    c.drawString(18 * mm, y, project_name[:80])
    y -= 10 * mm
    c.setFont("Helvetica", 9)
    c.drawString(18 * mm, y, "Vastu Architect AI - preliminary design report")
    y -= 12 * mm
    c.setFont("Helvetica-Bold", 9)
    c.drawString(18 * mm, y, "Room")
    c.drawString(65 * mm, y, "Zone")
    c.drawString(100 * mm, y, "L x W (mm)")
    c.drawString(145 * mm, y, "Area (m²)")
    y -= 6 * mm
    c.setFont("Helvetica", 9)
    for row in rows:
        if y < 18 * mm:
            c.showPage(); y = height - 20 * mm; c.setFont("Helvetica", 9)
        c.drawString(18 * mm, y, str(row.get("name", ""))[:24])
        c.drawString(65 * mm, y, str(row.get("zone", ""))[:18])
        c.drawString(100 * mm, y, f'{row.get("length_mm", 0):.0f} x {row.get("width_mm", 0):.0f}')
        c.drawString(145 * mm, y, f'{row.get("area_sqm", 0):.2f}')
        y -= 5 * mm
    c.save()
    return buf.getvalue()


def make_dxf(plot_length_mm: float, plot_width_mm: float, rooms: list[dict]) -> bytes:
    import ezdxf
    from io import StringIO
    doc = ezdxf.new("R2018")
    msp = doc.modelspace()
    L, W = float(plot_length_mm), float(plot_width_mm)
    msp.add_lwpolyline([(0, 0), (L, 0), (L, W), (0, W), (0, 0)])
    for r in rooms:
        x = float(r.get("x_mm", 0)); y = float(r.get("y_mm", 0))
        l = float(r.get("length_mm", 0)); w = float(r.get("width_mm", 0))
        if l > 0 and w > 0 and x + l <= L and y + w <= W:
            msp.add_lwpolyline([(x,y),(x+l,y),(x+l,y+w),(x,y+w),(x,y)])
    text = StringIO()
    doc.write(text)
    return text.getvalue().encode("utf-8")
