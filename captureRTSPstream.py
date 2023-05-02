# RTSP image Data capturing code 


#necessary Libraries
import cv2
import os
import time
import datetime


#amount of time desired between each image captured from RTSP stream
imagecapturetime = 1
# enterfolder path of where images should be saved
dir_path = ''
#enter the RTSP URL here
RTSP_URL = ''
number_of_images = 100
os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp'
last_recorded_time = time.time()
cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)
#display error if RTSP stream cannot be opened
if not cap.isOpened():
    print('Cannot open RTSP stream')
    exit(-1)
n_delta = number_of_images
n_start = 0

#displays the number of images already present in folder
for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path,path)):
        n_start += 1
print(n_start)
n=n_start 
while True:
    
    
    _, frame = cap.read()
    #display RTSP stream in window while capturing images
    cv2.imshow('RTSP stream', frame)
    curr_time = time.time()
    if curr_time - last_recorded_time >= imagecapturetime:
        #
        n=n+1
        realtime= datetime.datetime.now()
        #add timestampStr to image name if you would like timestamped images
        timestampStr = realtime.strftime("%d-%b-%Y (%H:%M:%S.%f)")
        #writes image and numbers it in order of images taken in folder
        cv2.imwrite(os.path.join(dir_path , f'{n}.png'), frame)
        
       
        last_recorded_time = curr_time
    if cv2.waitKey(1) == 27:
        break
    if n >= n_start+n_delta:
        break
#close everything after capturing
cap.release()
cv2.destroyAllWindows()
