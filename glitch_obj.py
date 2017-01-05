import bpy
import random


#set paths, stating the obvious but change these paths to match your machine
exportedFile = '/Users/gewoonsander/Documents/glitchobj/modelExport.obj'
glitchedFile = '/Users/gewoonsander/Documents/glitchobj/modelGlitched.obj'


#export obj
bpy.ops.export_scene.obj(filepath = exportedFile, use_materials = False)


#change numbers in obj file
def randomNumbers(n):
    count = 0
    f = open(exportedFile)
    fn = open(glitchedFile, 'w')
    for l in f:
        if count % n == 0:
            if l[0] == 'v':
                rn1 = random.choice(range(10))
                rn2 = random.choice(range(10))
                l = [str(rn1) if i == str(rn2) else i for i in l]
                
        fn.write(''.join(l))
        count += 1

    #close files
    f.close()
    fn.close()


#shuffle vertex lines
def shuffleVertices(n):
    count = 0
    f1 = open(exportedFile)
    f2 = open(exportedFile)
    fn = open(glitchedFile, 'w')

    a = [l for l in f1 if l[0:2] == 'v ']
    random.shuffle(a)

    for l in f2:
        if (count % n == 0):
            if l[0:2] == 'v ':
                l = a[random.choice(range(len(a)))]

        fn.write(''.join(l))
        count += 1

    #close files
    f1.close()
    f2.close()
    fn.close()


shuffleVertices(5)
randomNumbers(5)


#delete all objects in scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)


#open glitched file
bpy.ops.import_scene.obj(filepath=glitchedFile)
