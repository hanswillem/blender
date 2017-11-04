bl_info = {
    'name' : 'My Addon',
    'author' : 'Hans Willem Gijzel',
    'version' : (1, 0),
    'blender' : (2, 79),
    'location' : 'View 3D > Tools > My Addon',
    'description' : 'Says hello',
    'warning' : '',
    'wiki_url' : '',
    'category' : 'My Addon Category'
    }


#imports
import bpy


#panel class
class MyPanel(bpy.types.Panel):
    
    #panel attributes
    """What does this panel do?"""
    bl_label = 'My Panel Label'
    bl_idname = 'tools_my_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'My Addon'
    
    #draw loop
    def draw(self, context):
        layout = self.layout
        layout.label('My Label')
        layout.operator('script.my_operator', text="Say Hello!")


#operator class
class MyOperator(bpy.types.Operator):
    
    #operator attributes
    """What does this operator do?"""
    bl_label = 'My Operator'
    bl_idname = 'script.my_operator'
    bl_options = {'REGISTER', 'UNDO'}

    #execute
    def execute(self, context):
        print('Hello world!')
        
        return {'FINISHED'}
    
        
#registration
def register():
    bpy.utils.register_class(MyPanel)
    bpy.utils.register_class(MyOperator)
    

def unregister():
    bpy.utils.register_class(MyPanel)
    bpy.utils.register_class(MyOperator)


#enable to test the addon by running this script
if __name__ == '__main__':
    register()
