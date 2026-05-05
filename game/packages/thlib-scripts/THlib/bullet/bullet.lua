bullet_mgr = bullet_mgr or {}
bullet_mgr.path = "THlib/bullet/"
bullet_mgr.files = {"bullet_load.lua","bullet_effects.lua","bullet_classes.lua","bullet_styles.lua"}

for idx,file in pairs(bullet_mgr.files) do
    Include(bullet_mgr.path .. file)
end
