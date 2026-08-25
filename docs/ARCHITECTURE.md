# Software Architecture

Streamlit is the UI entry point: `app/main.py`.

Sibling modules are imported as plain modules because Streamlit executes `main.py` directly. The app explicitly adds `app/` to `sys.path`; this avoids the previous `attempted relative import with no known parent package` error.

## Modules
- `models.py`: project/room data models
- `vastu_rules.py`: rule engine
- `dimensions.py`: unit and area calculations
- `export.py`: PDF and DXF generation
- `ai_design.py`: exterior/interior/360 prompt generation
