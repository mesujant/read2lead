import cv2
import os

def blur_faces(images_path):
	# bat.jpg is the batman image.
	images = [img for img in os.listdir(images_path)]


	for image in images:
		img = images_path + image
		img = cv2.imread(img)
		

	   
	# make sure that you have saved it in the same folder
	# Averaging
	# You can change the kernel size as you want


		#create frame with frame size:

		avging = cv2.blur(img,(10,10))
		gausBlur = cv2.GaussianBlur(img, (5,5),0)
		medBlur = cv2.medianBlur(img,5)
		bilFilter = cv2.bilateralFilter(img,9,75,75)

		while True:

			cv2.imshow('Averaging' + image, avging)
			cv2.waitKey(0)
			  
			# Gaussian Blurring
			# Again, you can change the kernel size
			#gausBlur = cv2.GaussianBlur(img, (5,5),0) 
			cv2.imshow('Gaussian Blurring'+ image, gausBlur)
			#cv2.waitKey(0)
			  
			# Median blurring
			#medBlur = cv2.medianBlur(img,5)
			#cv2.imshow('Media Blurring', medBlur)
			#cv2.waitKey(0)
			  
			# Bilateral Filtering
			#bilFilter = cv2.bilateralFilter(img,9,75,75)
			cv2.imshow('Bilateral Filtering' + image, bilFilter)
			#cv2.waitKey(0)

			key == cv2.waitKey(0)

			if key == ord('q'):
				break
		cv2.destroyAllWindows()


class verifyPhoto:
	def __init__():
		pass

	#verify of any specific type and convert if not:
	def verify_type():
		pass

	def adjust_type():
		pass


	def check_if_face_found():
		pass


	 

class verify_document:
	#lowest level: document type, if document may content valid content:
	#highest level: content checking
	def __init__():
		pass


	def verify_type():
		pass

 




if __name__ == '__main__':
	images_path = "/home/sujan/Documents/read2lead/python/verify document/sample images/"
	blur_faces(images_path)

	#verify_photo(img_photo)
	#verify_document(img_doc)
