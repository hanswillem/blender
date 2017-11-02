bl_info = {
    "name": "Glitch OBJ",
    "author": "Hans Willem Gijzel",
    "version": (0, 1),
    "location": "View3D > Tools > Glitch OBJ",
    "category": "Scripts",
}


import bpy
import random


#---the glitch script----------------------------------------------------------------------------------------------------------------------------------------------


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


    #the obj file is saved to and loaded from the temp folder
    exportedFile = bpy.app.tempdir + 'modelExport.obj'
    glitchedFile = bpy.app.tempdir + 'modelGlitched.obj'


    #call the glitch function
    glitch(.1, .1, .1)


#------------------------------------------------------------------------------------------------------------------------------------------------------------------


#boiler plate
class GlitchObjPanel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_context = "objectmode"
    bl_category = "Glitch OBJ" #the name of the tab in the ui
    bl_label = "Glitch OBJ" #label in interface


    def draw(self, context):
        #button 01
        TheCol = self.layout.column(align=True)
        TheCol.operator("script.glitch_obj", text="Glitch!") #the bl_idname of the operator class to execute and the text on the button
    #end draw


class GlitchObjOperator(bpy.types.Operator):
    """Glitch OBJ""" #blender will use this as a tooltip for menu items and buttons
    bl_idname = "script.glitch_obj" #unique identifier for buttons and menu items to reference
    bl_label = "Glitch OBJ" #display name in the interface
    bl_options = {'REGISTER', 'UNDO'}


    def invoke(self, context, event):
        #The actual script to call
        myScript()


        return {'FINISHED'}


def register():
    bpy.utils.register_class(GlitchObjPanel)
    bpy.utils.register_class(GlitchObjOperator)


def unregister():
    bpy.utils.unregister_class(GlitchObjPanel)
    bpy.utils.unregister_class(GlitchObjOperator)


#this allows you to run the script directly from blenders text editor
#to test the addon without having to install it
if __name__ == "__main__":
    register()
