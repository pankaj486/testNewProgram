#
# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route('/')
# def home():
#     return "Website content is goes here!"
#
# if __name__=="__main__":
#     app.run(debug=True)


# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route('/')
# def home():
#     return "Homepage is here!"
#
# @app.route('/about/')
# def about():
#     return "about content is goes here!"
#
# if __name__=="__main__":
#     app.run(debug=True)


from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")
@app.route("/about/")
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)
