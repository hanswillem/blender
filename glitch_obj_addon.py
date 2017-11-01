bl_info = {
    "name": "Glitch Obj",
    "category": "Scripts",
}


import bpy
import random

def myScript():


    #export obj
    def exportOBJ():
        bpy.ops.export_scene.obj(filepath = exportedFile, use_materials = False)


    #import OBJ
    def importOBJ():
        #delete all objects in scene
        bpy.ops.object.select_all(action = 'SELECT')
        bpy.ops.object.delete(use_global = False)

        #open glitched file
        bpy.ops.import_scene.obj(filepath = glitchedFile)


    #change numbers in obj file
    def randomNumbers(n):
        if n != 0:
            exportOBJ()
            f = open(exportedFile)
            fn = open(glitchedFile, 'w')
            for l in f:
                if l[0] == 'v':
                    if random.random() < n:
                        rn1 = random.choice(range(10))
                        rn2 = random.choice(range(10))
                        l = [str(rn1) if i == str(rn2) else i for i in l]

                fn.write(''.join(l))

            f.close()
            fn.close()
            importOBJ()
        else:
            pass


    #shuffle vertex lines
    def shuffleVertices(n):
        if n != 0:
            exportOBJ()
            f1 = open(exportedFile)
            f2 = open(exportedFile)
            fn = open(glitchedFile, 'w')

            a = [l for l in f1 if l[0:2] == 'v ']
            random.shuffle(a)

            for l in f2:
                if l[0:2] == 'v ':
                    if random.random() < n:
                        l = a[random.choice(range(len(a)))]

                fn.write(''.join(l))

            f1.close()
            f2.close()
            fn.close()
            importOBJ()
        else:
            pass


    #remove faces
    def removeFaces(n):
        if n != 0:
            exportOBJ()
            f = open(exportedFile)
            fn = open(glitchedFile, 'w')

            for l in f:
                if l[0] == 'f':
                    if random.random() < n:
                        l = ''

                fn.write(''.join(l))

            f.close()
            fn.close()
            importOBJ()
        else:
            pass


    def glitch(n1, n2, n3):
        shuffleVertices(n1)
        randomNumbers(n2)
        removeFaces(n3)


    #the files are saved to the same folder as the blend file
    exportedFile = bpy.path.abspath('//modelExport.obj')
    glitchedFile = bpy.path.abspath('//modelGlitched.obj')


    #the script is only executed when the file is saved
    if bpy.data.is_saved:
        glitch(.1, .1, .1)
    else:
        print('Save the file first!')


#-------------------------------------------------------------------


#addon boiler plate
class GlitchObj(bpy.types.Operator):
    """Glitch an obj file""" #blender will use this as a tooltip for menu items and buttons.
    bl_idname = "script.glitch_obj" #unique identifier for buttons and menu items to reference.
    bl_label = "Glitch Obj" #display name in the interface.
    bl_options = {'REGISTER', 'UNDO'} #enable undo for the operator.

    def execute(self, context): #execute() is called by blender when running the operator.
        # The original script
        myScript()
        return {'FINISHED'} #this lets blender know the operator finished successfully.


def register():
    bpy.utils.register_class(GlitchObj)


def unregister():
    bpy.utils.unregister_class(GlitchObj)


#This allows you to run the script directly from blenders text editor
#to test the addon without having to install it.
if __name__ == "__main__":
    register()