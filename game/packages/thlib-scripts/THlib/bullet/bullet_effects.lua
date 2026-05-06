--bullet_effects.lua by phsonh 26.5.3



function bullet_fog(master_bullet,color_index,time,start_alpha,tag_alpha,start_scale,tag_scale,use_bullet_img)
    local master = master_bullet
    local color = color_index
    local bullet_hscale,bullet_vscale = master.hscale,master.vscale
    local bullet_a = master._a
    --获取子弹的类型,判断应该用什么尺寸的弹雾
    --local fog_eff = bullet_mgr.bullet_effect.fog[master.style]


    --对于大玉/光玉/炎弹/音符等弹型,其弹雾贴图为子弹贴图,use_bullet_img传入true,其他弹型传入false
    use_bullet_img = use_bullet_img or false
    local bullet_img = master.img
    if not use_bullet_img then
        --使用默认弹雾贴图
        master.img = "fog_img_" .. tostring(color_index)
    end

    master._a = start_alpha
    master.vscale,master.hscale = start_scale,start_scale
    master.layer = LAYER_ENEMY_BULLET_EF
    master.colli = false

    --在time帧之内把透明度以0插值模式从start_alpha变成tag_alpha
    lerp_to(master,"_a",0,time,tag_alpha)
    --在time帧之内把缩放以4插值模式从start_scale变成tag_scale
    lerp_to(master,"vscale",0,time,tag_scale)
    --lerp_to(master,"vscale",4,time,tag_scale)
    lerp_to(master,"hscale",0,time,tag_scale)
    --lerp_to(master,"hscale",4,time,tag_scale)
    task.New(master,function ()
        task.Wait(time)
        master.layer = LAYER_ENEMY_BULLET
        master.colli = true
        master.img = bullet_img
        master.hscale,master.vscale = bullet_hscale,bullet_vscale
        master._a = bullet_a
    end)
end




bullet_break = Class(object)
function bullet_break:init()
    
end