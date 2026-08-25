# Vastu Architect AI — Senior Architecture Design Engine

A starter GitHub-ready project for **Vastu-aware residential architecture** with real metric dimensions, 2D DXF export, simple 3D OBJ export, PDF/image export, interior/exterior concept prompts, and AI integration hooks.

## Scope
- Plot and building inputs in mm/metres/feet conversion.
- Vastu zoning engine with transparent rule IDs and source references.
- Rule conflicts are reported instead of silently forcing a layout.
- 2D floor-plan DXF export compatible with AutoCAD/DXF viewers.
- Basic 3D massing OBJ export for Blender/AutoCAD-compatible workflows.
- SVG/PNG preview and PDF report generation.
- AI prompt builder for modern exterior, interior and 360° panorama concepts.
- API-ready architecture for connecting image-generation/LLM providers.

## Important Vastu reference policy
This project does **not** claim that every popular internet Vastu rule is an ancient-script rule. Rules are tagged by source and confidence. Classical references include Mānasāra and Mayamata; modern practitioner rules should be separated from classical text-derived rules.

Primary references included in `docs/vastu_references.md`:
- Prasanna Kumar Acharya, *Architecture of Mānasāra: Text with English Translation and Notes*.
- Bruno Dagens, *Mayamata: An Indian Treatise on Housing Architecture and Iconography*.
- Government Sanskrit archive material on Viśvakarma Vāstu Śāstram.

## Run
```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Open `http://127.0.0.1:8000`.

## Generate sample files
```bash
python app/generate_sample.py
```
Outputs go to `generated/`.

## GitHub
Create a repository, copy this folder into it, then:
```bash
git init
git add .
git commit -m "Initial Vastu Architect AI engine"
git branch -M main
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin main
```

## Safety / professional use
This is a design-assistance engine, not a substitute for a licensed architect/structural engineer, local building bye-laws, NBC requirements, fire rules, seismic design, soil investigation, or municipal approval.
