from flask import Flask, render_template,request, redirect # 変更
from flask_sqlalchemy import SQLAlchemy # 追加

app = Flask(__name__)
@app.route("/")
def index():
    tasks = Todo.query.all()
    return render_template("index.html", tasks=tasks)


@app.route("/create", methods=["POST"])
def create():
    title = request.form.get("title")
    details = request.form.get("details")
    new_task = Todo(title=title, details=details)
    db.session.add(new_task)
    db.session.commit()
    return redirect("/")

  

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
db = SQLAlchemy(app)
class Todo(db.Model):
 id = db.Column(db.Integer, primary_key=True)
 title = db.Column(db.String(100))
 details = db.Column(db.String(100))

@app.route("/delete/<int:id>")
def delete(id):
   delete_task = Todo.query.get(id)
   db.session.delete(delete_task)
   db.session.commit()
   return redirect("/")

@app.route("/update/<int:id>")
def updata(id):
    task = Todo.query.get(id)
    return render_template("update.html", task=task)



@app.route("/change/<int:id>", methods=["POST"])
def change(id):
    task = Todo.query.get(id)
    title = request.form.get("title")
    details = request.form.get("details")
    task.title = title
    task.details = details
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
   app.run(debug=True)