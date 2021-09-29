import cv2
import os
 		
#return rois of the images
def return_roi(img_file):
	#get rois from screen and mouse:
	img = cv2.imread(img_file)
	roi = cv2.selectROI(img)
	cv2.destroyAllWindows()
	return roi

def cut_images(images_path):
	#path = "/home/sujan/Pictures/test/"
	folder_name = images_path.split('/')[-2]
	new_folder_name = folder_name + "_cut"
	path_parent = images_path + "../"
	dest_path = path_parent + new_folder_name + "/"
	if not os.path.isdir(path_parent + new_folder_name):
		os.mkdir(path_parent + new_folder_name)
	else:
		print("folder already exists")
		input("Do you want to continue..?")

	images = [img for img in os.listdir(images_path)]
	x, y, w, h = return_roi(images_path + images[0])
	print(x, y, w, h)


	for i, image in enumerate(images):
		print(image)
		 
		extension = image.split(".")[-1]
		img = cv2.imread(images_path + image)
		crop_img = img[y:y+h, x:x+w]
		cv2.imwrite(dest_path + new_folder_name + str(i) + "." + extension, crop_img)
		 



 

if __name__ == '__main__':
	#images_path = "/home/sujan/Pictures/test/"
	while True:
		images_path = input("Enter image path:")
		cut_images(images_path)