# emojify-Alok
Emotion Detection using cnn and opencv and deep learning

### Packages need to be installed
- pip install numpy
- pip install opencv-python
- pip install keras
- pip3 install --upgrade tensorflow
- pip install pillow
- install for all requirements -->pip install -r requirements.txt

### download FER2013 dataset
- from below link and put in data folder under your project directory
- https://www.kaggle.com/msambare/fer2013

### Train Emotion detector
- with all face expression images in the FER2013 Dataset
- command --> python TrainEmotionDetector.py
- command for run the main code for activate camera for emotion detection -->python TestEmotionDetector.py

It will take several hours depends on your processor. (On i7 processor with 16 GB RAM it took me around 4 hours)
after Training , you will find the trained model structure and weights are stored in your project directory.
emotion_model.json
emotion_model.h5
