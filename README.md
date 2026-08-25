# Vastu-Shastra-rule-engine — Error-Free Streamlit Starter

A clean, GitHub-ready architecture design starter focused on Vastu-aware residential planning, real dimensions, DXF/PDF export and AI visualization prompts.

## Run on Streamlit
Set the main file to:

`app/main.py`

The app uses **non-relative imports** and explicitly adds `app/` to `sys.path`, preventing the error:

`ImportError: attempted relative import with no known parent package`

## Features
- Plot dimensions in feet, stored internally in millimetres
- Room schedule with area calculation
- Vastu validation: PASS / REVIEW
- DXF plot + room rectangle export
- PDF room schedule export
- Exterior / interior / 360° AI prompts
- Structured Vastu/reference data
- Automated tests

## Local test

```bash
python -m pytest
```

## Important professional boundary
This is a design assistant, not a substitute for a licensed architect/structural engineer. Vastu recommendations never override structural safety, NBC/local bylaws, fire safety, accessibility, soil/foundation engineering or other statutory requirements.
