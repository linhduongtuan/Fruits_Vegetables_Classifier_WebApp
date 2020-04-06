import json
from commons import get_tensor, get_model
with open('/Users/mac/Downloads/Fruits_Classifier_Webapp/cat_to_name.json') as f:
	cat_to_name = json.load(f)
with open('//Users/mac/Downloads/Fruits_Classifier_Webapp/class_to_idx.json') as f:
	class_to_idx = json.load(f)

idx_to_class = {v:k for k, v in class_to_idx.items()}
	
model = get_model()

def get_fruit_name(image_bytes):
	tensor = get_tensor(image_bytes)
	outputs = model(tensor)
	_, prediction = outputs.max(1)
	category = prediction.item()
	class_idx = idx_to_class[category]
	fruit_name = cat_to_name[class_idx]
	return category, fruit_name
