#when executed this script checks the batch_file and starts rendering the first available blend file
#when done it renders the next available blend files
#this script can be executed on multiple machines simultaneously provided that the batch_file and the containing blend files are within reach of those machines


import os
import sys

def main():

    batch_file = 'batch_render.bat'

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
        os.system(picked_file)


if __name__ == '__main__':
    main()
