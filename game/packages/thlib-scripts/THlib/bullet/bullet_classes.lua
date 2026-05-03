--bullet_classes.lua by phsonh 26.5.3


bullet = Class(object)

function bullet:init(bullet_style,color_index,x,y,v,angle,omega,destroyable)
    self.img = bullet_style .. "_" .. tostring(color_index)
    self.x = x
    self.y = y
    self.layer = LAYER_ENEMY_BULLET
    self.group = GROUP_ENEMY_BULLET

    SetV(self, v, angle, true)
    self.omiga = omega or 0
end

function bullet:frame()
    task.Do(self)
    Print(self.colli,self.a)
end

function bullet:kill()
    local w = lstg.world
    New(item_faith_minor, self.x, self.y)
    if self._index and BoxCheck(self, w.boundl, w.boundr, w.boundb, w.boundt) then
        New(BulletBreak, self.x, self.y, self._index)
    end
end

function bullet:del()
    --	self.imgclass.del(self)
    local w = lstg.world
    if self._index and BoxCheck(self, w.boundl, w.boundr, w.boundb, w.boundt) then
        New(BulletBreak, self.x, self.y, self._index)
    end
end

function bullet:render()
    if self._blend and self._a and self._r and self._g and self._b then
        SetImgState(self, self._blend, self._a, self._r, self._g, self._b)
    end
    DefaultRenderFunc(self)
    if self._blend and self._a and self._r and self._g and self._b then
        SetImgState(self, '', 255, 255, 255, 255)
    end
end



danmaku = {}
danmaku.__index = danmaku
function danmaku:new()
    local obj = {
        tex          = arrow_big,
        color        = COLOR_RED,
        offset       = {x=0,y=0},
        speed        = {max=1.0,min=1.0},
        angle        = {main=0,delta=0},
        num          = {way=1,layer=1},
        form         = {style="fan",aim=false},
        se           = nil,
        polar_offset = {angle=0,radius=0},
        omiga        = 0,
        tasks        = {},
        fog          = {time=8,max_scale=1.5,min_scale=0.25,use_bullet_img=false}
    }
    return setmetatable(obj, self)
end

---发射弹幕
---@param unit any 发弹的单位（通常是 boss 或 enemy）
function danmaku:shoot(unit)
    local layer_num = self.num.layer
    local way_num   = self.num.way
    local layer_d_speed = (layer_num > 1) and (-(self.speed.max - self.speed.min) / (layer_num - 1)) or 0
    if self.se then 
        PlaySound(self.se, 0.1, unit.x / 256, false)
    end
    local target_dir = self.angle.main
    -- 只要aim不是0就叠加指向玩家的角度
    if self.form.aim ~= 0 then
        target_dir = target_dir + Angle(unit, player)
    end

    -- 样式
    if self.form.style == "fan" then
        -- 扇形样式
        -- 奇偶狙完全由 way_num 决定,奇数 way 必中，偶数 way 必空
        local start_angle = target_dir - (self.angle.delta * (way_num - 1)) / 2

        for way = 1, way_num do
            local current_way_angle = start_angle + (way - 1) * self.angle.delta
            local dx = self.offset.x + self.polar_offset.radius * cos(current_way_angle + self.polar_offset.angle)
            local dy = self.offset.y + self.polar_offset.radius * sin(current_way_angle + self.polar_offset.angle)
            for layer = 1, layer_num do
                local speed = self.speed.max + (layer - 1) * layer_d_speed
                local bullet = New(bullet,self.tex, self.color, unit.x + dx, unit.y + dy, speed,current_way_angle,self.omiga,true)
                bullet.master = self
                New(bullet_fog,bullet,self.color,self.fog.time,self.fog.max_scale,self.fog.min_scale,self.fog.use_bullet_img)
                for i, task_func in ipairs(self.tasks) do
                    task.New(bullet,task_func)
                end
            end
        end

    elseif self.form.style == "ring" then
        -- 环形样式
        local step = 360 / way_num
        -- aim = 2 时，相位偏移半个步长实现偶数狙
        local offset = (self.form.aim == 2) and (step / 2) or 0
        local start_angle = target_dir + offset

        for way = 1, way_num do
            local way_base = start_angle + (way - 1) * step
            local dx = self.offset.x + self.polar_offset.radius * cos(way_base + self.polar_offset.angle)
            local dy = self.offset.y + self.polar_offset.radius * sin(way_base + self.polar_offset.angle)

            for layer = 1, layer_num do
                -- delta_angle 控制螺旋偏移方向
                local final_angle = way_base + (layer - 1) * self.angle.delta
                local speed = self.speed.max + (layer - 1) * layer_d_speed
                local bullet = New(bullet,self.tex, self.color, unit.x + dx, unit.y + dy, speed,final_angle,self.omiga,true)
                bullet.master = self
                New(bullet_fog,bullet,self.color,self.fog.time,self.fog.max_scale,self.fog.min_scale,self.fog.use_bullet_img)
                for i, task_func in ipairs(self.tasks) do
                    task.New(bullet,task_func)
                end
            end
        end
    end
