#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib import urlopen
import json

url = 'https://randomuser.me/api/?results=100'

def get_people(url):  # get data from url and parse

    response = urlopen(url)
    data = json.loads(response.read())
    people = data['results']

    return people  # [0,1, .., 99] -> dictionary

people = get_people(url)

class Person:


    def __init__(self, person):
        self.person = person


    def set_person(self, person):
        person_dict = {}
        person_dict['name'] = person['name']['first'] + " " + person['name']['last'] #fullname
        person_dict['gender'] = person['gender']
        person_dict['email'] = person['email']
        person_dict['phone'] = person['phone']
        person_dict['medium'] = person['picture']['medium']
        #return person_dict

        print(person_dict)

instancelist = []

for i in range(10):
     card = Person(people[i])
     card.set_person(people[i])
     print (card)

#print instancelist









# from flask import Flask, redirect, url_for, request

'''app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"
    #return r
if __name__ == "__main__":
    app.run()
'''