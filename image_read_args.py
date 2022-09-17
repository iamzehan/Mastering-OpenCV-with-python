import argparse
import cv2 
parser = argparse.ArgumentParser()
parser.add_argument("path_image", help="path to input image to be displayed")
args = parser.parse_args()
image = cv2.imread(args.path_image)
args = vars(parser.parse_args())
image2=cv2.imread(args['path_image'])
cv2.imshow("Loaded image 1",image)
cv2.imshow("Loaded image 2",image2)