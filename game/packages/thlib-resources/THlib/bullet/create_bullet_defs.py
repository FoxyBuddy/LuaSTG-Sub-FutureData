import json

class BulletConfigGenerator:
    def __init__(self):
        self.data = {"defs": {}}

    def add_bullet(self, name, type="static", collision=None, offset=None, 
                   scale_x=1.0, scale_y=1.0, interval=4, colors=None):
        """
        添加一种子弹定义
        :param name: 子弹在 JSON 中的键名
        :param type: "static" 或 "ani"
        :param collision: 碰撞字典 {"a": float, "b": float, "is_rect": bool}
        :param offset: 偏移字典 {"x": float, "y": float}
        :param scale_x: 横向缩放 (默认 1.0)
        :param scale_y: 纵向缩放 (默认 1.0)
        :param interval: 动画间隔帧数 (仅在 type="ani" 时出现在 JSON 中)
        :param colors: 颜色映射数据
        """
        bullet_def = {
            "type": type
        }
        
        # 仅针对动画子弹添加间隔参数
        if type == "ani":
            bullet_def["interval"] = interval

        # 填充碰撞、偏移与缩放
        bullet_def["collision"] = collision or {"a": 4, "b": 4, "is_rect": False}
        bullet_def["offset"] = offset or {"x": 0, "y": 0}
        bullet_def["scale_x"] = scale_x
        bullet_def["scale_y"] = scale_y
        
        # 颜色映射
        bullet_def["colors"] = colors or {}
        self.data["defs"][name] = bullet_def

    def save_to_file(self, filename="bullet_defs.json"):
        """将当前所有数据保存为指定名称的 JSON 文件"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, indent=2, ensure_ascii=False)
            print(f"成功导出: {filename}")
        except Exception as e:
            print(f"导出失败: {e}")



if __name__ == "__main__":
    generator = BulletConfigGenerator()
    # 添加子弹
    # 点弹
    generator.add_bullet(
        name="ball_small",
        collision={"a": 2, "b": 2, "is_rect": False},
        offset={"x": 0, "y": 0},
        scale_x=0.5,
        scale_y=0.5,
        colors={str(i): f"ball_small_{i}" for i in range(1, 17)}
    )
    # 黑点弹
    generator.add_bullet(
        name="mildew",
        collision={"a": 2, "b": 2, "is_rect": False},
        offset={"x": 0, "y": 0},
        scale_x=0.5,
        scale_y=0.5,
        colors={str(i): f"mildew_{i}" for i in range(1, 17)}
    )
    # 米弹
    generator.add_bullet(
        name="grain_a",
        collision={"a": 2.5, "b": 2.5, "is_rect": False},
        offset={"x": 0, "y": 0},
        scale_x=0.5,
        scale_y=0.5,
        colors={str(i): f"grain_a_{i}" for i in range(1, 17)}
    )
    # 棱弹
    generator.add_bullet(
        name="grain_b",
        collision={"a": 2.5, "b": 2.5, "is_rect": False},
        offset={"x": 0, "y": 0},
        scale_x=0.5,
        scale_y=0.5,
        colors={str(i): f"ball_mid_{i}" for i in range(1, 17)}
    )
    # 黑米弹
    generator.add_bullet(
        name="grain_c",
        collision={"a": 2.5, "b": 2.5, "is_rect": False},
        offset={"x": 0, "y": 0},
        scale_x=0.5,
        scale_y=0.5,
        colors={str(i): f"grain_c_{i}" for i in range(1, 17)}
    )
    # 苦无弹
    generator.add_bullet(
        name="arrow_small",
        collision={"a": 2.5, "b": 2.5, "is_rect": False},
        offset={"x": 0, "y": 0},
        scale_x=0.5,
        scale_y=0.5,
        colors={str(i): f"arrow_small_{i}" for i in range(1, 17)}
    )
    # 钱弹
    generator.add_bullet(
        name="money",
        collision={"a": 4, "b": 4, "is_rect": False},
        offset={"x": 0, "y": 0},
        scale_x=0.5,
        scale_y=0.5,
        colors={str(i): f"money_{i}" for i in range(1, 9)}
    )
    # 统弹
    generator.add_bullet(
        name="gun_bullet",
        collision={"a": 2.5, "b": 2.5, "is_rect": False},
        offset={"x": 0, "y": 0},
        scale_x=0.5,
        scale_y=0.5,
        colors={str(i): f"gun_bullet_{i}" for i in range(1, 17)}
    )
    # 休止符
    generator.add_bullet(
        name="silence",
        collision={"a": 4.5, "b": 4.5, "is_rect": False},
        offset={"x": 0, "y": 0},
        scale_x=0.5,
        scale_y=0.5,
        colors={str(i): f"silence_{i}" for i in range(1, 17)}
    )
    # 滴弹
    generator.add_bullet(
        name="kite",
        collision={"a": 2.5, "b": 2.5, "is_rect": False},
        offset={"x": 0, "y": 0},
        scale_x=0.5,
        scale_y=0.5,
        colors={str(i): f"kite_{i}" for i in range(1, 17)}
    )
    # 箭弹
    generator.add_bullet(
        name="arrow_mid",
        collision={"a": 3.5, "b": 3.5, "is_rect": False},
        offset={"x": 0, "y": 0},
        scale_x=0.5,
        scale_y=0.5,
        colors={str(i): f"arrow_mid_{i}" for i in range(1, 17)}
    )
    # 箭弹
    generator.add_bullet(
        name="arrow_mid",
        collision={"a": 3.5, "b": 3.5, "is_rect": False},
        offset={"x": 0, "y": 0},
        scale_x=0.5,
        scale_y=0.5,
        colors={str(i): f"arrow_mid_{i}" for i in range(1, 17)}
    )
    # 札弹
    generator.add_bullet(
        name="square",
        collision={"a": 3, "b": 3, "is_rect": False},
        offset={"x": 0, "y": 0},
        scale_x=0.5,
        scale_y=0.5,
        colors={str(i): f"square_{i}" for i in range(1, 17)}
    )
    # 鳞弹
    generator.add_bullet(
        name="arrow_big",
        collision={"a": 2.5, "b": 2.5, "is_rect": False},
        offset={"x": 0, "y": 0},
        scale_x=0.5,
        scale_y=0.5,
        colors={str(i): f"arrow_big_{i}" for i in range(1, 17)}
    )
    # 小玉
    generator.add_bullet(
        name="ball_mid",
        collision={"a": 4, "b": 4, "is_rect": False},
        offset={"x": 0, "y": 0},
        scale_x=0.5,
        scale_y=0.5,
        colors={str(i): f"ball_mid{i}" for i in range(1, 17)}
    )
    # 环玉
    generator.add_bullet(
        name="ball_mid_c",
        collision={"a": 4, "b": 4, "is_rect": False},
        offset={"x": 0, "y": 0},
        scale_x=0.5,
        scale_y=0.5,
        colors={str(i): f"ball_mid_c_{i}" for i in range(1, 17)}
    )
    # 刀弹
    generator.add_bullet(
        name="knife",
        collision={"a": 4, "b": 4, "is_rect": False},
        offset={"x": 0, "y": 0},
        scale_x=0.5,
        scale_y=0.5,
        colors={str(i): f"knife_{i}" for i in range(1, 17)}
    )
    # 刀弹
    generator.add_bullet(
        name="knife",
        collision={"a": 4, "b": 4, "is_rect": False},
        offset={"x": 0, "y": 0},
        scale_x=0.5,
        scale_y=0.5,
        colors={str(i): f"knife_{i}" for i in range(1, 17)}
    )
    # 小星弹
    generator.add_bullet(
        name="star_small",
        collision={"a": 3, "b": 3, "is_rect": False},
        offset={"x": 0, "y": 0},
        scale_x=0.5,
        scale_y=0.5,
        colors={str(i): f"star_small_{i}" for i in range(1, 17)}
    )
    # 椭弹
    generator.add_bullet(
        name="ellipse",
        collision={"a": 3, "b": 3, "is_rect": False},
        offset={"x": 0, "y": 0},
        scale_x=0.5,
        scale_y=0.5,
        colors={str(i): f"ellipse_{i}" for i in range(1, 17)}
    )
    # 椭弹
    generator.add_bullet(
        name="ellipse",
        collision={"a": 3, "b": 3, "is_rect": False},
        offset={"x": 0, "y": 0},
        scale_x=0.5,
        scale_y=0.5,
        colors={str(i): f"ellipse_{i}" for i in range(1, 17)}
    )
    # 火弹
    generator.add_bullet(
        name="water_drop",
        type="ani",
        interval=6,
        scale_x=0.5,
        scale_y=0.5,
        colors={
            str(i): [f"water_drop_1_{i}", f"water_drop_2_{i}", f"water_drop_3_{i}"] for i in range(1, 17)
        }
    )
    # 蝶弹
    generator.add_bullet(
        name="butterfly",
        collision={"a": 4, "b": 4, "is_rect": False},
        offset={"x": 0, "y": 0},
        scale_x=0.5,
        scale_y=0.5,
        colors={str(i): f"butterfly_{i}" for i in range(1, 17)}
    )
    # 中玉
    generator.add_bullet(
        name="ball_big",
        collision={"a": 8, "b": 8, "is_rect": False},
        offset={"x": 0, "y": 0},
        scale_x=0.5,
        scale_y=0.5,
        colors={str(i): f"ball_big_{i}" for i in range(1, 17)}
    )
    # 心弹
    generator.add_bullet(
        name="heart",
        collision={"a": 9, "b": 9, "is_rect": False},
        offset={"x": 0, "y": 0},
        scale_x=0.5,
        scale_y=0.5,
        colors={str(i): f"heart_{i}" for i in range(1, 17)}
    )
    # 弯刀弹
    generator.add_bullet(
        name="knife_b",
        collision={"a": 3.5, "b": 3.5, "is_rect": False},
        offset={"x": 0, "y": 0},
        scale_x=0.5,
        scale_y=0.5,
        colors={str(i): f"knife_b_{i}" for i in range(1, 17)}
    )
    # preimg
    generator.add_bullet(
        name="preimg",
        collision={"a": 4, "b": 4, "is_rect": False},
        offset={"x": 0, "y": 0},
        scale_x=0.5,
        scale_y=0.5,
        colors={str(i): f"preimg_{i}" for i in range(1, 17)}
    )
    # 大星弹
    generator.add_bullet(
        name="star_big",
        collision={"a": 5.5, "b": 5.5, "is_rect": False},
        offset={"x": 0, "y": 0},
        scale_x=0.5,
        scale_y=0.5,
        colors={str(i): f"star_big_{i}" for i in range(1, 17)}
    )
    # bubble
    generator.add_bullet(
        name="bubble",
        collision={"a": 4, "b": 4, "is_rect": False},
        offset={"x": 0, "y": 0},
        scale_x=0.5,
        scale_y=0.5,
        colors={str(i): f"bubble_{i}" for i in range(1, 17)}
    )
    # 音符弹
    generator.add_bullet(
        name="music",
        type="ani",
        interval=6,
        scale_x=0.5,
        scale_y=0.5,
        colors={
            str(i): [f"music_1_{i}", f"music_2_{i}", f"music_3_{i}"] for i in range(1, 17)
        }
    )
    # 大玉
    generator.add_bullet(
        name="ball_huge",
        collision={"a": 13.5, "b": 13.5, "is_rect": False},
        offset={"x": 0, "y": 0},
        scale_x=0.5,
        scale_y=0.5,
        colors={str(i): f"ball_huge{i}" for i in range(1, 17)}
    )
    # 光玉
    generator.add_bullet(
        name="ball_light",
        collision={"a": 11.5, "b": 11.5, "is_rect": False},
        offset={"x": 0, "y": 0},
        scale_x=0.5,
        scale_y=0.5,
        colors={str(i): f"ball_light{i}" for i in range(1, 17)}
    )
    # 输出到文件
    generator.save_to_file("bullet_defs.json")