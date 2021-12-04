from flask import Flask, render_template, redirect

app = Flask(__name__)	

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/days/')
def days():
        return render_template('days.html')
	
	
if __name__ == '__main__':
	app.run(debug=True, port=5000) # host="0.0.0.0"
