kite = Class(bullet)
function kite:init(color_index,x,y,v,angle,omega,destroyable)
    bullet.init(self,"kite",color_index,x,y,v,angle,omega,destroyable)
    New(bullet_fog,self,color_index,15,2.5,0.25,4)
end


money = Class(bullet)
function money:init(color_index,x,y,v,angle,omega,destroyable)
    bullet.init(self,"money",color_index,x,y,v,angle,omega,destroyable)
    New(bullet_fog,self,color_index,15,2.5,0.25,4)
end


mildew = Class(bullet)
function mildew:init(color_index,x,y,v,angle,omega,destroyable)
    bullet.init(self,"mildew",color_index,x,y,v,angle,omega,destroyable)
    New(bullet_fog,self,color_index,15,2.5,0.25,4)
end


ball_big = Class(bullet)
function ball_big:init(color_index,x,y,v,angle,omega,destroyable)
    bullet.init(self,"ball_big",color_index,x,y,v,angle,omega,destroyable)
    New(bullet_fog,self,color_index,15,5,1,4)
end


grain_a = Class(bullet)
function grain_a:init(color_index,x,y,v,angle,omega,destroyable)
    bullet.init(self,"grain_a",color_index,x,y,v,angle,omega,destroyable)
    New(bullet_fog,self,color_index,8,1.5,0.25,4)
end



--[[
money
mildew
arrow_big
grain_b
ball_mid_c
ball_light
ball_huge
music
bubble
arrow_small
star_big
silence
preimg
arrow_mid
ball_small
square
grain_a
ball_mid
grain_c
knife
knife_b
heart
ball_big
butterfly
water_drop
ellipse
gun_bullet
star_small
]]