from flask import Flask, request, render_template, redirect, url_for
from model_wrapper import ModelWrapper

app = Flask(__name__, template_folder="templates/html", static_folder="static")

model_wrapper = ModelWrapper("trained_model.pt")


def isFileAllowed(filename):
    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

@app.route('/main', methods=['GET'])
def main():
    return render_template('detect.html')

@app.route('/detect', methods=['POST'])
def predictClassForFile():
    if 'image' not in request.files:
        return redirect(url_for('renderError', message="Nie przekazano żadnego pliku"))
    image_file = request.files['image']
    if image_file.filename == '':
        return redirect(url_for('renderError', message="Nazwa pliku jest pusta"))
    if image_file and isFileAllowed(image_file.filename):
        model_wrapper.predict(image_file)
        return redirect(url_for('renderResults', image_filename=f"result_{image_file.filename}"))
    return redirect(url_for('renderError', message="Niedozwolony format pliku"))

@app.route('/detect/<image_filename>')
def renderResults(image_filename):
    image_url = url_for('static', filename=f'results/{image_filename}')
    return render_template('results.html', image_url=image_url)

@app.route('/error/<message>')
def renderError(message):
    return render_template('error.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
