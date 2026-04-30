import json
from PIL import Image
import os

def crop_and_combine_bullets(json_path, image_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Open the atlas image
    try:
        atlas_img = Image.open(image_path).convert("RGBA")
    except FileNotFoundError:
        print(f"Error: {image_path} not found.")
        return

    sprites = data.get('sprites', [])
    
    # Dictionary to group sprites by base name (e.g., 'arrow_big', 'music')
    groups = {}
    
    for sprite in sprites:
        name = sprite['name']
        # Extract base name and number
        # Assuming names are like 'arrow_big1', 'music13'
        base_name = ""
        num_str = ""
        for i in range(len(name) - 1, -1, -1):
            if name[i].isdigit():
                num_str = name[i] + num_str
            else:
                base_name = name[:i+1]
                break
        
        if not num_str:
            continue
            
        num = int(num_str)
        if num < 1 or num > 16:
            continue
            
        if base_name not in groups:
            groups[base_name] = {}
        groups[base_name][num] = sprite

    # Process each group
    for base_name, members in groups.items():
        # Only process if we have a sequence (some might not have all 1-16, but we'll try)
        if not members:
            continue
            
        # Determine cell size based on the first available sprite
        first_sprite = list(members.values())[0]
        w = first_sprite['rect']['width']
        h = first_sprite['rect']['height']
        
        # Create a new image: 1 column, 16 rows
        new_img = Image.new("RGBA", (w, h * 16), (0, 0, 0, 0))
        
        found_any = False
        for i in range(1, 17):
            if i in members:
                found_any = True
                s = members[i]
                rect = s['rect']
                box = (rect['x'], rect['y'], rect['x'] + rect['width'], rect['y'] + rect['height'])
                crop = atlas_img.crop(box)
                # Paste at (0, (i-1)*h)
                new_img.paste(crop, (0, (i-1) * h))
        
        if found_any:
            output_path = os.path.join(output_folder, f"{base_name.strip('_')}.png")
            new_img.save(output_path)
            print(f"Saved: {output_path}")

if __name__ == "__main__":
    crop_and_combine_bullets('bullet_atlas.json', 'bullet_atlas.png', 'output_bullets')