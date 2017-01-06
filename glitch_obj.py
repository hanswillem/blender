import bpy
import random


#export obj
def exportOBJ():
    bpy.ops.export_scene.obj(filepath = exportedFile, use_materials = False)


#import OBJ
def ImportOBJ():
    #delete all objects in scene
    bpy.ops.object.select_all(action = 'SELECT')
    bpy.ops.object.delete(use_global = False)

    #open glitched file
    bpy.ops.import_scene.obj(filepath = glitchedFile)


#change numbers in obj file
def randomNumbers(n):
    if n != 0:
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

        f.close()
        fn.close()
    else:
        pass


#shuffle vertex lines
def shuffleVertices(n):
    if n != 0:
        count = 0
        f1 = open(exportedFile)
        f2 = open(exportedFile)
        fn = open(glitchedFile, 'w')

        a = [l for l in f1 if l[0:2] == 'v ']
        random.shuffle(a)

        for l in f2:
            if count % n == 0:
                if l[0:2] == 'v ':
                    l = a[random.choice(range(len(a)))]

            fn.write(''.join(l))
            count += 1

        f1.close()
        f2.close()
        fn.close()
    else:
        pass


#remove faces
def removeFaces(n):
    if n != 0:
        count = 0;
        f = open(exportedFile)
        fn = open(glitchedFile, 'w')

        for l in f:
            if count % n == 0:
                if l[0] == 'f':
                    l = ''
                
            fn.write(''.join(l))
            count += 1

        f.close()
        fn.close()
    else:
        pass


def glitch(n1, n2, n3):
    exportOBJ()
    shuffleVertices(n1)
    ImportOBJ()
    exportOBJ()
    randomNumbers(n2)
    ImportOBJ()
    exportOBJ()
    removeFaces(n3)
    ImportOBJ()


#set paths, stating the obvious but change these paths to match your machine
exportedFile = '/Users/hanswillemgijzel/Documents/glitchobj/modelExport.obj'
glitchedFile = '/Users/hanswillemgijzel/Documents/glitchobj/modelGlitched.obj'


glitch(2, 2, 0)
