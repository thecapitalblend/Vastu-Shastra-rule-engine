import json
import sys
from pathlib import Path

# Streamlit executes this file as a script. The app directory is added explicitly
# so sibling modules work without fragile relative imports.
APP_DIR = Path(__file__).resolve().parent
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))
ROOT_DIR = APP_DIR.parent

import streamlit as st

from models import Project, Room
from dimensions import room_area
from vastu_rules import RULES, validate_room
from ai_design import exterior_prompt, interior_prompt, panorama_360_prompt
from export import make_dxf, make_pdf

st.set_page_config(page_title="Vastu Architect AI", page_icon="🏠", layout="wide")

st.title("🏠 Vastu Architect AI")
st.caption("Vastu-aware planning • real dimensions • CAD/PDF export • AI visualization prompts")

with st.sidebar:
    st.header("Project")
    name = st.text_input("Project name", "Modern Vastu Residence")
    length_ft = st.number_input("Plot length (ft)", min_value=5.0, value=50.0, step=0.5)
    width_ft = st.number_input("Plot width (ft)", min_value=5.0, value=40.0, step=0.5)
    floors = st.number_input("Floors", min_value=1, max_value=10, value=2, step=1)
    facing = st.selectbox("Facing", ["North", "South", "East", "West", "North-East", "North-West", "South-East", "South-West"])

plot_l = length_ft * 304.8
plot_w = width_ft * 304.8
project = Project(name=name, plot_length_mm=plot_l, plot_width_mm=plot_w, floors=int(floors), facing=facing)

st.subheader("1. Room schedule")
if "rooms" not in st.session_state:
    st.session_state.rooms = []

c1, c2, c3, c4, c5 = st.columns([1.5, 1.2, 1, 1, 0.7])
with c1: room_name = st.text_input("Room", "Living Room", key="room_name")
with c2: zone = st.selectbox("Vastu zone", ["North-East", "North", "North-West", "West", "Centre", "East", "South-East", "South", "South-West"], key="zone")
with c3: rl = st.number_input("Length mm", min_value=500.0, value=4000.0, step=100.0, key="rl")
with c4: rw = st.number_input("Width mm", min_value=500.0, value=3500.0, step=100.0, key="rw")
with c5:
    if st.button("Add"):
        st.session_state.rooms.append({"name": room_name, "zone": zone, "length_mm": rl, "width_mm": rw, "area_sqm": room_area(rl, rw), "x_mm": 0, "y_mm": 0})

if st.session_state.rooms:
    st.dataframe(st.session_state.rooms, use_container_width=True, hide_index=True)
else:
    st.info("Add rooms to create the schedule.")

st.subheader("2. Vastu validation")
if st.session_state.rooms:
    for r in st.session_state.rooms:
        result = validate_room(r["zone"], r["name"])
        label = f"{r['name']} — {r['zone']}"
        if result["status"] == "PASS":
            st.success(f"{label}: {result['reason']}")
        else:
            st.warning(f"{label}: {result['reason']}")

st.subheader("3. Exports")
rows = st.session_state.rooms
pdf_bytes = make_pdf(name, rows)
dxf_bytes = make_dxf(plot_l, plot_w, rows)
e1, e2 = st.columns(2)
with e1:
    st.download_button("📄 Download PDF report", pdf_bytes, file_name="vastu_design_report.pdf", mime="application/pdf")
with e2:
    st.download_button("📐 Download DXF plan", dxf_bytes, file_name="vastu_plan.dxf", mime="application/dxf")

st.subheader("4. AI 3D / Interior / Exterior / 360")
payload = {"name": name, "plot_length_mm": plot_l, "plot_width_mm": plot_w, "floors": int(floors), "facing": facing}
for title, prompt in [("Exterior", exterior_prompt(payload)), ("Interior", interior_prompt(payload)), ("360°", panorama_360_prompt(payload))]:
    with st.expander(f"{title} AI prompt"):
        st.code(prompt, language="text")

with st.expander("Reference rules"):
    st.json([r.__dict__ for r in RULES])
    st.caption("Classical-source verification is required before presenting a rule as an exact verse-level prescription. Structural, fire, accessibility and local code requirements remain mandatory.")
