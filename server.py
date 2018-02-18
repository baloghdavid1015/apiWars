from flask import Flask, render_template, redirect, request, url_for
import requests
import util
import data_handler
app = Flask(__name__)

@app.route("/")
def main_page():
    response = requests.get('https://swapi.co/api/planets').json()
    planets = response['results']
    headers = ["Name", "Diameter", "Climate", "Terrain", "Surface Water Percentage", "Population", "Residents", ""]
    print(planets)
    return render_template("main_page.html", planets=planets, headers=headers)


@app.route("/registration")
def registration():
    return render_template("registration.html")


@app.route("/registration", methods=['POST'])
def save_user():
    sent_data = request.form

    new_data = {
        'user_name': sent_data['user_name'],
        'password': util.hash_password(sent_data['password']),
    }
    insert_data = data_handler.add_new_user(
        new_data['user_name'],
        new_data['password']
    )

    registration_time = 0
    error_handler = 1
    print(insert_data[registration_time])
    if insert_data[error_handler] == -1:
        return render_template('registration.html', error=True)

    return redirect('/')


if __name__ == "__main__":
    app.run(
        port=3000,
        debug=True
    )

