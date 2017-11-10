#when executed this script checks the batch_file and starts rendering the first available blend file
#when done, it renders the next available blend file until there are no available files left
#this script can be executed on multiple machines simultaneously provided that the batch_file and the containing blend files are within reach of those machines
#also blender must be installed in the same directory on all machines


import sys
import subprocess


def main():
    print('starting script...')

    batch_file = 'P:/_blender_batch_render/batch_render.bat'

    while True:

        #pick first available file
        f = open(batch_file, 'r')
        picked_file = None
        for i in f:
            print()
            if not i[:2] == '//':
                picked_file = i
                break
        f.close()

        if picked_file == None:
            print('no more files to render')
            sys.exit()

        #add prefix to line
        f = open(batch_file, 'r')
        l = []
        for i in f:
            if i == picked_file:
                i = '//' + picked_file
            l.append(i)
        f.close()

        #save .bat file
        f = open(batch_file, 'w')
        for i in l:
            f.write(i)
        f.close()

        #start render
        subprocess.call(picked_file, shell = True)


if __name__ == '__main__':
    main()
