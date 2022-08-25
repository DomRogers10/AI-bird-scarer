import tensorflow as tf
import numpy as np
import cv2
import time
import matplotlib.pyplot as plt
import os
import time
import queue
import threading

model = tf.keras.models.load_model("Large_data_set_classifier.h5")
count = 0
print(os.getcwd())
os.chdir("/home/domrogers64bit/Python_Files")
print(os.getcwd())

class VideoCapture:
    def __init__(self, name):
        self.cap = cv2.VideoCapture(name)
        self.q = queue.Queue()
        t = threading.Thread(target=self._reader)
        t.daemon = True
        t.start()
    
    def _reader(self):
        while True:
            ret, img = self.cap.read()
            if not ret:
                break
            if not self.q.empty():
                try:
                    self.q.get_nowait()
                except queue.Empty:
                    pass
            self.q.put(img)
    
    def read(self):
        return self.q.get()

cap = VideoCapture(0)
birds = 0

while True:
    try:
        img = cap.read()
        
        #img = cv2.flip(img, 0)
        original = img[::]
        img = np.array(tf.image.resize(img,(256,256))).astype(int)
        img = img.reshape((1,256,256,3))/255
        #print(count)
        #count += 1
        prediction = model.predict(img, verbose=False)[0][0]
        print(prediction)
        if prediction < 0.7:
            count += 1
            if count >= 3:          
                os.system("paplay alarm.wav")
                plt.imsave(f"image{birds}.jpg", original)
                birds += 1
                
        else:
            count = 0
    except Exception as e:
        print(e)
        break
