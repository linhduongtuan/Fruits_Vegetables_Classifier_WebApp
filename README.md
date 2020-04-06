# Fruits_Vegetables_Classifier_WebApp
Recently, we have published a paper "Automated fruit recognition using EfficientNet and MixNet" (https://doi.org/10.1016/j.compag.2020.105326) at Journal Q1: https://www.sciencedirect.com/journal/computers-and-electronics-in-agriculture
You also can find our full paper using sci-hub.tw (https://sci-hub.tw/https://doi.org/10.1016/j.compag.2020.105326)
This is an neural network webapp visualizing the training of the network and testing accuracy of 99.5% accuracy. The neural network uses pretrained EfficientNet_B0 and then trained to classify images of fruits and vegetables. It is built using Pytorch framework using Python as primary language. The webapp is built using flask.

Dataset used :

120 Category Fruits and Vegetables Dataset: you can download the dataset at: Kaggle here: https://www.kaggle.com/moltean/fruits
or github here: https://github.com/Horea94/Fruit-Images-Dataset
The original paper of the dataset is here: https://www.researchgate.net/publication/321475443_Fruit_recognition_from_images_using_deep_learning

Neural Network used :
EfficientNet_B0 is originated at a paper: https://arxiv.org/pdf/1905.11946.pdf
And the code was hacked by Ross Wrightman. Thank Ross for your fantastic work to create a valuable models in PyTorch.
The hacked models by Ross Wrightman can be found here: https://github.com/rwightman/pytorch-image-models & https://github.com/rwightman/gen-efficientnet-pytorch


Flow :
The full code used to train the model can be taken at EfficientNet_B0_SGD.ipynb. So far, the experiments in our paper can also be reproducible by modifying the notebook.
Input image is fed and transformed using : commons.py
Inference is done by : inference.py
Running local web by: fruit_vegetable.py
Complete flow :

Run on Ubuntu 18.04 and MacOS Catanlina, but not test on Windows -

Make sure you have installed Python , Pytorch and flask.

First download all the folders and files
git clone https://github.com/linhduongtuan/Fruits_Vegetables_Classifier_WebApp.git
Then open the command prompt (or powershell) and change the directory to the path where all the files are located.
cd Fruits_Vegetables_Classifier_WebApp
Now run the following commands -
For Windows: set FLASK_APP=Fruits_Vegetables.py
Or for Mac or Ubuntu: export FLASK_APP=Fruits_Vegetables.py
and then:
flask run

This will firstly download the models and then start the local web server.

now go to the local server something like this - http://127.0.0.1:5000/ and see the result and explore.

@creator - Duong Tuan Linh
