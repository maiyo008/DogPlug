#!/usr/bin/python3
""" Starts a Flask Web Application"""
from models import storage
from models.service import Service
from models.groomer import Groomer
from models.owner import Owner
from models.dog import Dog
from os import environ
from flask import Flask, render_template, request
app = Flask(__name__)

owner_id = ""

@app.teardown_appcontext
def close_db(error):
    """ Remove current SQLAlchemy session"""
    storage.close()


@app.route('/', strict_slashes=False)
def index():
    return render_template('index.html')


@app.route('/dogProfile', strict_slashes=False)
def dogProfile():
    return render_template('profile.html')

@app.route('/form', methods=['POST'])
def form():
    params_owner = {}
    params_dog = {}

    owner_name = request.form.get("owner_name")
    email = request.form.get("email")
    contact = request.form.get("contact")

    params_owner["name"] = owner_name
    params_owner["email"] = email
    params_owner["contact"] = contact

    owner_obj = Owner(**params_owner)
    owner_id = owner_obj.id
    owner_obj.save()

    dog_name = request.form.get("dog_name")
    breed = request.form.get("breed")
    weight = request.form.get("weight")
    age = request.form.get("age")
    params_dog["name"] = dog_name
    params_dog["breed"] = breed
    params_dog["weight"] = weight
    params_dog["age"] = age
    params_dog["owner_id"] = owner_id

    dog_obj = Dog(**params_dog)
    dog_obj.save()
    
    return render_template('form.html')

@app.route('/search_groomers', methods=['POST'], strict_slashes=False)
def search_groomers():
    """ Searches for groomers by location"""
    location = request.form.get("location")
    groomers = storage.search_groomer(location)
   
    return render_template('groomer.html', groomers=groomers)

@app.route('/groomers', strict_slashes=False)
def groomer():
    groomers = storage.groomer_location()
    return  render_template(
        'groomer.html',
        groomers=groomers
    )



@app.route('/dogplug_services', strict_slashes=False)
def dogplug_services():
    """ Dogplug services"""
    services = storage.all(Service).values()
    services = sorted(services, key=lambda k: k.description)
    
    return render_template(
        'dogplug_services.html',
        services=services
    )


@app.route('/dog_profile', methods=['GET', 'POST'], strict_slashes=False)
def dog_profile():
    """ Create a dog profile """
    if request.method == "POST":
        owner_name = request.form["owner"]
        email = request.form["email"]
        contact = request.form["contact"]

        print("{}{}{}".format(owner_name, email, contact))
    return render_template('profile.html')



if __name__ == "__main__":
    """ Main function"""
    app.run(host='0.0.0.0', port=5000)
