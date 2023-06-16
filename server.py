from flask import Flask, redirect,render_template, request
import dojo
import ninja
app = Flask(__name__)

@app.route('/')
def index():
    return redirect ('/dojos')


@app.route('/dojos')
def dojo_dashboard():
    dojos = dojo.Dojo.get_all_dojos()
    return render_template('dojo_dashboard.html', all_dojos = dojos)

@app.route('/create/new_dojo',methods=['POST'])
def create():
    print(request.form)
    dojo.Dojo.save(request.form)
    return redirect('/dojos')


@app.route('/dojo/show/<int:dojo_id>')
def dojo_show(dojo_id):
    dojos =dojo.Dojo.get_one(dojo_id)
    ninjas = ninja.Ninja.get_all_ninjas_from_dojo(dojo_id)
    return render_template('dojo_show.html', dojo=dojos, all_ninjas = ninjas)

@app.route('/ninjas')
def new_ninja():
    dojos = dojo.Dojo.get_all_dojos()
    return render_template("new_ninja.html", dojos= dojos)

@app.route("/ninjas", methods =['POST'])
def created_ninja():
    ninja.Ninja.save(request.form)
    return redirect (f"/dojo/show/{request.form['dojo_id']}")


if __name__ == "__main__":
    app.run(debug=True)

