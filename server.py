import os
import csv
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)
print(__name__)

print("Current working directory:")
print(os.getcwd())

print("Template folder:")
print(app.template_folder)


@app.route("/")
def my_home():
    return render_template("index.html")


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/works.html")
def works():
    return render_template("works.html")


@app.route("/work.html")
def work():
    return render_template("work.html")


@app.route("/contact.html")
def contact():
    return render_template("contact.html")

def write_to_file(data):
    with open('database.txt',mode='a') as database:
        email= data["email"]
        subject= data["subject"]
        message= data["message"]
        file=database.write(f'\n {email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', 'a', newline='') as database2:
        writer = csv.writer(database2)
        writer.writerow([
            data['email'],
            data['subject'],
            data['message']
        ])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect(url_for('thankyou'))

        except:
            return 'Did not store to database!'
    else:
        return 'Something went wrong! Try again!'

    return 'Great, you have submitted your form'



@app.route("/thankyou.html")
def thankyou():
    print("THANK YOU ROUTE REACHED")
    return render_template("thankyou.html")


if __name__ == "__main__":
    app.run(debug=True)
