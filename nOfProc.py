# version 1.0
# created by Carlo Pasquinucci - carlo.a.pasquinucci@gmail.com
# relesead under license GPL GNU 3

# How to run it: python oOfProc.py numberOfCells  -decomposeFile
# Return: the number of processors required
# Nice to use with checkQualityMesh.py


import sys

"""
narg=len(sys.argv)

if narg!=2:
    print("Number of argument is not 1")
    if narg>2:
        print("Reduce the number of arguments")
    else:
        print("Increase the number of arguments")
    exit()
 """

 cellMesh=float(sys.argv[1])
 nCellsProProcessor=500000
 
nProcessorAux=nCellsProProcessor/cellMesh
nProcessor=int(nProcessorAux)

##Write decomposeParDict file:
if sys.argv[2]==-decomposeFile:
 #check if the system folder exist:
    import os
    if not os.path.exists('my_folder'):
       os.makedirs('my_folder')
    f = open("system/decomposeParDict", "w")
    f.write("numberOfSubdomains "+str(nProcessor)+" ;")
    f.write("method scotch")
    f.close()
