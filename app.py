from flask import Flask, render_template, request, redirect
import model

app = Flask(__name__)


@app.route("/")
def index():
    ## print the guestbook
    return render_template("index.html", entries=model.get_entries())

@app.route("/add")
def addentry():
    ## add a guestbook entry
    return render_template("addentry.html")

@app.route("/postentry", methods=["POST"])
def postentry():
    name = request.form["name"]
    message = request.form["message"]
    model.add_entry(name, message)
    return redirect("/")

# defining a new route that will allow us to delete items from the guestbook
# same as the homepage (route /), but had an 'x' underneath each post to delete it
@app.route('/admin')
def admin():
    #print('123')
    return render_template('admin.html', entries=model.get_entries()) # return the template we want; using the same model to handle data

# method to handle the delete action, not adding a post
@app.route("/delete", methods=["POST"])
def delete():
    id_num = request.form['id']
    button = request.form['delete']
    name = request.form["name"]
    message = request.form["message"]
    model.delete_entry()
    return render_template('admin.html', entries=model.get_entries())
    #return redirect('/')


if __name__=="__main__":
    model.init()
    app.run(debug=True)
