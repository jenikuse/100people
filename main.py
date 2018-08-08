#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib, json

class Person:

    def __init__(self, count):
        self.count = count

    def get_people(self): #get data from url and parse

        url = 'https://randomuser.me/api/?results=100'
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        people = data['results']

        return people    #[0,1, .., 99] -> dictionary

    people = get_people()

    def set_person(self, people, count):

        person = {}
        person['name'] = people[count]['name']['first'] + " " + people[count]['name']['last'] #fullname
        person['gender'] = people[count]['gender']
        person['email'] = people[count]['email']
        person['phone'] = people[count]['phone']
        person['medium'] = people[count]['picture']['medium']


instancelist = [Person(i) for i in range(100)]
print instancelist[0]




#def filter_people(people):
#    d1 = people[0]['gender']









# from flask import Flask, redirect, url_for, request
#r = request()
#data = r.json()
#print(data)
'''app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"
    #return r
if __name__ == "__main__":
    app.run()
'''