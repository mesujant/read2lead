import cv2
import os

#generate blur face of sample photo
def blur_faces(images_path):
	# bat.jpg is the batman image.
	images = [img for img in os.listdir(images_path)]
	new_folder_name = "Blur Face"


	folder_name = images_path.split('/')[-2]
	new_folder_name = folder_name + "_cut"
	path_parent = images_path + "../"
	dest_path = path_parent + new_folder_name + "/"
	if not os.path.isdir(path_parent + new_folder_name):
		os.mkdir(path_parent + new_folder_name)
	else:
		print("folder already exists")
		input("Do you want to continue..?")



	for image in images:
		img_name, extension = image.split(".")
		new_img_name = img_name + "_blur" + "." + extension
		img = images_path + image
		img = cv2.imread(img)

		avging = cv2.blur(img,(10,10))
		gausBlur = cv2.GaussianBlur(img, (5,5),0)
		medBlur = cv2.medianBlur(img,5)
		bilFilter = cv2.bilateralFilter(img,9,75,75)

		blur_images = [avging, gausBlur, medBlur, bilFilter]
		 

		for i, blur_img in enumerate(blur_images):
			cv2.imwrite(dest_path + image + str(i) + "." + extension, blur_img )
		print("images blured")
		input()

def test():
	#check harcascade in web cam:
		 
class verifyPhoto:
	def __init__(self):
		pass

	#verify of any specific type and convert if not:
	def verify_type():
		pass

	def adjust_type():
		pass

	#check if face found
	#cant find the face yet
	def check_if_face_found(self, img_path):
		img = cv2.imread(img_path, cv2.)
		face_cascade_path = os.getcwd() + "/harcascade/harcascade_frontal_alt.xml"
		face_cascade = cv2.CascadeClassifier(face_cascade_path)
		faces = face_cascade.detectMultiScale(img, 1.1, 2)
		print(faces)
		print(len(faces))
		input()
		return len(faces) > 0
		


	 

class verify_document:
	#lowest level: document type, if document may content valid content:
	#highest level: content checking
	def __init__():
		pass


	def verify_type():
		pass

 




if __name__ == '__main__':
	images_path = "/home/sujan/Documents/read2lead/python/verify document/sample images/"
	#blur_faces(images_path)
	images= os.listdir(images_path)

	v1 = verifyPhoto()
	for img in images:
		print(img)
		v1.check_if_face_found(images_path + img[0])
		input()

	#verify_photo(img_photo)
	#verify_document(img_doc)
