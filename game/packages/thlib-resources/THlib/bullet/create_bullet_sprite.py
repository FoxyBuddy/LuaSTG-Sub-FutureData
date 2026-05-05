import json

def generate_bullet_json(image_width, image_height, bullet_configs, texture_name="bullet", texture_path="bullet.png"):
    """
    生成不包含中心点的子弹纹理 JSON
    """
    sprites = []
    current_x = 0  # X轴起始位置

    for config in bullet_configs:
        name_prefix = config["name"]
        w = config["w"]
        h = config["h"]
        count = config["count"]
        
        # 按照从下往上数（左下角开始）的逻辑生成坐标
        for i in range(count):
            # y坐标计算：总高度减去 (当前索引+1)*高度
            # 索引0是第一行（最下面），y = 2048 - 16 = 2032
            y_pos = image_height - (i + 1) * h
            
            sprite_entry = {
                "name": str(name_prefix) + "_" + str(i + 1),
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
# 在这里按顺序添加 29 种子弹的参数
bullet_config_list = [
    {"name": "ball_small", "w": 16, "h": 16, "count": 16},
    {"name": "mildew",     "w": 16, "h": 16, "count": 16},
    {"name": "grain_a",    "w": 32, "h": 16, "count": 16},
    {"name": "grain_b",    "w": 32, "h": 16, "count": 16},
    {"name": "grain_c",    "w": 32, "h": 16, "count": 16},
    {"name": "arrow_small","w": 32, "h": 16, "count": 16},
    {"name": "gun_bullet","w": 32, "h": 24, "count": 16},
    {"name": "slience","w": 64, "h": 24, "count": 16},
    {"name": "kite","w": 32, "h": 24, "count": 16},
    {"name": "arrow_mid","w": 64, "h": 24, "count": 16},
    {"name": "money","w": 32, "h": 32, "count": 16},
    {"name": "square","w": 32, "h": 32, "count": 16},
    {"name": "arrow_big","w": 32, "h": 32, "count": 16},
    {"name": "ball_mid","w": 32, "h": 32, "count": 16},
    {"name": "ball_mid_c","w": 32, "h": 32, "count": 16},
    {"name": "knife","w": 64, "h": 32, "count": 16},
    {"name": "star_small","w": 32, "h": 32, "count": 16},
    {"name": "ellipse","w": 64, "h": 32, "count": 16},
    {"name": "water_drop_1","w": 96, "h": 64, "count": 16},
    {"name": "water_drop_2","w": 96, "h": 64, "count": 16},
    {"name": "water_drop_3","w": 96, "h": 64, "count": 16},
    {"name": "butterfly","w": 64, "h": 64, "count": 16},
    {"name": "ball_big","w": 64, "h": 64, "count": 16},
    {"name": "heart","w": 64, "h": 64, "count": 16},
    {"name": "knife_b","w": 64, "h": 64, "count": 16},
    {"name": "preimg","w": 64, "h": 64, "count": 16},
    {"name": "bubble","w": 64, "h": 64, "count": 16},
    {"name": "music_1","w": 64, "h": 64, "count": 16},
    {"name": "music_2","w": 64, "h": 64, "count": 16},
    {"name": "music_3","w": 64, "h": 64, "count": 16},
    {"name": "star_big","w": 96, "h": 96, "count": 16},
    {"name": "ball_huge","w": 128, "h": 128, "count": 16},
    {"name": "ball_light","w": 128, "h": 128, "count": 16},


    # 你可以继续向下添加，例如：
    # {"name": "next_bullet", "w": 32, "h": 32, "count": 16},
]

# 执行计算 (1856x2048)
json_content = generate_bullet_json(1888, 2048, bullet_config_list)

# 写入文件
with open("bullets_sprites.json", "w", encoding="utf-8") as f:
    json.dump(json_content, f, indent=2, ensure_ascii=False)

print("JSON 脚本生成成功，已去掉中心点字段。")