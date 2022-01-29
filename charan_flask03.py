from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    posts = [{'title':'bolero','author':'mahindra'},{'title':'CBR','author':'honda'}]
    return render_template('base.html',author='bob', x='5263', y='SRAVYA IS A GOOD GIRL', sunny=False)


if __name__ == '__main__':
    app.run(debug=True)