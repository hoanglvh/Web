from flask import Flask, request, render_template
from flask_mail import Mail, Message
app = Flask(__name__, template_folder='views')

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'hoanglvh2814@gmail.com'
app.config['MAIL_PASSWORD'] = 'Phongphuhome@2018'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
@app.route('/gmail')
def index():
    return render_template('gmail/index.html')

@app.route('/gmail', methods=['post'])
def sendmail():
    msg = Message('Hello', sender = 'hoanglvh2814@gmail.com', recipients = [request.form.get('email')])
    msg.body = 'Hello Mail'
    mail.send(msg)
    return 'ok'
app.run(debug=True)