# Fruits_Vegetables_Classifier_WebApp
Recently, we published a paper "Automated fruit recognition using EfficientNet and MixNet", can be found here:  https://doi.org/10.1016/j.compag.2020.105326
or https://www.researchgate.net/publication/339798572_Automated_fruit_recognition_using_EfficientNet_and_MixNet

This is an neural network webapp visualizing the training of the network and testing accuracy ~ 99.5% accuracy.
The neural network uses pretrained EfficientNet_B0 and then trained to classify images of fruits and vegetables.
It is built using Pytorch framework using Python as primary language.
The webapp is built using Flask.

## Dataset used :     
120 Category Fruits and Vegetables Dataset can be found here:     

https://www.kaggle.com/moltean/fruits
or https://github.com/Horea94/Fruit-Images-Dataset
And the original paper of the dataset was introduced by Horea Mureșan and Mihai Oltean (https://www.researchgate.net/publication/321475443_Fruit_recognition_from_images_using_deep_learning)
## Neural Network used : 
EfficientNet family was introduced by a paper from Google Brain at https://arxiv.org/pdf/1905.11946.pdf
And codes for the EfficientNet family were hacked by Ross Wrightman. Thank Ross for his fantastic work to create valuable models for image classification tasks on PyTorch. We can find the codes of Ross here: https://github.com/rwightman/pytorch-image-models and https://github.com/rwightman/gen-efficientnet-pytorch
* You can download the trained weight of EfficientNet_B0 model [here](https://github.com/linhduongtuan/Fruits_Vegetables_Classifier_WebApp/blob/master/release/EfficientNet_B0_SGD.pth)    

       

## Flow:
* to reproduce our experiments in our paper, you can use [EfficientNet_B0_SGD.ipynb] (https://github.com/linhduongtuan/Fruits_Vegetables_Classifier_WebApp/blob/master/EfficientNet_B0_SGD.ipynb)
* Input image is fed and transformed using : [commons.py](https://github.com/linhduongtuan/Fruits_Vegetables_Classifier_WebApp/blob/master/commons.py)     
* Inference is done by : [inference.py](https://github.com/linhduongtuan/Fruits_Vegetables_Classifier_WebApp/blob/master/inference.py) 
* Run on local web: [app.py] (https://github.com/linhduongtuan/Fruits_Vegetables_Classifier_WebApp/blob/master/app.py) 

## Run on Ubuntu and MacOS, but not test on Windows - 
Make sure you have installed Python , Pytorch, Flask and other related packages, refer requirement.txt.

* _First download all the folders and files_     
`git clone https://github.com/linhduongtuan/Fruits_Vegetables_Classifier_WebApp.git`     
* _Then open the command prompt (or powershell) and change the directory to the path where all the files are located._       
`cd Fruits_Vegetable_Classifier_WebApp`      
* _Now run the following commands_ -        

`python app.py`     


This will firstly download the models and then start the local web server.

now go to the local server something like this - http://127.0.0.1:5000/ and see the result and explore.

## How to cite
If you find our work useful for your research, please cite the paper using the following BibTex entry:
### BibTex
```
@article{DUONG2020105326,
title = "Automated fruit recognition using EfficientNet and MixNet",
journal = "Computers and Electronics in Agriculture",
volume = "171",
pages = "105326",
year = "2020",
issn = "0168-1699",
doi = "https://doi.org/10.1016/j.compag.2020.105326",
url = "http://www.sciencedirect.com/science/article/pii/S0168169919319787",
author = "Linh T. Duong and Phuong T. Nguyen and Claudio {Di Sipio} and Davide {Di Ruscio}",
abstract = "The classification of fruits offers many useful applications in daily life, such as automated harvesting or building up stocks for supermarkets. Studies have been proposed to classify fruits from input images, exploiting image processing and machine learning techniques. Though a lot of improvements have been achieved in recent years, many approaches still suffer prolonged training/testing time, or a considerably high number of false positives. For several applications, it is crucial to provide users with not only precise but also real-time recommendations. In this paper, we propose a practical solution to fruit recognition by exploiting two recently-developed classifiers that have demonstrated themselves to be both effective and efficient. We adopted EfficientNet and MixNet, two families of deep neural networks to build an expert system being able to accurately and swiftly identify fruits. Such a system can be deployed onto devices with limited computational resources to prompt exact and timely recommendations. The approach’s performance has been validated on a real dataset consisting of 48,905 images for training and 16,421 images for testing. The experimental results showed that the application of EfficientNet and MixNet on the considered dataset substantially improves the overall prediction accuracy in comparison to a well-established baseline."
} 

```


### @creator - Duong Tuan Linh
