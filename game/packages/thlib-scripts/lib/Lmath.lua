---=====================================
---luastg math
---=====================================

----------------------------------------
---常量

PI = math.pi
PIx2 = math.pi * 2
PI_2 = math.pi * 0.5
PI_4 = math.pi * 0.25
SQRT2 = math.sqrt(2)
SQRT3 = math.sqrt(3)
SQRT2_2 = math.sqrt(0.5)
GOLD = 360 * (math.sqrt(5) - 1) / 2

----------------------------------------
---数学函数

int = math.floor
abs = math.abs
max = math.max
min = math.min
rnd = math.random
sqrt = math.sqrt

math.mod = math.mod or math.fmod
mod = math.mod

---获得数字的符号(1/-1/0)
function sign(x)
    if x > 0 then
        return 1
    elseif x < 0 then
        return -1
    else
        return 0
    end
end

---获得(x,y)向量的模长
function hypot(x, y)
    return sqrt(x * x + y * y)
end

---阶乘，目前用于组合数和贝塞尔曲线
local fac = {}
function Factorial(num)
    if num < 0 then
        error("Can't get factorial of a minus number.")
    end
    if num < 2 then
        return 1
    end
    num = int(num)
    if fac[num] then
        return fac[num]
    end
    local result = 1
    for i = 1, num do
        if fac[i] then
            result = fac[i]
        else
            result = result * i
            fac[i] = result
        end
    end
    return result
end

---组合数，目前用于贝塞尔曲线
function combinNum(ord, sum)
    if sum < 0 or ord < 0 then
        error("Can't get combinatorial of minus numbers.")
    end
    ord = int(ord)
    sum = int(sum)
    return Factorial(sum) / (Factorial(ord) * Factorial(sum - ord))
end

--------------------------------------------------------------------------------
--- 弹幕逻辑随机数发生器，用于支持 replay 系统

local ENABLE_NEW_RNG = false

if ENABLE_NEW_RNG then
    -- 2019 年的新一代 xoshiro256** 随机数发生器
    local random = require("random")
    ran = random.xoshiro512ss()
else
    -- 2006 年的 WELL512 随机数发生器
    ran = lstg.Rand()
end



function lerp_to(unit, struct, lerp_mode, lerp_time, target_value)
    local start_value = unit[struct]
    local delta = target_value - start_value
    local duration = math.floor(lerp_time)
    local mode = math.floor(lerp_mode)

    if duration <= 0 then
        unit[struct] = target_value
        return
    end

    task.New(unit, function()
        for t = 1, duration do
            task.Wait(1)
            local x = t / duration -- 进度 0.0 -> 1.0
            local r = x            -- 最终计算的比例

            -- 模式分支判断
            if mode == 0 then r = x                                   -- linear
            elseif mode == 1 then r = x^2                             -- easeIn2
            elseif mode == 2 then r = x^3                             -- easeIn3
            elseif mode == 3 then r = x^4                             -- easeIn4
            elseif mode == 4 then r = 1-(1-x)^2                       -- easeOut2
            elseif mode == 5 then r = 1-(1-x)^3                       -- easeOut3
            elseif mode == 6 then r = 1-(1-x)^4                       -- easeOut4
            elseif mode == 8 then r = 3*x^2 - 2*x^3                   -- smoothstep
            elseif mode >= 9 and mode <= 14 then                      -- Split 系列
                local is_in_first_half = x < 0.5
                local s_x = is_in_first_half and (x * 2) or ((x - 0.5) * 2)
                local s_r = 0
                
                -- 根据子模式选择基础曲线
                local p = (mode == 9 or mode == 12) and 2 or ((mode == 10 or mode == 13) and 3 or 4)
                
                if mode <= 11 then -- easeInOut
                    s_r = is_in_first_half and (s_x^p) or (1 - (1 - s_x)^p)
                else               -- easeOutIn
                    s_r = is_in_first_half and (1 - (1 - s_x)^p) or (s_x^p)
                end
                r = is_in_first_half and (s_r / 2) or (0.5 + s_r / 2)
            elseif mode == 15 then r = (x < 1) and 0 or 1             -- delayed
            elseif mode == 16 then r = 1                              -- instant
            elseif mode == 18 then r = math.sin(x * math.pi / 2)      -- easeOutSin
            elseif mode == 19 then r = 1 - math.cos(x * math.pi / 2)  -- easeInSin
            elseif mode == 20 or mode == 21 then                      -- Sin 复合
                if x < 0.5 then
                    local s_x = x * 2
                    local s_r = (mode == 20) and math.sin(s_x * math.pi / 2) or (1 - math.cos(s_x * math.pi / 2))
                    r = s_r / 2
                else
                    local s_x = (x - 0.5) * 2
                    local s_r = (mode == 20) and (1 - math.cos(s_x * math.pi / 2)) or math.sin(s_x * math.pi / 2)
                    r = 0.5 + s_r / 2
                end
            end

            -- 应用最终值
            unit[struct] = start_value + delta * r
        end
    end)
end

--示例:lerp_to(self,"vscale",0,60,3),把自身的vscale缩放在60帧之内以0号插值模式变成3