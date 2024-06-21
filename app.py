from flask import Flask, request, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/flask_db"
mongo = PyMongo(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.form['content']
        degree = request.form['degree']
        mongo.db.todos.insert_one({'content': content, 'degree': degree})
        return redirect(url_for('index'))

    todos = mongo.db.todos.find()
    return render_template('index.html', todos=todos)

if __name__ == '__main__':
    app.run(debug=True)