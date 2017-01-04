import bpy
import random


#set paths, stating the obvious but change these paths to match your machine
exportedFile = '/Users/gewoonsander/Documents/glitchobj/modelExport.obj'
glitchedFile = '/Users/gewoonsander/Documents/glitchobj/modelGlitched.obj'


#save obj

bpy.ops.export_scene.obj(filepath=exportedFile)


#change numbers in obj file
count = 0
f = open(exportedFile)
fn = open(glitchedFile, 'w')
for l in f:
    if count % 10 == 0:
        if l[0:2] == 'v ':
            l = ['1' if i == '0' else i for i in l]
            l = [str(i) for i in l]
    fn.write(''.join(l))
    count = count + 1


#save file and reopen in c4d (merge with current doc)
f.close()
fn.close()


#open glitched file
bpy.ops.import_scene.obj(filepath=glitchedFile)
