from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    items = ["T-rex", "Stegosaurus", "Triceratops"]
    return render_template('index.html', name="Niels", age=31, items = items )

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)