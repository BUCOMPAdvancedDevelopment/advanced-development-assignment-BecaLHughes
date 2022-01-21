import logging
import requests
from flask import Flask, render_template,request

app = Flask(__name__)
@app.route('/')
@app.route('/home')
def home():
 return render_template('home.html')
@app.route('/about')
def about():
 return render_template('about.html')
@app.route('/register')
def form():
 return render_template('register.html')
# [END form]
# [START submitted]
@app.route('/submitted', methods=['POST'])
def submitted_form():
 name = request.form['name']
 email = request.form['email']
 password = request.form['password']
 confirm_password = request.form['confirm_password']
# form error handling
 if password != confirm_password:
     return render_template('register.html',
     error="Your passwords do not match. Please try again.")
 if len(password) < 8:
     return render_template('register.html',
     error="Your password needs to be at least 8 characters long." )
 if name is None or not name or email is None:
     return render_template('register.html',
     error="Please fill in all boxes." )
 # [END submitted]
 # [START render_template]
 return render_template(
 'submitted_form.html',
 name=name,
 email=email,
 password=password,
 confirm_password=confirm_password) 
 # [END render_template]
@app.errorhandler(500)
def server_error(e):
 # Log the error and stacktrace.
 logging.exception('An error occurred during a request.')
 return 'An internal error occurred.', 500
@app.errorhandler(404)
def page_not_found(error):
 return render_template('404.html'), 404
if __name__ == '__main__':
 # Only run for local development.
 app.run(host='127.0.0.1', port=8080, debug=True)
@app.route('/productoverview')
def productoverview():
 return render_template('productoverview.html')
 
#login
@app.route('/login')
def login():
 return render_template('login.html')
 
@app.route('/account', methods=['POST'])
def account():
 username = request.form['username']
 password = request.form['password']
 return render_template(
 'account.html',
 username=username,
 password=password)

#contact page
@app.route('/contact')
def contact():
 return render_template('contact.html')

#mongodb
@app.route("/basket", methods=["GET"]) 
def mesh_mongo():
 url= "https://europe-west2-ad-assignment-337410.cloudfunctions.net/Service_Mesh_Layer_Function"
 req = requests.post(url, json={
 "source": "mongo",
 }, headers={"Content-type": "application/json", "Accept": "text/plain"})
 return(req.content)

@app.route("/google", methods=["GET"])
def mesh_google():
 url= "https://europe-west2-ad-assignment-337410.cloudfunctions.net/Service_Mesh_Layer_Function"
 req = requests.post(url, json={
 "source": "google",
 }, headers={"Content-type": "application/json", "Accept": "text/plain"})
 return(req.content)