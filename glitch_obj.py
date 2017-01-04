import bpy
import random


#set paths, stating the obvious but change these paths to match your machine
exportedFile = '/Users/gewoonsander/Documents/glitchobj/modelExport.obj'
glitchedFile = '/Users/gewoonsander/Documents/glitchobj/modelGlitched.obj'


#export obj
bpy.ops.export_scene.obj(filepath=exportedFile)


#change numbers in obj file
count = 0
f = open(exportedFile)
fn = open(glitchedFile, 'w')
for l in f:
    if count % 10 == 0:
        if l[0] == 'v':
            rn1 = random.choice(range(5))
            rn2 = random.choice(range(10))
            l = [str(rn1) if i == str(rn2) else i for i in l]
    fn.write(''.join(l))
    count = count + 1


#save file
f.close()
fn.close()


#delete all objects in scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)


#open glitched file
bpy.ops.import_scene.obj(filepath=glitchedFile)
