local path = "THlib/bullet/"


local bullet_sprites = LoadTableFromJson(LoadJson(path .. "bullet_sprites.json"))
local bullet_defs = LoadTableFromJson(LoadJson(path .. "bullet_defs.json"))


local bullet_tex = bullet_sprites.textures
LoadTexture('bullet', path .. bullet_tex, true)

--加载子弹贴图
for i,bullet in bullet_sprites do
    LoadImage(bullet.name,bullet.texture,bullet.rect.x,bullet.rect.y,bullet.rect.width,bullet.rect.height)
end