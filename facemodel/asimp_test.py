import pyassimp
from pyassimp import load

scene = load('model.fbx')
print(111)
assert len(scene.meshes)
mesh = scene.meshes[0]

assert len(mesh.vertices)
print(mesh.vertices[0])
pyassimp.export(scene,'444.fbx','gltf2')
print(111)
