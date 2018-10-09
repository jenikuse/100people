#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from urllib import request
import json

app = Flask(__name__)


def main():
    n = 100
    url = "https://randomuser.me/api/?results={}".format(n)

    def get_people(url):  # get data from url and parse
        response = request.urlopen(url)
        data = json.loads(response.read())
        return data['results']  # [0, 1, .., 99] -> dictionary

    
    class Person:
        
        def __init__(self, person):
            self.person = person
            
        def set_person(self):
            self.name = self.person['name']['first'] + " " + self.person['name']['last']
            self.gender = self.person['gender']
            self.email = self.person['email']
            self.phone = self.person['phone']
            self.medium = self.person['picture']['medium']

            
    people = get_people(url)
    
    card_list = []
    for i in range(n):
        card = Person(people[i])
        card.set_person()
        card_list.append(card)

    return card_list


users = main()  # card[n].name card[n].gender etc


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', users = users)
