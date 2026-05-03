--bullet_classes.lua by phsonh 26.5.3

bullet_fog = Class(object)
function bullet_fog:init(master_bullet,time)

end

bullet = Class(object)

function bullet:init(bullet_style,color_index,destroyable)
    bullet_fog(self,10)
end

function bullet:frame()
    task.Do(self)
end

function bullet:kill()
    local w = lstg.world
    New(item_faith_minor, self.x, self.y)
    if self._index and BoxCheck(self, w.boundl, w.boundr, w.boundb, w.boundt) then
        New(BulletBreak, self.x, self.y, self._index)
    end
    if self.imgclass.size == 2.0 then
        self.imgclass.del(self)
    end
end

function bullet:del()
    --	self.imgclass.del(self)
    local w = lstg.world
    if self.imgclass.size == 2.0 then
        self.imgclass.del(self)
    end
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