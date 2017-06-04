#!/usr/bin/env python3
# coder: wang.rui

""" server. """

from flask import Flask, jsonify, abort, request, make_response, render_template, redirect

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

class Question(db.Model):
    type = db.Column(db.String, primary_key=True)
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    analysis = db.Column(db.String)
    choice_0 = db.Column(db.String, nullable=False)
    choice_1 = db.Column(db.String, nullable=False)
    choice_2 = db.Column(db.String)
    choice_3 = db.Column(db.String)
    answer = db.Column(db.String, nullable=False)

    def make_dict(self):
        question = {}
        question["type"] = self.type
        question["id"] = self.id
        question["description"] = self.description
        question["analysis"] = self.analysis
        question["choices"] = []
        for choice in [self.choice_0, self.choice_1, self.choice_2, self.choice_3]:
            if (choice is not None) and (choice != ""):
                question["choices"].append(choice)
        question["answer"] = "ABCD"[self.answer]
        return question








@app.route("/")
def index():
    return render_template('1.html')

@app.route("/index&id=1")
def index_1():
    return render_template('index.html')
@app.route("/index&id=2")
def index_2():
    return render_template('index.html')
@app.route("/index&id=3")
def index_3():
    return render_template('index.html')
@app.route("/index&id=4")
def index_4():
    return render_template('index.html')
@app.route("/index&id=5")
def index_5():
    return render_template('index.html')






@app.route("/video&id=1")
def video_1():
    return render_template('video.html')
@app.route("/video&id=2")
def video_2():
    return render_template('video.html')
@app.route("/video&id=3")
def video_3():
    return render_template('video.html')
@app.route("/video&id=4")
def video_4():
    return render_template('video.html')
@app.route("/video&id=5")
def video_5():
    return render_template('video.html')

@app.route("/choose")
def choose():
    return render_template('2.html')

@app.route("/test&id=1")
def test1():
    return render_template('3.html')
@app.route("/test&id=2")
def test2():
    return render_template('3.html')
@app.route("/test&id=3")
def test3():
    return render_template('3.html')



@app.route("/word&id=1")
def word1():
    return render_template('word1.html')
@app.route("/word&id=2")
def word2():
    return render_template('word2.html')
@app.route("/word&id=3")
def word3():
    return render_template('word3.html')
@app.route("/word&id=4")
def word4():
    return render_template('word4.html')
@app.route("/word&id=5")
def word5():
    return render_template('word5.html')




@app.route("/done1")
def done1():
    return redirect('/static/video/1.mp4')

@app.route("/done2")
def done2():
    return redirect('/static/video/2.mp4')


@app.route("/done3")
def done3():
    return redirect('/static/video/3.mp4')


@app.route("/done4")
def done4():
    return redirect('/static/video/4.mp4')



@app.route("/done5")
def done5():
    return redirect('/static/video/5.mp4')









@app.route("/question_info", methods=["GET"])
def question_statis_info():
    info = {}
    for info_t in db.session.query(Question.type, db.func.count(Question.id)).group_by(Question.type).all():
        info[info_t[0]] = info_t[1]
    return jsonify(info)

@app.route("/question", methods=["POST"])
def find_question():
    try:
        question_type = request.form["question_type"]
        question_id = int(request.form["question_id"])
    except ValueError:
        abort(400)
    return_data = {"status":"ok"}

    if question_type not in ["AccidentHandling", "BasicSafe", "BiomaterialSafe", "InstrumentSafe", "ReagentSafe"]:
        return jsonify({'status':'error', "message":"{} is not vaild type".format(question_type)}), 400

    question = Question.query.filter_by(id=question_id, type=question_type).first()
    if question is not None:
        return_data["question"] = question.make_dict()
        return jsonify(return_data)
    else:
        return jsonify({'status':'error', 'message':"invalid id."})

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'status':"error", "message":"Bad Request!"}), 400)

if __name__ == '__main__':
    app.run(
        threaded = True,
        port = 5045

    )
