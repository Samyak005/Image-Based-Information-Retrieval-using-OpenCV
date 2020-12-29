from files.colordescriptor import ColorDescriptor
import glob
import cv2
 
# this file performs feature extraction for all the images in  images folder and writes them into index.csv 

cd = ColorDescriptor((8, 12, 3))
output = open("index.csv", "w")  # w refers to write mode
 
for imagePath in glob.glob("static/images/*"):  # loops over every image in images folder
	imageID = imagePath[imagePath.rfind("/") + 1:]
	image = cv2.imread(imagePath)
 
	features = cd.describe(image) # this returns the features 
 
	features = [str(f) for f in features]  # features converted individually to string for join operation in next line 
	output.write("%s,%s\n" % (imageID, ",".join(features)))
 
output.close()