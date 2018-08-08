#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template

from urllib import urlopen
import json

app = Flask(__name__)


def main():
    url = 'https://randomuser.me/api/?results=100'

    def get_people(url):  # get data from url and parse

        response = urlopen(url)
        data = json.loads(response.read())
        people = data['results']

        return people  # [0,1, .., 99] -> dictionary

    class Person:

        def __init__(self, person):
            self.person = person

        # def __repr__(self):
        #   return self.name

        def set_person(self):
            self.name = self.person['name']['first'] + " " + self.person['name']['last']  # fullname
            self.gender = self.person['gender']
            self.email = self.person['email']
            self.phone = self.person['phone']
            self.medium = self.person['picture']['medium']

    people = get_people(url)
    card_list = []

    for i in range(100):
        card = Person(people[i])
        card.set_person()
        card_list.append(card)

    return card_list


users = main()  # card[0].name card[0].gender etc


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', users = users)


'''app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
'''