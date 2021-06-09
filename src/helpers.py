##helpers
import os
import spacy
import random
import pandas as pd

dir_path = os.path.dirname(os.path.realpath(__file__))
nlp = spacy.load("en_core_web_lg")
VERB = "VERB"
verbs_data = pd.read_csv(dir_path+"/data/verb.csv")
verbs = verbs_data.copy()
verbs = verbs[['convolute', 'convoluted']]
space = ' '

from src.data.entities import Entities

class Helpers:

    def __init__(self):
        self.story = 'verb'

    # random cost
    def random_cost(x):
        return random.randint(1, 4)
        # print(random_cost())

    # lemmatizes
    def lemmat(action):
        action = nlp(action)
        for token in action:
            return token.lemma_
            break;



    # turns entities into predicate labels
    def label(entity):
        return "?" + str(entity)[:3]

    # remove duplicate from list
    def unduplicate(arr):
        arr = list(dict.fromkeys(arr))
        return arr

    # get past
    def get_past(action):
        act = Helpers.lemmat(action)
        verb = verbs.loc[verbs['convolute'] == act]

        try:
            return verb.convoluted.values[0]
        except:
            return action

    # function to check if word is among the entities
    def isEntity(word):
        re = False
        for entity in Entities:
            if entity is str(word):
                re = True
                break;
        return re

    # returns entity label
    def ent_value(ent):
        ent = str(ent).lower()
        value = None
        for entity in Entities:
            if entity.lower() == ent:
                value = Entities[entity]
                break
        return value




