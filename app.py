from flask import Flask, render_template

# This is the app per se. The blueprints, which are like mini-apps, include the controllers
# for each class/table.

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True) 