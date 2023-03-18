
# Chess Pieces Detection System

This model is for people who are still learning chess and doesn't know which piece is what called like and let them track chess board while playing in real time

I used yolov7 pretrained algorithm, trained it on images of my chess board that I have annotated and passed through roboflow that automatically splited data into 70 % train 20% validation 10% test. I did training in Google colab with 1000 epochs and 16 batchsize. Finally I created script detection.py that detects pieces in real time from your primary webcam connected to PC using OpenCV
## Screenshots


![alt text](https://github.com/Wachu2005/Chess-Pieces-Detection-System/blob/master/Readme%20images/Chesspiecesdetection.jpg)

![alt text](https://github.com/Wachu2005/Chess-Pieces-Detection-System/blob/master/Readme%20images/Chesspiecesdetection2.jpg)

![alt text](https://github.com/Wachu2005/Chess-Pieces-Detection-System/blob/master/Readme%20images/Images-7b3404ea-b5e6-11ed-9ed5-b42e99eb25df_jpg.rf.dcdb9c3461c9dcb0e068bea9ac1f230a.jpg)


## Tech Stack

Python,
OpenCV,
Roboflow,
PyTorch,
Numpy,
Google colab,
Jupyter Notebook


