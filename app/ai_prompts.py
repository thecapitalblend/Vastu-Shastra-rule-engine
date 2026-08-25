def build_prompts(project):
    base = (f'{project.project_name}, plot {project.plot_width_mm/304.8:.2f} ft × {project.plot_depth_mm/304.8:.2f} ft, '
            f'{project.floors}-storey, {project.style}, true north angle {project.north_angle_deg}°. '
            'Use realistic human scale, structural logic, accurate openings, Indian climate response, and buildable details.')
    return {
      'exterior': base + ' Photorealistic architectural exterior, modern Indian facade, clean proportions, realistic materials, daylight and dusk variants.',
      'interior': base + ' Photorealistic interior design, coordinated furniture, lighting, circulation, storage, material palette, realistic room dimensions.',
      '360': base + ' Equirectangular 2:1 architectural panorama, seamless 360-degree interior/exterior viewpoint, no distorted geometry, physically plausible lighting.'
    }
