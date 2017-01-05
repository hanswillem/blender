import bpy
import random


def glitch(n1, n2):
    
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
                if (count % n == 0):
                    if l[0:2] == 'v ':
                        l = a[random.choice(range(len(a)))]

                fn.write(''.join(l))
                count += 1

            f1.close()
            f2.close()
            fn.close()
        else:
            pass

    #set paths, stating the obvious but change these paths to match your machine
    exportedFile = '/Users/gewoonsander/Documents/glitchobj/modelExport.obj'
    glitchedFile = '/Users/gewoonsander/Documents/glitchobj/modelGlitched.obj'

    #export obj
    bpy.ops.export_scene.obj(filepath = exportedFile, use_materials = False)

    shuffleVertices(n1)
    randomNumbers(n2)

    #delete all objects in scene
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

    #open glitched file
    bpy.ops.import_scene.obj(filepath=glitchedFile)


glitch(5, 5)