end

---设置弹幕子弹类型和颜色
---@param bullet_type any 子弹类型
---@param bullet_color any 颜色
function danmaku:set_type(bullet_type, bullet_color)
    self.tex = bullet_type
    self.color = bullet_color
end

---设置弹幕的发弹点横纵坐标偏移
---@param offset_x number x轴偏移
---@param offset_y number y轴偏移
function danmaku:set_offset(offset_x, offset_y)
    self.offset.x = offset_x
    self.offset.y = offset_y
end

---设置弹幕的角度参数
---@param dir number 方向参数, 代表弹幕中心轴
---@param diff number 角度差参数
function danmaku:set_angle(dir, diff)
    self.angle.main = dir
    self.angle.delta = diff
end
---设置弹幕的速度参数
---@param max_speed number 最大速度
---@param min_speed number 最小速度
function danmaku:set_speed(max_speed, min_speed)
    self.speed.max = max_speed
    self.speed.min = min_speed
end

---设置弹幕的way数和每way层数
---@param way number way数
---@param layer number 层数
function danmaku:set_num(way, layer)
    self.num.way = way
    self.num.layer = layer
end

---设置弹幕的展开方式
---@param style any 展开方式 "fan"/"ring"
---@param aim number 狙击模式:0:无,1:奇数,2:偶数
function danmaku:set_form(style,aim)
    self.form.style = style
    self.form.aim = aim
end

---设置弹幕的发射音效
---@param se any 音效
function danmaku:set_sound(se)
    self.se = se
end

---设置极坐标偏移
---@param angle number 极坐标角度
---@param radius number 极坐标半径
function danmaku:set_polar_offset(angle, radius)
    self.polar_offset.angle = angle
    self.polar_offset.radius = radius
end

---克隆当前的弹幕配置
---@return table 返回一个新的 Danmaku 实例
function danmaku:clone()
    local new_obj = danmaku:new() -- 创建一个拥有默认值的新实例
    
    -- 遍历当前对象的所有属性并赋值给新对象
    for k, v in pairs(self) do
        if type(v) == "table" then
            -- 如果是表，需要简单深拷贝一层
            -- 这样修改新弹幕的任务时，不会影响旧弹幕
            new_obj[k] = {}
            for sub_k, sub_v in pairs(v) do
                new_obj[k][sub_k] = sub_v
            end
        else
            -- 普通属性（数字、字符串、布尔值）直接赋值
            new_obj[k] = v
        end
    end
    
    return new_obj
end

function danmaku:add_task(task_func)
    table.insert(self.tasks,task_func)
end

function danmaku:set_task(index,task_func)
    self.tasks[index] = task_func
end

function danmaku:set_fog(time,max_scale,min_scale,use_bullet_img)
    self.fog.time = time
    self.fog.max_scale = max_scale
    self.fog.min_scale = min_scale
    self.fog.use_bullet_img = use_bullet_img or false

end