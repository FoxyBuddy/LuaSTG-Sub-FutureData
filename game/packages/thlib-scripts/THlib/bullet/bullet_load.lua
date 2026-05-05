--bullet_load.lua by phsonh 26.5.3
bullet_mgr = bullet_mgr or {}
--子弹类型表
bullet_mgr.bullet_styles = {}
--加载json文件并转成表
local bullet_sprites = LoadTableFromJson(LoadJson(bullet_mgr.path .. "bullet_sprites.json"))
local bullet_defs = LoadTableFromJson(LoadJson(bullet_mgr.path .. "bullet_defs.json"))
--加载子弹图集
local bullet_tex_name = bullet_sprites.textures[1].path
LoadTexture('bullet', bullet_mgr.path .. bullet_tex_name, true)
--注册子弹类型表
for bullet_style,defs in pairs(bullet_defs.defs) do
    table.insert(bullet_mgr.bullet_styles,bullet_style)
end

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
        Print(a,b)
        local is_rect = coll_info.is_rect
        local bullet_type = conf["type"]
        local scale = (conf["scale_x"] + conf["scale_y"])/2
        local c_x = w / 2 + conf["offset"]["x"]
        local c_y = h / 2 - conf["offset"]["y"]
        if bullet_type == "ani" then
            --如果是动画类型子弹
            local row_num = conf["row_num"]
            local col_num = conf["col_num"]
            local interval = conf["interval"]
            --单张子弹纹理的宽高
            local single_w = w / conf["col_num"]
            local single_h = h / conf["row_num"]
            --全局缩放和中心偏移
             --json中纹理中心所采用的的坐标系与标准纹理坐标系的y轴方向相反
            --加载子弹动画
            LoadAnimation(name,tex,x,y,single_w,single_h,col_num,row_num,interval,a,b,is_rect)
            SetAnimationCenter(name,c_x,c_y)
            SetAnimationScale(name,scale)
        elseif bullet_type == "static" then
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

-- 打印子弹类型表
Print("Bullet Styles:")
for i, style_name in ipairs(bullet_mgr.bullet_styles) do
    Print(string.format("[%d] %s", i, style_name))
end