"""Test app to make sure that flask is working correctly.
"""

from flask import Flask, render_template, request, redirect
app = Flask(__name__)       # new Flask object


@app.route("/")
def hello():
    author = "Me"
    name = "You"
    return render_template('test_index.html', author=author, name=name)


@app.route('/test_signup', methods=['POST'])
def report_signup():
    print('Signup detected for ' + request.form['email'])
    return redirect('/')


if __name__ == "__main__":
    app.run()