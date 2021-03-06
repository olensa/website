from flask import Flask, render_template, request, flash
from forms import ContactForm
from flask_mail import Mail, Message
import emails


mail = Mail() 

app = Flask(__name__)
app.secret_key = emails.KEY

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = emails.MYEMAIL
app.config["MAIL_PASSWORD"] = emails.EMAIL
 
mail.init_app(app)

@app.route('/')
def visitka():
    return render_template('visitka.html')

@app.route('/spock')
def spock():
    return render_template('spock.html')


@app.route('/contact', methods=['GET','POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            msg = Message(form.subject.data, sender='lenaglotova21@gmail.com', recipients=['lenaglotova21@gmail.com'])
            msg.body = """
            From: %s <%s>
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
            return render_template('contact.html', success=True)  
    elif request.method == 'GET':
        return render_template('contact.html', form=form)
 

if __name__== '__main__':
    app.run(debug=True)