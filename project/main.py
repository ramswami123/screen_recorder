from codecs import Codec
import pyautogui
import cv2
import numpy as np

#specifying quality of recording
resolution =(1920,1080)


#assigning video code
# @return a fourcc code
Codec= cv2.VideoWriter_fourcc(*"XVID")
# This static method constructs the fourcc code of the 
# codec to be used in the constructor VideoWriter::VideoWriter or VideoWriter::open


#addressing output file
file_name="recording.avi"

#speacifying frame rate 
frame_rate=60.0

#creating a videowriter object
out=cv2.VideoWriter(file_name,Codec,frame_rate,resolution)


#now creating pop-up window for viewing real time recording
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)# creates an empty window
#speacifing size of window
cv2.resizeWindow("Live",420,270)

#lets strat recording our screen 
#we wiil be running infinite loop
#in every instance we will take screen shot
#write to output file using --video writter
while True:
    image=pyautogui.screenshot()#screenshot of screen
    frame=np.array(image) #converts the screen shot into numpy array
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    #write it to frame /adding frame to output file
    out.write(frame)
    
    #displaying the recording screen
    cv2.imshow('LIVE',frame)
    
    #assiging s key bar to stop recording
    if cv2.waitKey(1)==ord('s'):break


#relasing the video writter
out.release()

#to close entire programme
cv2.destroyAllWindows()