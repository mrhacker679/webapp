from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__, template_folder='templates')
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'username'
app.config['MAIL_PASSWORD'] = 'password'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    sender = request.form['sender']
    recipients = request.form['recipients'].split(',')
    subject = request.form['subject']
    message = request.form['message']

    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = message

    mail.send(msg)
    return 'Email sent!'

if __name__ == '__main__':
    app.run(debug=True)
