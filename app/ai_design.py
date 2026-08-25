def exterior_prompt(project: dict) -> str:
    return f"""Photorealistic modern Indian residential architecture visualization. Plot {project['plot_length_mm']:.0f} x {project['plot_width_mm']:.0f} mm, {project['floors']} floors, {project['facing']}-facing. Clean contemporary façade, realistic construction proportions, Indian materials, daylight, architectural photography, physically plausible structure. Preserve exact CAD dimensions; visualization only."""

def interior_prompt(project: dict) -> str:
    return f"""Photorealistic modern Indian residential interior for {project['name']}. {project['floors']} floors, {project['facing']}-facing. Warm minimal materials, functional furniture, realistic circulation, accurate scale, natural daylight, premium architectural photography. Follow approved room schedule; do not invent structural changes."""

def panorama_360_prompt(project: dict) -> str:
    return f"""360-degree equirectangular architectural visualization of a modern Indian home, {project['plot_length_mm']:.0f} x {project['plot_width_mm']:.0f} mm, {project['floors']} floors, {project['facing']}-facing. Seamless 2:1 panorama, realistic perspective, complete surrounding context, physically plausible materials and lighting. Use CAD geometry as the source of truth."""
