import json

class BulletConfigGenerator:
    def __init__(self):
        self.data = {"defs": {}}

    def _generate_colors(self, name, count):
        """生成 1 到 count 的颜色映射"""
        return {str(i): f"{name}_{i}" for i in range(1, count + 1)}

    def add_effect(self, name, time,start_alpha,tag_alpha,start_scale,tag_scale,use_bullet_img):
        self.data["defs"][name] = {
            "time": 8,
            "alpha":{"start_alpha":start_alpha,"tag_alpha":tag_alpha},
            "scale": {"start_scale":start_scale,"tag_scale":tag_scale},
            "use_bullet_img":use_bullet_img
        }

    
    def save(self, filename="bullet_effect_defs.json"):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)
        print(f"成功导出: {filename}")


if __name__ == "__main__":
    gen = BulletConfigGenerator()

    # 1. ball_small
    gen.add_effect("ball_small",8,0,255,2,0.5,False)
    # 2. mildew
    gen.add_effect("mildew",8,0,255,2,0.5,False)
    # 3. grain_a
    gen.add_effect("grain_a",8,0,255,3,0.5,False)
    # 4. grain_b
    gen.add_effect("grain_b",8,0,255,3,0.5,False)
    # 5. grain_c
    gen.add_effect("grain_c",8,0,255,3,0.5,False)
    # 6. arrow_small
    gen.add_effect("arrow_small",8,0,255,3,0.5,False)
    # 7. gun_bullet
    gen.add_effect("gun_bullet",8,0,255,3,0.5,False)
    # 8. silence
    gen.add_effect("silence",8,0,255,5,1,True)
    # 9. kite
    gen.add_effect("kite",8,0,255,3,0.5,False)
    # 10. arrow_mid
    gen.add_effect("arrow_mid",8,0,255,5,1,False)
    # 11. money
    gen.add_effect("money",8,0,255,3,0.5,False)
    # 12. square
    gen.add_effect("square",8,0,255,3,0.5,False)
    # 13. arrow_big
    gen.add_effect("arrow_big",8,0,255,3,0.5,False)
    # 14. ball_mid
    gen.add_effect("ball_mid",8,0,255,3,0.5,False)
    # 15. ball_mid_c
    gen.add_effect("ball_mid_c",8,0,255,3,0.5,False)
    # 16. knife
    gen.add_effect("knife",8,0,255,5,1,False)
    # 17. star_small
    gen.add_effect("star_small",8,0,255,3,0.5,False)
    # 18. ellipse
    gen.add_effect("ellipse",8,0,255,5,1,False)
    # 19. water_drop
    gen.add_effect("water_drop",8,0,255,5,1,True)
    # 20. butterfly
    gen.add_effect("butterfly",8,0,255,5,1,False)
    # 21. ball_big
    gen.add_effect("ball_big",8,0,255,5,1,False)
    # 22. heart
    gen.add_effect("heart",8,0,255,5,1,False)
    # 23. knife_b
    gen.add_effect("knife_b",8,0,255,5,1,False)
    # 24. music
    gen.add_effect("music",8,0,255,5,1,True)
    # 25. star_big
    gen.add_effect("star_big",8,0,255,5,1,False)
    # 26. ball_huge
    gen.add_effect("ball_huge",8,0,255,2,1,True)
    # 27. ball_light
    gen.add_effect("ball_light",8,0,255,2,1,True)
    gen.save()