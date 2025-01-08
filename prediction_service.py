from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__, template_folder="./templates/html/", static_folder="./static/")

def isFileAllowed(filename):
    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

@app.route('/main', methods=['GET'])
def main():
    return render_template('predict.html')

@app.route('/predict', methods=['POST'])
def predictClassForFile():
    if 'image' not in request.files:
        return redirect(url_for('renderError', message="Nie przekazano żadnego pliku"))
    image_file = request.files['image']
    if image_file.filename == '':
        return redirect(url_for('renderError', message="Nazwa pliku jest pusta"))
    if image_file and isFileAllowed(image_file.filename):        
        image_class = "Przykładowa klasa obrazu"
        return redirect(url_for('renderResults', image_class=image_class))
    return redirect(url_for('renderError', message="Niedozwolony format pliku"))

@app.route('/predict/class/<image_class>')
def renderResults(image_class):
    return render_template('results.html', image_class=image_class)

@app.route('/error/<message>')
def renderError(message):
    return render_template('error.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
