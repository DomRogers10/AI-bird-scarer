# AI Bird Scarer

An AI project aimed to detect and scare birds automatically using a raspberry pi and the CV2 camera module.
Plenty of birdscarers already exist, but these are almost always manually operated, or occur at regular intervals. Either way, they are time consuming and wasteful, so why not automate it using AI?

The project uses a convolutional neural network to identify birds in real time, initiating a number of outputs from the pi to scare it away.
I used Tensorflow to train the model on Google Colab, before loading and running the model on the Pi. The training data consisted of these [60,000 images from Kaggle](https://www.kaggle.com/datasets/gpiosenka/100-bird-species)

The "scaring" features consist of:

*An alarm system triggered remotely on a nearby bluetooth speaker (for models RPi 3 onwards)*

*A motorized, rotating arm*
