from flask import Flask, render_template, url_for, flash , redirect
from forms import Registration, Login, Trash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ce22a76129e6b25009Trashe5b338f02d35ff'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db '

posts = [
    {
        'author': 'Ash Jagtap',
        'publisher': 'geeta press',
        'dob':'11 feb 2005'
    },
    {
        'author': 'Ashhuuu',
        'publisher': 'nana book wala',
        'dob': '12 January'
    }
]



@app.route('/home')
def home():
    return render_template('home.html', posts=posts, title='ghar se hun bkl')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = Registration()
    if form.validate_on_submit():
        flash(f'registration completed for {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        if form.email.data == 'ashu@gmail.com' and form.password.data == 'lavdekapassword':
            flash(f'you have been logged in by email {form.email.data}', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful, Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/trash')
def trash():
    form = Trash() 
    return render_template('trash.html', title='Trash', form=form)

if __name__ == '__main__':
    app.run(debug=True)
