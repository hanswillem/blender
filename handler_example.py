#the myFunction function updates everytime when there is a frame change.

def myFunction(scene):
    print(scene.frame_current)

bpy.app.handlers.frame_change_pre.clear() #clear the handler list, otherwise it keeps the previous added handler
bpy.app.handlers.frame_change_pre.append(myFunction)
