import json
import os
from PIL import Image

def generate_bullet_json(bullet_configs, texture_name="bullet_effect", texture_path="bullet.png"):
    """
    使用 Pillow 自动获取尺寸，并生成编号从上往下递增的 JSON
    """
    # 1. 使用 Pillow 自动获取宽高
    if not os.path.exists(texture_path):
        raise FileNotFoundError(f"找不到文件: {texture_path}，请确保图片与脚本在同一目录。")
    
    with Image.open(texture_path) as img:
        image_width, image_height = img.size
    
    print(f"成功读取图片: {texture_path} | 分辨率: {image_width}x{image_height}")

    sprites = []
    current_x = 0  # X轴起始位置

    for config in bullet_configs:
        name_prefix = config["name"]
        w = config["w"]
        h = config["h"]
        count = config["count"]
        
        # 计算这组子弹在大图中的起始 Y 坐标
        # 逻辑：图片底部对齐。由于编号从上往下，i=0 (编号1) 应该是最靠上的位置。
        group_top_y = image_height - (count * h)
        
        for i in range(count):
            # i=0 时，y_pos 为 group_top_y (最顶端)
            # i 增加时，y_pos 增加 (向下移动)
            y_pos = group_top_y + (i * h)
            
            sprite_entry = {
                "name": f"{name_prefix}_{i + 1}",
                "texture": texture_name,
                "rect": {
                    "x": current_x,
                    "y": y_pos,
                    "width": w,
                    "height": h
                },
                "scale":0.5
            }
            sprites.append(sprite_entry)
        
        # 处理完一种子弹，x轴向右偏移该子弹的宽度
        current_x += w

    # 封装最终格式
    output_data = {
        "textures": [
            {
                "name": texture_name,
                "path": texture_path
            }
        ],
        "sprites": sprites
    }

    return output_data

# --- 配置区域 ---
bullet_config_list = [
    {"name": "fog_img",     "w": 64, "h": 64, "count": 16},#1
    {"name": "del_img",     "w": 64, "h": 64, "count": 16},#2
]


target_image = "bullet_effect.png"

try:
    json_content = generate_bullet_json(bullet_config_list, texture_path=target_image)

    # 写入文件
    with open("bullet_effect_sprites.json", "w", encoding="utf-8") as f:
        json.dump(json_content, f, indent=2, ensure_ascii=False)

    print("JSON生成成功")
except Exception as e:
    print(f"发生错误: {e}")