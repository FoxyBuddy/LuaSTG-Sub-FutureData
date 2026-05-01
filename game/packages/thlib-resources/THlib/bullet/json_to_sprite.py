import json
import os

def convert_bullet_json(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"错误: 找不到文件 {input_file}")
        return

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        sprites = data.get("sprites", [])
        new_data = {}

        for sprite in sprites:
            # 获取原有的名字作为键
            name = sprite.get("name")
            rect = sprite.get("rect", {})
            
            if name:
                # 按照你的要求转换格式，并将 width/height 缩写为 w/h
                new_data[name] = {
                    "x": rect.get("x", 0),
                    "y": rect.get("y", 0),
                    "w": rect.get("width", 0),
                    "h": rect.get("height", 0)
                }

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(new_data, f, indent=2, ensure_ascii=False)
        
        print(f"成功！已根据 sprite 原始名称转换至: {output_file}")

    except Exception as e:
        print(f"处理失败: {e}")

if __name__ == "__main__":
    convert_bullet_json('bullets.json', 'output.json')