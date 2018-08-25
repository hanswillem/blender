# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


bl_info = {
    'name' : 'My Add-on',
    'author' : 'Hans Willem Gijzel',
    'version' : (1, 0),
    'blender' : (2, 79),
    'location' : 'View 3D > Tools > My Add-on',
    'description' : 'This is a template for a basic add-on.',
    'warning' : '',
    'wiki_url' : '',
    'category' : 'A Category'
    }


import bpy

def sayHello():
    print('Hello world!')


#panel class
class MyPanel(bpy.types.Panel):

    #panel attributes
    """My Add-on Panel Class"""
    bl_label = 'My Panel Label'
    bl_idname = 'tools_my_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'My Add-on'

    #draw loop
    def draw(self, context):
        layout = self.layout
        layout.label('Some text')
        col = layout.column(align = True)
        col.operator('script.operator_say_hello', text = 'Say hello')


#operator class
class MyOperator(bpy.types.Operator):

    #operator attributes
    """My Add-on Operator Class"""
    bl_label = 'My Operator'
    bl_idname = 'script.operator_say_hello'
    bl_options = {'REGISTER', 'UNDO'}

    #poll - if the poll function returns False, the button will be greyed out
    @classmethod
    def poll(cls, context):
        return 2 > 1

    #execute
    def execute(self, context):
        sayHello()

        return {'FINISHED'}


#registration
def register():
    bpy.utils.register_class(MyPanel)
    bpy.utils.register_class(MyOperator)



def unregister():
    bpy.utils.unregister_class(MyPanel)
    bpy.utils.unregister_class(MyOperator)



#enable to test the addon by running this script
if __name__ == '__main__':
    register()
