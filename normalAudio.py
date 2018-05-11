import os
import subprocess

basePath = r"Z:\Temp\DemPower\AudioNormalize\Activities"

#use of * - see Unpacking Argument Lists
#https://goo.gl/F4LpBS
#print(*files, sep='\n')

for fname in os.listdir(basePath):
	inPath = os.path.join(basePath, fname)
	if os.path.isdir(inPath):
        # skip directories
		continue
	outDir = os.path.join(basePath, "out")
	outPath = os.path.join(outDir,fname)
	(dummy, extension) = os.path.splitext(fname)
	if extension.lower() == ".m4a" or extension.lower() == ".mp4":
		##File has aac encoded sound
		encode = "aac"
		myCmd1 =  "ffmpeg-normalize " + inPath + \
            " -c:a aac --normalization-type peak --target-level -1 --output " \
            + outPath
	elif extension.lower() == ".webm":
		##File has vorbis encoded sound
		encode = "vorbis"	
		myCmd1 =  "ffmpeg-normalize " + inPath + \
             " -c:a libvorbis --normalization-type peak --target-level -1 --output " \
             + outPath
	else:
		encode = "unknown extension"	
	print(fname, encode,'\n')
    #p1 = subprocess.Popen(myCmd1, shell=True)
    #p1.wait()


