from flask import Flask, request, redirect, render_template
import html

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/signup', methods=['GET', 'POST'])
def display_user_signup():
    username = ""
    username_error = ""

    password = ""
    password_error = ""

    verify = ""
    verify_error = ""

    email = ""
    email_error = ""  

    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        verify = request.form["verify"]
        email = request.form["email"]

        if not username:
            username_error = "Username cannot be blank"
        elif " " in username:
            username_error = "Username cannot contain spaces"
        elif len(username) < 3 or len(username) > 20:
            username_error = "Username must be between 3 & 20 characters"
        else:
            username_error = ""

        if not password:
            password_error = "Password cannot be blank"
        else:
            password_error = ""
        
        if verify != password:
            verify_error = "Passwords do not match"
        else: verify_error = ""

        if email != "":
            if " " in email:
                email_error = "Email cannot contain spaces"
            elif len(email) < 3 or len(email) > 20:
                email_error = "Email must be between 3 - 20 characters"
            elif "@" not in email or ".com" not in email or ".." in email:
                email_error = "Email not valid"
            else:
                email_error = ""
    
        if not username_error and not password_error and not verify_error and not email_error:
            return render_template("welcome.html", username=username)
        else:
            return render_template('forms.html', username=username, username_error=username_error, password=password, password_error=password_error, verify=verify, verify_error=verify_error, email=email, email_error=email_error)
    else:
        return render_template('forms.html')

@app.route("/welcome", methods=['POST'])
def welcome():
    username = request.form['username']

app.run()