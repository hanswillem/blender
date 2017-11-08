#batch render all .blend files in current folder
#
#install on windows:
#------------------
#copy brender.py to the programs folder (or any other folder you like)
#add '.py' to PATHEXT in Extension Variables
#add brender to path in Extension variables
#add Blender to PATH in Extension variables
#restart windows
#------------------
#use on windows:
#------------------
#in command prompt navigate to folder with .blend files
#type 'brender' to start batch render


import os
import sys


def main():
    #variables
    folder = os.getcwd()
    blend_files = []

    #make a list of all .blend files
    for i in os.listdir(folder):
        if i.endswith('.blend'):
            blend_files.append(i)

    if len(blend_files) == 0:
        print('No blend files found!')
        sys.exit()

    #make a .bat file to enable batch rendering
    f = open('batch_render.bat', 'w')
    for i in blend_files:
        render_string = 'blender -b "' + os.path.join(folder, i) + '" -x 1 -a' + '\n'
        f.write(render_string)
    f.close()

    #start the rendering
    print('Starting render...')
    os.system('batch_render.bat')

    print('Batch render done')


if __name__ == '__main__':
    main()
