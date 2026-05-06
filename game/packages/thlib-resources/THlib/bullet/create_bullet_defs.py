import json

class BulletConfigGenerator:
    def __init__(self):
        self.data = {"defs": {}}

    def _generate_colors(self, name, count):
        """生成 1 到 count 的颜色映射"""
        return {str(i): f"{name}_{i}" for i in range(1, count + 1)}

    def add_static(self, name, a=4.0, b=4.0, scale=0.5, count=16, is_rect=False,off_x=0,off_y=0):
        """
        添加普通静态子弹
        :param name: 子弹名
        :param a: 碰撞参数 a
        :param b: 碰撞参数 b
        :param scale: 缩放比例
        :param count: 颜色/纹理数量
        :param is_rect: 是否为矩形判定
        """
        self.data["defs"][name] = {
            "type": "static",
            "collision": {"a": a, "b": b, "is_rect": is_rect},
            "offset": {"x": off_x, "y": off_y},
            "scale_x": scale,
            "scale_y": scale,
            "colors": self._generate_colors(name, count)
        }

    def add_ani(self, name, row, col, interval=8, a=4.0, b=4.0, scale=0.5, count=16, is_rect=False,off_x=0,off_y=0):
        """
        添加动画子弹
        :param name: 子弹名
        :param row: 行数
        :param col: 列数
        :param interval: 帧间隔
        """
        self.data["defs"][name] = {
            "type": "ani",
            "collision": {"a": a, "b": b, "is_rect": is_rect},
            "offset": {"x": off_x, "y": off_y},
            "scale_x": scale,
            "scale_y": scale,
            "interval": interval,
            "row_num": row,
            "col_num": col,
            "colors": self._generate_colors(name, count)
        }

    def save(self, filename="bullet_defs.json"):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)
        print(f"成功导出: {filename}")


if __name__ == "__main__":
    gen = BulletConfigGenerator()

    # 1. ball_small
    gen.add_static("ball_small",  a=2.0,  b=2.0,  scale=0.5, count=16)
    # 2. mildew
    gen.add_static("mildew",      a=2.0,  b=2.0,  scale=0.5, count=16)
    # 3. grain_a
    gen.add_static("grain_a",     a=2.5,  b=2.5,  scale=0.5, count=16)
    # 4. grain_b
    gen.add_static("grain_b",     a=2.5,  b=2.5,  scale=0.5, count=16)
    # 5. grain_c
    gen.add_static("grain_c",     a=2.5,  b=2.5,  scale=0.5, count=16)
    # 6. arrow_small
    gen.add_static("arrow_small", a=2.5,  b=2.5,  scale=0.5, count=16)

    # 7. gun_bullet
    gen.add_static("gun_bullet",  a=2.5,  b=2.5,  scale=0.5, count=16)
    # 8. slience (修正了拼写错误)
    gen.add_static("silence",     a=4.5,  b=4.5,  scale=0.5, count=16)
    # 9. kite
    gen.add_static("kite",        a=2.5,  b=2.5,  scale=0.5, count=16)
    # 10. arrow_mid
    gen.add_static("arrow_mid",   a=3.5,  b=3.5,  scale=0.5, count=16,off_x=16,off_y=0)
    # 11. money
    gen.add_static("money",       a=4.0,  b=4.0,  scale=0.5, count=16)
    # 12. square
    gen.add_static("square",      a=3.0,  b=3.0,  scale=0.5, count=16)
    # 13. arrow_big
    gen.add_static("arrow_big",   a=2.5,  b=2.5,  scale=0.5, count=16)
    # 14. ball_mid
    gen.add_static("ball_mid",    a=4.0,  b=4.0,  scale=0.5, count=16)
    # 15. ball_mid_c
    gen.add_static("ball_mid_c",  a=4.0,  b=4.0,  scale=0.5, count=16)
    # 16. knife
    gen.add_static("knife",       a=4.0,  b=4.0,  scale=0.5, count=16)
    # 17. star_small
    gen.add_static("star_small",  a=3.0,  b=3.0,  scale=0.5, count=16,off_x=0,off_y=1)
    # 18. ellipse
    gen.add_static("ellipse",     a=3.0,  b=3.0,  scale=0.5, count=16)

    # 19. water_drop (动画弹: w=288, h=64, 对应 1x3 帧)
    gen.add_ani("water_drop",     row=1, col=3, interval=6, a=4.0, b=4.0, scale=0.5, count=16)

    # 20. butterfly
    gen.add_static("butterfly",   a=4.0,  b=4.0,  scale=0.5, count=16)
    # 21. ball_big
    gen.add_static("ball_big",    a=8.0,  b=8.0,  scale=0.5, count=16)
    # 22. heart
    gen.add_static("heart",       a=9.0,  b=9.0,  scale=0.5, count=16)
    # 23. knife_b
    gen.add_static("knife_b",     a=3.5,  b=3.5,  scale=0.5, count=16)

    # 24. music (动画弹: w=192, h=64, 对应 1x3 帧)
    gen.add_ani("music",          row=1, col=3, interval=6, a=4.0, b=4.0, scale=0.5, count=16,off_x=16,off_y=0)
    # 25. star_big
    gen.add_static("star_big",    a=5.5,  b=5.5,  scale=0.5, count=16,off_x=0,off_y=-1)
    #gen.add_static("star_big",    a=5.5,  b=5.5,  scale=0.5, count=16,off_x=0,off_y=-0.5)
    # 26. ball_huge
    gen.add_static("ball_huge",   a=13.5, b=13.5, scale=0.5, count=16)
    # 27. ball_light
    gen.add_static("ball_light",  a=11.5, b=11.5, scale=0.5, count=16)

    gen.save()