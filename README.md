
# Chess Pieces Detection System

This model is for people who are still learning chess and doesn't know which piece is what called like.

I used yolov7 pretrained algorithm, trained it on images of my chess board that I have annotated and passed through roboflow that automatically splited data into 70 % train 20% validation 10% test. I did training in Google colab with 1000 epochs and 16 batchsize.
Finally I created script detection.py that detects pieces in real time from your primary webcam connected to PC using OpenCV
## Demo




## Screenshots


![alt text](https://github.com/Wachu2005/Chess-Pieces-Detection-System/blob/master/Readme%20images/Chesspiecesdetection.jpg)