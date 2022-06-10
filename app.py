import flask as f

app = f.Flask(__name__)

@app.route("/")
def yalla():
  return f.render_template("indx.html")


@app.route("/about")
def about():
  return f.render_template("about.html")


@app.route("/gallery")
def gallery():
  return f.render_template("gallery.html")


@app.route("/posts")
def posts():
  return f.render_template("posts.html")
