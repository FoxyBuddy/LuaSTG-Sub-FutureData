import json
import os
from PIL import Image

def generate_bullet_json(bullet_configs, texture_name="bullet", texture_path="bullet.png"):
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
                "type": str(name_prefix),
                "texture": texture_name,
                "rect": {
                    "x": current_x,
                    "y": y_pos,
                    "width": w,
                    "height": h
                }
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
    {"name": "money",          "w": 16, "h": 16, "count": 3},#1
    {"name": "ball_small",     "w": 16, "h": 16, "count": 16},#2
    {"name": "mildew",         "w": 16, "h": 16, "count": 16},#3
    {"name": "grain_small",    "w": 16, "h": 16, "count": 16},#4
    {"name": "star_small",     "w": 16, "h": 16, "count": 16},#5
    {"name": "grain_c",        "w": 16, "h": 16, "count": 16},#6
    {"name": "gun_bullet",     "w": 16, "h": 16, "count": 16},#7
    {"name": "square",         "w": 16, "h": 16, "count": 16},#8
    {"name": "grain_b",        "w": 16, "h": 16, "count": 16},#9
    {"name": "arrow_small",    "w": 16, "h": 16, "count": 16},#10
    {"name": "grain_a",        "w": 16, "h": 16, "count": 16},#11
    {"name": "ball_mid",       "w": 16, "h": 16, "count": 16},#12
    {"name": "ball_mid_c",     "w": 16, "h": 16, "count": 16},#13
    {"name": "arrow_big",      "w": 16, "h": 16, "count": 16},#14
    {"name": "laser",          "w": 16, "h": 16, "count": 16},#15
    {"name": "kite",           "w": 16, "h": 16, "count": 16},#16

    {"name": "preimg",         "w": 32, "h": 32, "count": 8},#17
    {"name": "ellipse",        "w": 32, "h": 32, "count": 8},#18
    {"name": "knife_a",        "w": 32, "h": 32, "count": 8},#19
    {"name": "butterfly",      "w": 32, "h": 32, "count": 8},#20
    {"name": "ball_big",       "w": 32, "h": 32, "count": 8},#21
    {"name": "star_big",       "w": 32, "h": 32, "count": 8},#22
    {"name": "arrow_mid",      "w": 32, "h": 32, "count": 8},#23
    {"name": "heart",          "w": 32, "h": 32, "count": 8},#24
    {"name": "tear",           "w": 32, "h": 32, "count": 8},#25
    {"name": "stone",          "w": 32, "h": 32, "count": 8},#26
    {"name": "silence",        "w": 32, "h": 32, "count": 8},#27
    {"name": "orb_small",      "w": 32, "h": 32, "count": 8},#28

    {"name": "music",          "w": 96, "h": 32, "count": 4},
    {"name": "fire_new",       "w": 128, "h": 32, "count": 4},
    {"name": "fire_old",       "w": 128, "h": 32, "count": 2},

    {"name": "ball_huge",      "w": 64, "h": 64, "count": 4},
    {"name": "orb_big",        "w": 64, "h": 64, "count": 4},
    {"name": "ball_light",     "w": 64, "h": 64, "count": 8},
]

# --- 执行 ---
# 确保你的图片叫 bullet.png 
target_image = "bullet_v2.png"

try:
    # 删除了原来的 1184, 512 参数，现在会自动获取
    json_content = generate_bullet_json(bullet_config_list, texture_path=target_image)

    # 写入文件
    with open("bullet_sprites_v2.json", "w", encoding="utf-8") as f:
        json.dump(json_content, f, indent=2, ensure_ascii=False)

    print("JSON 脚本生成成功，已按从上往下（1->N）顺序排列。")
except Exception as e:
    print(f"发生错误: {e}")