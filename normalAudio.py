import os

inDir = r"Z:\Temp\DemPower\AudioNormalize"
outDir = r"Z:\Temp\DemPower\AudioNormalize\out"
files = os.listdir(inDir)

#use of * - see Unpacking Argument Lists
#https://goo.gl/F4LpBS
#print(*files, sep='\n')

for file in files:
    inFile = os.path.join(inDir,file)
    outFile = os.path.join(outDir,file)
    myCmd =  "ffmpeg-normalize " + inFile + " -c:a aac --normalization-type peak --target-level -1 --output " + outFile
    print(myCmd + '\n')


