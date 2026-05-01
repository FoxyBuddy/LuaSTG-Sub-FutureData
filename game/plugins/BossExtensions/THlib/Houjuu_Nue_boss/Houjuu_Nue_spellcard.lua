LoadImageFromFile("_scbg", "THlib/Houjuu_Nue_boss/cdbg07a.png", true, 0, 0, false)
LoadImageFromFile("_scbg_mask", "THlib/Houjuu_Nue_boss/cdbg07b.png", true, 0, 0, false)

spellcard_background = Class(_spellcard_background)
spellcard_background.init = function(self)
    _spellcard_background.init(self)
    _spellcard_background.AddLayer(self, "_scbg_mask", true, 0, 0, 0, 1, 1, 0, "", 1, 1, nil, nil)
    _spellcard_background.AddLayer(self, "_scbg", false, 0, 0, 0, 0, 0, 0, "", 1, 1, nil, nil)
end
