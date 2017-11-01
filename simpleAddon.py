bl_info = {
    "name": "My Script",
    "category": "Scripts",
}


import bpy


def myScript():
    print("Hello world!")


# boiler plate

class myClass(bpy.types.Operator):
    """My Script that just says hello"""      # blender will use this as a tooltip for menu items and buttons.
    bl_idname = "script.hello"                # unique identifier for buttons and menu items to reference.
    bl_label = "My Script"                    # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}         # enable undo for the operator.

    def execute(self, context):               # execute() is called by blender when running the operator.

        # The original script
        myScript()

        return {'FINISHED'}                   # this lets blender know the operator finished successfully.

def register():
    bpy.utils.register_class(myClass)


def unregister():
    bpy.utils.unregister_class(myClass)


# This allows you to run the script directly from blenders text editor
# to test the addon without having to install it.
if __name__ == "__main__":
    register()
