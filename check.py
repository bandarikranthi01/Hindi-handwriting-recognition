from keras.preprocessing.image import img_to_array
import tensorflow as tf
from keras.models import load_model
import numpy as np
import argparse
import imutils
import cv2
import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd

from gtts import gTTS
from playsound import  playsound

labels = [u'\u091E', u'\u091F', u'\u0920', u'\u0921',u'\u0922',u'\u0923',u'\u0924',u'\u0925',u'\u0926',u'\u0927',u'\u0915',u'\u0928',u'\u092A',u'\u092B',u'\u092c',u'\u092d',u'\u092e',u'\u092f',u'\u0930',u'\u0932',u'\u0935',u'\u0916',u'\u0936',u'\u0937',u'\u0938',u'\u0939','क्ष','त्र','ज्ञ',u'\u0917',u'\u0918',u'\u0919',u'\u091a',u'\u091b',u'\u091c',u'\u091d',u'\u0966',u'\u0967',u'\u0968',u'\u0969',u'\u096a',u'\u096b',u'\u096c',u'\u096d',u'\u096e',u'\u096f']

import numpy as np
from keras.preprocessing import image
from tkinter import filedialog as fd

print("[INFO] loading network...")
#filename = fd.askopenfilename()
test_image = cv2.imread(filename)
image = cv2.resize(test_image, (32, 32))
image = image.astype("float") / 255.0
image = img_to_array(image)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = np.expand_dims(image, axis=0)
image = np.expand_dims(image, axis=3)
model = tf.keras.models.load_model("C:/Users/banda/PycharmProjects/Hindi-OCR-master/HindiModel3.h5")
lists = model.predict(image)[0]
print("The letter is ", labels[np.argmax(lists)]," ")


mytext= labels[np.argmax(lists)]
language='hi'
myobj=gTTS(text=mytext,lang=language,slow=False)
myobj.save("sound.mp3")
playsound("sound.mp3")
'''
import pyttsx3;
engine = pyttsx3.init()
engine.say(labels[np.argmax(lists)])
engine.runAndWait()
voices = engine.getProperty('voices')
#engine.setProperty('voice', voice.id)
'''