#DOESN'T WORK JET!!!

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
    if count % 25 == 0:
        rn1 = random.choice(range(10))
        rn2 = random.choice(range(10))
        l = [rn1 if i == str(rn2) else i for i in l] #pick random numbers and change them in other random numbers
        #l = [0 if i == 'f' else i for i in l] #remove faces
        l = [str(i) for i in l]
    fn.write(''.join(l))
    count = count + 1


#save file and reopen in c4d (merge with current doc)
f.close()
fn.close()


#open glitched file
bpy.ops.import_scene.obj(filepath=glitchedFile)
