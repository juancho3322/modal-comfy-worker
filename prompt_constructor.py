def construct_prompt(input_data):
    prompt = input_data.get("prompt", "A beautiful cinematic scene")
    
    # Aquí modificamos el workflow con el nuevo prompt
    workflow = {
        "positive_prompt": prompt,   # Cambia según el nombre exacto en tu workflow
        "negative_prompt": input_data.get("negative", "blurry, bad quality"),
        "seed": input_data.get("seed", 42),
        "steps": input_data.get("steps", 20),
        "width": input_data.get("width", 704),
        "height": input_data.get("height", 480),
        "frames": input_data.get("frames", 81),
        "fps": input_data.get("fps", 24),
    }
    
    return workflow
