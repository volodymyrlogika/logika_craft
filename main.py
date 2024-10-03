from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

sky = Sky(texture='sky_sunset')

cube = Entity(model='cube', texture='grass', scale=1, collider='box', origin_y=-.5)
tree = Entity(model="assets\\minecraft_tree\\scene.gltf", scale=5, collider='box', origin_y=-.5)

ground = Entity(model='plane', collider='box', scale=150, texture='grass', texture_scale=(4,4))
ground.y=0
# EditorCamera()  # add camera controls for orbiting and moving the camera

player = FirstPersonController()
app.run()

