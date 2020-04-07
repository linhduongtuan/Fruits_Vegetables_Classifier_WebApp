import json
import torch.nn.functional as F
#from commons import get_model, get_tensor
import torch
import io
import torch.nn as nn
from PIL import Image
import torchvision.transforms as transforms
from timm import create_model
from commons import get_model, get_tensor
import numpy as np
with open('cat_to_name.json') as f:
    cat_to_name = json.load(f)
with open('class_to_idx.json') as f:
    class_to_idx = json.load(f)
with open('Fruits_Classifier_Webapp/labels.txt', 'r') as f:
    classes = f.readline()
    
model = get_model()
 
model.eval()

def get_fruit_probability(all_probabilities):
    probs = all_probabilities.data.numpy()[0]
    probs.tolist()
    return probs
    
def get_fruit_name(image_bytes):
    fruit_names = []
    tensor = get_tensor(image_bytes)
    outputs = model.forward(tensor)
    
    # Probs
    probs = F.softmax(outputs, dim=1)
      
    # Top probs
    top_probs, top_labs = probs.topk(k=5)
    top_probs = top_probs.detach().numpy().tolist()[0]
    top_labs = top_labs.detach().numpy().tolist()[0]
      
    # Convert indices to classes
    idx_to_class = {val: key for key, val in class_to_idx.items()}
    top_labels = [idx_to_class[lab] for lab in top_labs]
    top_fruits = [cat_to_name[idx_to_class[lab]] for lab in top_labs]
    return top_probs, top_labels, top_fruits
    
