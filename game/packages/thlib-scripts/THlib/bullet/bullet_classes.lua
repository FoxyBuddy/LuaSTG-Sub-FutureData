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