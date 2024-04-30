from flask import Flask, render_template , request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_app.db'

db = SQLAlchemy(app)

class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable = False)
    story = db.Column(db.String(10000), nullable = False)

    def __repr__(self):
        return '<Story %r>' % self.id


@app.route('/')
def index():
    data = Story.query.all()
    return render_template("index.html", context=data)




@app.route('/insert_form' , methods = ['GET' , 'POST'])
def insert_form():
    if request.method == 'POST':

        form_name = request.form['name']
        form_story = request.form['story']

        new_story = Story(name = form_name, story = form_story)
        try:
            db.session.add(new_story)
            db.session.commit()

            redirect('/insert_form')

        except:
            return "issue adding your story"
        
    data = "insert text"

    return render_template("insert_form.html", context=data)

@app.route("/contact_me")
def contact_me():
    data = {'Head': 'You are welcome','Name':'Umer Arif', 'Email':'umer.dadabhoy@gmail.com', 'Last':'See Ya'}

    return render_template("contact_me.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)