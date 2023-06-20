import bpy
import os

path = "/home/limr/Desktop/model/男_fbx_new"

for i in os.listdir(path):
    filepath = os.path.join(path, i)
    bpy.ops.import_scene.fbx(filepath=filepath)
    bpy.ops.export_scene.fbx(filepath="/home/limr/Desktop/test/"+i, path_miode="COPY", embed_textures=True, use_selection=True,
                             apply_unit_scale=True, global_scale=0.01)
    bpy.ops.object.delete()
    bpy.ops.outliner.orphans_purge()
    for i in bpy.data.actions:
        bpy.data.actions.remove(i, do_unlink = True)