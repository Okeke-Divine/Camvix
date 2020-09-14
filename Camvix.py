# ============================ Dependetied ==============
from PIL import Image, ImageTk
import time
#===============================================
video = cv2.VideoCapture(0)
while True:
	isTrue,frame = video.read()
	cv2.imshow("Skiy - Camera - 10 Second(s)", frame)
	key = cv2.waitKey(10)
	if key == ord('q'):
		cv2.imwrite('skiy-pic.jpg',frame)


video.release()