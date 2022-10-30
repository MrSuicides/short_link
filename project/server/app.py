from flask import Flask, render_template

# from models import MongoMethods

# Your API definition
app = Flask(__name__, template_folder='../client/templates')  # , CERF


# db = MongoMethods()


@app.route('/')
def longtask():
    # db.insert('asd', 'dqsd')
    # test = db.collection_count()

    return render_template("index.html")


#host='0.0.0.0'
if __name__ == '__main__':
    app.run()
