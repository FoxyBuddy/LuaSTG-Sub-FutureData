--bullet_load.lua by phsonh 26.5.3
bullet_mgr = bullet_mgr or {}
--子弹类型表
bullet_mgr.bullet_styles = {}
bullet_mgr.bullet_hitbox = {}
bullet_mgr.bullet_effect = {}
bullet_mgr.bullet_effect.fog = {}
bullet_mgr.bullet_effect.del = {}
--加载json文件并转成表
local bullet_sprites = LoadTableFromJson(LoadJson(bullet_mgr.path .. "bullet_sprites.json"))
local bullet_defs = LoadTableFromJson(LoadJson(bullet_mgr.path .. "bullet_defs.json"))
local bullet_effect_sprites = LoadTableFromJson(LoadJson(bullet_mgr.path .. "bullet_effect_sprites.json"))
local bullet_effect_defs = LoadTableFromJson(LoadJson(bullet_mgr.path .. "bullet_effect_defs.json"))
local bullet_break_sprites = LoadTableFromJson(LoadJson(bullet_mgr.path .. "bullet_break_sprites.json"))
--加载子弹纹理图集
local bullet_tex_name = bullet_sprites.textures[1].name
local bullet_tex_path = bullet_sprites.textures[1].path
LoadTexture(bullet_tex_name, bullet_mgr.path .. bullet_tex_path, true)
--加载子弹效果图集
local bullet_effect_tex_name = bullet_effect_sprites.textures[1].name
local bullet_effect_tex_path = bullet_effect_sprites.textures[1].path
LoadTexture(bullet_effect_tex_name, bullet_mgr.path .. bullet_effect_tex_path, true)
--加载消弹道具图集
local bullet_break_tex_name = bullet_break_sprites.textures[1].name
local bullet_break_tex_path = bullet_break_sprites.textures[1].path
LoadTexture(bullet_break_tex_name, bullet_mgr.path .. bullet_break_tex_path, true)
--注册子弹类型表
for bullet_style,defs in pairs(bullet_defs.defs) do
    table.insert(bullet_mgr.bullet_styles,bullet_style)
end
table.sort(bullet_mgr.bullet_styles)

bullet_mgr.insertMap = function(map, key, value)
	map[key] = value
end

for bullet_style,defs in pairs(bullet_defs.defs) do
    bullet_mgr.insertMap(bullet_mgr.bullet_hitbox, bullet_style, bullet_defs.defs[bullet_style].collision)
end
table.sort(bullet_mgr.bullet_hitbox)

--加载子弹贴图
for i,bullet_sprite in pairs(bullet_sprites.sprites) do
    --获取位于bullet_sprites的子弹贴图(包含颜色索引)
    local name = bullet_sprite.name
    local style = bullet_sprite.type
    local tex = bullet_sprite.texture
    local x = bullet_sprite.rect.x
    local y = bullet_sprite.rect.y
    local w = bullet_sprite.rect.width
    local h = bullet_sprite.rect.height
    --获取位于bullet_defs.json的弹幕配置(不区分颜色)
    local conf = bullet_defs.defs[style]
    if conf then
        local coll_info = conf["collision"]
        local a = coll_info.a
        local b = coll_info.b
        local is_rect = coll_info.is_rect
        local bullet_type = conf["type"]
        local scale = (conf["scale_x"] + conf["scale_y"])/2
        if bullet_type == "ani" then
            --如果是动画类型子弹
            local row_num = conf["row_num"]
            local col_num = conf["col_num"]
            local interval = conf["interval"]
            --单张子弹纹理的宽高
            local single_w = w / conf["col_num"]
            local single_h = h / conf["row_num"]
            local c_x = single_w / 2 + conf["offset"]["x"]
            local c_y = single_h / 2 + conf["offset"]["y"]
            --全局缩放和中心偏移
            --json中纹理中心所采用的的坐标系与标准坐标系的y轴方向相同
            --加载子弹动画
            LoadAnimation(name,tex,x,y,single_w,single_h,col_num,row_num,interval,a,b,is_rect)
            SetAnimationCenter(name,c_x,c_y)
            SetAnimationScale(name,scale)
        elseif bullet_type == "static" then
            local c_x = w / 2 + conf["offset"]["x"]
            local c_y = h / 2 + conf["offset"]["y"]
            --如果是静态类型子弹,加载子弹纹理
            LoadImage(name,tex,x,y,w,h,a,b,is_rect)
            SetImageCenter(name,c_x,c_y)
            SetImageScale(name,scale)
            
        end
    else
        --异常处理
        Print("Unknown bullet style: " .. tostring(style))
    end
end

--加载子弹效果贴图
for i,bullet_effect_sprite in pairs(bullet_effect_sprites.sprites) do
    --获取位于bullet_effect_sprites的子弹特效贴图(包含颜色索引)
    local name = bullet_effect_sprite.name
    local tex = bullet_effect_sprite.texture
    local x = bullet_effect_sprite.rect.x
    local y = bullet_effect_sprite.rect.y
    local w = bullet_effect_sprite.rect.width
    local h = bullet_effect_sprite.rect.height
    local scale = bullet_effect_sprite.scale
    --加载子弹特效纹理
    LoadImage(name,tex,x,y,w,h,0,0,true)
    SetImageScale(name,scale)
end

--加载子弹特效默认配置
bullet_mgr.bullet_effect.fog = bullet_effect_defs.defs
--Print(bullet_mgr.bullet_effect.fog)
--加载消弹道具贴图
for i,bullet_break_sprite in pairs(bullet_break_sprites.sprites) do
    --获取位于bullet_break_sprites的消弹道具贴图(包含伪动画索引)
    local name = bullet_break_sprite.name
    local tex = bullet_break_sprite.texture
    local x = bullet_break_sprite.rect.x
    local y = bullet_break_sprite.rect.y
    local w = bullet_break_sprite.rect.width
    local h = bullet_break_sprite.rect.height
    local scale = bullet_break_sprite.scale
    --加载消弹道具纹理
    LoadImage(name,tex,x,y,w,h,0,0,true)
    SetImageScale(name,scale)
end

-- 打印子弹类型表
Print("Bullet Styles:")
for i, style_name in ipairs(bullet_mgr.bullet_styles) do
    Print(string.format("[%d] %s", i, style_name))
end
Print("Bullet Effects:")
local function PrintTable(t, name, indent)
    indent = indent or 0
    name = name or "root"
    local prefix = string.rep("  ", indent) -- 每层增加两个空格缩进

    if type(t) ~= "table" then
        Print(prefix .. name .. " = " .. tostring(t))
    else
        Print(prefix .. name .. " = {")
        for k, v in pairs(t) do
            PrintTable(v, k, indent + 1)
        end
        Print(prefix .. "}")
    end
end

-- 使用方法：
--PrintTable(bullet_mgr.bullet_effect.fog, "BulletDefs")