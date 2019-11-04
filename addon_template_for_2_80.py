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


#setup some global scene properties
bpy.types.Scene.my_prop_slider = bpy.props.FloatProperty(min=-1, max=1, name='Slider')
bpy.types.Scene.my_prop_value = bpy.props.IntProperty(name='Value')
bpy.types.Scene.my_prop_toggle = bpy.props.BoolProperty(name='Toggle')


#set the properties (you don't have to do this)
bpy.context.scene.my_prop_slider = 0
bpy.context.scene.my_prop_value = 0
bpy.context.scene.my_prop_toggle = False


#the main function
def main():
    print('Hello world!')
    print('Slider: ' + str(bpy.context.scene.my_prop_slider))
    print('Value: ' + str(bpy.context.scene.my_prop_value))
    print('Toggle: ' + str(bpy.context.scene.my_prop_toggle))


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
        col = layout.column(align = True)
        col.operator('script.myoperator', text='Say Hello!')
        col.prop(context.scene, 'my_prop_slider', slider=True)
        col.prop(context.scene, 'my_prop_value')
        col.prop(context.scene, 'my_prop_toggle')
        
        
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
