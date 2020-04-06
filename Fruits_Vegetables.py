from flask import Flask, render_template, request
from inference import get_fruit_name


app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def hello_world():
	if request.method == 'GET':
		return render_template('index.html',name = "Linh")
	if request.method == 'POST':
		print(request.files)
		if 'file' not in request.files:
			print('file not uploaded , please try again')
			return
		file = request.files['file']
		image = file.read()
		category,fruit_name = get_fruit_name(image_bytes=image)
		return render_template('result.html',fruit = fruit_name, category = category)


