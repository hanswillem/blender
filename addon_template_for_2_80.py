bl_info = {
    'name' : 'My Addon',
    'author' : 'Hans Willem Gijzel',
    'version' : (1, 0),
    'blender' : (2, 80, 0  ),
    'location' : 'View 3D > Tools > My Addon',
    'description' : 'Says hello',
    'warning' : '',
    'wiki_url' : '',
    'category' : 'My Add-on Category'
    }


#imports
import bpy


#the main function
def main():
    print('Hello world!')


#panel class
class MYPANEL_PT_Panel(bpy.types.Panel):
    #panel attributes
    """Tooltip"""
    bl_label = 'My Panel Label'
    bl_idname = 'MYPANEL_PT_Panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'My Addon'
    
    #draw loop
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator('script.myoperator', text = 'Say Hello!')
        

#operator class
class MYOPERATOR_OT_Operator(bpy.types.Operator):
    #operator attributes
    """Tooltip"""
    bl_label = 'My Operator Label'
    bl_idname = 'script.myoperator'
    
    #poll - if the poll function returns False, the button will be greyed out
    @classmethod
    def poll(cls, context):
        return 2 > 1
    
    #execute
    def execute(self, context):
        main()
        return {'FINISHED'}
    
        
#registration
classes = (
    MYPANEL_PT_Panel,
    MYOPERATOR_OT_Operator,
)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)



#enable to test the addon by running this script
if __name__ == '__main__':
    register()
