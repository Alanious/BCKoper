from flask import Flask, render_template, request, flash
from forms import ContactForm
from flask_mail import Message, Mail

mail = Mail()

app = Flask(__name__)

app.secret_key = 'development key'

app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'mail.sarafina.eu',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'shop@sarafina.eu',
    MAIL_PASSWORD = 'K0per2021!',
))

mail.init_app(app)


@app.route("/")
def index():
    return render_template("index1.html")

@app.route("/about")
def about_us():
    return render_template("about.html")

@app.route("/Senior")
def senior_team():
    return render_template("Senior.html")

@app.route("/news")
def young_team():
    return render_template("news.html")

@app.route("/youngster")
def youngster():
    return render_template("youngster.html")

@app.route("/newster")
def newster():
    return render_template("newster.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()

  if request.method == 'POST':
    if form.validate() == False:
      flash('Vsa polja je potrebno izpolniti.')
      return render_template('contact.html', form=form)
    else:
      msg = Message(form.subject.data, sender='bck.novi.clani@gmail.com', recipients=['shop@sarafina.eu'])
      msg.body = """
      Ime otroka: %s (%s)
      Šola, ki jo obiskuje: %s
      Razred, ki ga obiskuje: %s
      Ime in priimek staršev: %s
      Email staršev: %s 
      Telefon staršev: %s 
      Dodatna vprašanja: %s
            """ % (form.name.data, form.birth.data, form.school.data, form.year.data, form.names.data, form.email.data, form.phone.data, form.message.data)
      mail.send(msg)

      return render_template('contact.html', success=True)

  elif request.method == 'GET':
    return render_template('contact.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)