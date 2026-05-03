--bullet_effects.lua by phsonh 26.5.3


bullet_fog = Class(object)
function bullet_fog:init(master_bullet,color_index,time,max_scale,min_scale,lerp_mode)
    --捕获父子弹对象
    self.master_bullet = master_bullet
    --弹雾持续时间
    self.stay_time = time
    --弹雾最大初始缩放
    self.max_scale = max_scale
    --弹雾最小初始缩放
    self.min_scale = min_scale
    --弹雾尺寸缩放的插值模式
    self.lerp_mode = lerp_mode
    --基础属性
    self.colli = false
    self.bound = self.master_bullet.bound
    self.x,self.y = self.master_bullet.x,self.master_bullet.y
    self.layer=self.master_bullet.layer + 5
    self.group=GROUP_GHOST
    self._a,self.vscale,self.hscale = 255,self.max_scale,self.max_scale
    self._blend = "mul+add"
    self.rot = self.master_bullet.rot


    --对于大玉/光玉/炎弹/音符等弹型,其弹雾贴图为子弹贴图,use_bullet_img传入true,其他弹型传入false
    self.use_bullet_img = false
    if self.use_bullet_img then
        --使用子弹贴图
        self.img = self.master_bullet.img
    else
        --使用默认弹雾贴图
        self.img = "preimg_" .. tostring(color_index)
    end


    --在stay_time帧之内把透明度以0插值模式从0变成255
    lerp_to(self,"_a",1,self.stay_time,0)
    --在stay_time帧之内把缩放以4插值模式从max_scale变成min_scale
    lerp_to(self,"vscale",self.lerp_mode,self.stay_time,self.min_scale)
    lerp_to(self,"hscale",self.lerp_mode,self.stay_time,self.min_scale)


    --弹雾期间关掉父子弹对象判定,且不显示子弹
    self.master_bullet.colli = false
    --self.master_bullet.hide = true
end


function bullet_fog:frame()
    task.Do(self)
    if IsValid(self.master_bullet) then
        --更新自身坐标,跟随子弹
        self.x,self.y = self.master_bullet.x,self.master_bullet.y
    end
    --Print(self.master_bullet.colli,self.master_bullet.a)
    if self.timer >= self.stay_time then
        --弹雾时间结束,开启父子弹对象判定和显示
        self.master_bullet.colli = true
        self.master_bullet.hide = false
        --删除弹雾对象
        Del(self)
    end
end


function bullet_fog:render()
    if self._blend and self._a and self._r and self._g and self._b then
        SetImgState(self, self._blend, self._a, self._r, self._g, self._b)
    end
    DefaultRenderFunc(self)
    if self._blend and self._a and self._r and self._g and self._b then
        SetImgState(self, '', 255, 255, 255, 255)
    end
end


bullet_break = Class(object)
function bullet_break:init()
    
end