bl_info = {
    "name": "My Script",
    "author": "Hans Willem Gijzel",
    "version": (1, 0),
    "location": "View3D > Tools > Scripts",
    "category": "Scripts",
}


import bpy


#------------------------------------------------------------------------------------------------------------------------------------------------------


#the actual script to execute when the button is pressed
def myScript():
    print("Hello world!")


#------------------------------------------------------------------------------------------------------------------------------------------------------


#boiler plate
class myScriptPanel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_context = "objectmode"
    bl_category = "My Scripts" #the name of the tab in the ui
    bl_label = "Execute My Script" #label in interface


    def draw(self, context):
        #button 01
        TheCol = self.layout.column(align=True)
        TheCol.operator("script.hello_world", text="Say hello") #the operator class to execute and the text on the button
    #end draw


class MyScriptOperator(bpy.types.Operator):
    """My Script that just says hello""" #blender will use this as a tooltip for menu items and buttons
    bl_idname = "script.hello_world" #unique identifier for buttons and menu items to reference
    bl_label = "My Script" #display name in the interface
    bl_options = {'REGISTER', 'UNDO'}


    def invoke(self, context, event):
        #The actual script to call
        myScript()


        return {'FINISHED'}


def register():
    bpy.utils.register_class(MyScriptOperator)
    bpy.utils.register_class(myScriptPanel)


def unregister():
    bpy.utils.unregister_class(MyScriptOperator)
    bpy.utils.unregister_class(myScriptPanel)


#this allows you to run the script directly from blenders text editor
#to test the addon without having to install it
if __name__ == "__main__":
    register()
