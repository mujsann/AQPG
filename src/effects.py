import spacy
from src.helpers import Helpers
from src.data.entities import *

nlp = spacy.load("en_core_web_lg")
VERB = "VERB"
space = " "

class Effects:

    def __init__(self):
        self.player_name = player_name

    # save the segment number and the pobjs
    # returns effect of subseg and count of effects.py in the sub_seg
    def get_dob_effect(self, subsegment):
        global eff
        player_name = self.player_name
        #     doc = doc.lower()
        doc = nlp(subsegment[1])

        pobjs = []
        act_pobjs = []
        for token in doc:
            if token.dep_ is 'pobj' or token.dep_ is 'dobj' or token.dep_ is 'nsubj':
                pobjs.append([token, token.i])
        # print(pobjs)
        for token in doc:
            if token.dep_ is "nsubj" and token.text == player_name and token.head.pos_ is "VERB":
                action = token.head
                index = action.i
                get_pobj = [[action, pobj[0]] for pobj in pobjs if index < pobj[1]]

                if get_pobj:
                    act_pobjs.append(get_pobj[0])
        # print(act_pobjs)

        if act_pobjs:
            for act in act_pobjs:
                if str(subsegment[0]) == str(act[0]):
                    eff = act
                    # print(eff)

            effect = Helpers.get_past(str(eff[0])) + space + Helpers.label(Helpers.ent_value(eff[1]))
            return (effect)
        return "none"

    def get_obj(self, subsegment):
        #     doc = doc.lower()
        doc = nlp(subsegment[1])
        player_name = self.player_name

        pobjs = []
        act_pobjs = []
        for token in doc:
            if token.dep_ is 'pobj' or token.dep_ is 'dobj' or token.dep_ is 'nsubj':
                pobjs.append([token, token.i])

        for token in doc:
            if token.dep_ is "nsubj" and token.text == player_name and token.head.pos is VERB:
                action = token.head
                index = action.i
                get_pobj = [[action, pobj[0]] for pobj in pobjs if index < pobj[1]]

                if get_pobj:
                    act_pobjs.append(get_pobj[0])

        if act_pobjs:
            for act in act_pobjs:
                if str(subsegment[0]) == str(act[0]):
                    eff = act

            objct = eff[1]
            return (objct)
        return ("none")

    #    print(effect)

    # get_dob_effect(subsegments[1])

    def get_pred_entities (self, subsegments):
        sents = subsegments
        player_actions = []
        pred_entities = []  # entities that will be used as predicates
        acts_params = []
        for i, subseg in enumerate(sents):
            subseg = nlp(subseg)
            for token in subseg:
                #         rule 1
                if token.dep_ is "nsubj" and token.text == player_name and token.head.pos is VERB:
                    action = token.head
                    a = [child for child in action.children if child.dep_ is "prep"]
                    if (len(a)):
                        parent = a[0]
                        b = [chil for chil in parent.children if chil.dep_ == 'pobj']
                        if len(b):
                            acts_params.append([player_name, str(token.head), b[0], i, ])
                            if Helpers.ent_value(b[0]):
                                e = str(Helpers.ent_value(b[0]))
                                pred_entities.append([Helpers.get_past(str(token.head)), Helpers.label(e)])

                    c = [child for child in action.children if child.dep_ == 'dobj']
                    if (len(c) and Helpers.ent_value(c[0])):
                        acts_params.append([player_name, str(token.head), c[0], i, ])
                        player_actions.append(str(token.head))
                        if Helpers.ent_value(c):
                            e = str(Helpers.ent_value(c[0]))
                            pred_entities.append([Helpers.get_past(str(token.head)), Helpers.label(e)])

                if token.dep_ == "advcl":
                    for child in token.children:
                        for entity in Entities:
                            if entity == str(child):
                                if (Helpers.ent_value(entity)):
                                    acts_params.append([player_name, str(token), entity, i])
                                    player_actions.append(str(token))
                                    if Helpers.ent_value(entity):
                                        e = str(Helpers.ent_value(entity))
                                        pred_entities.append([Helpers.get_past(token.text), Helpers.label(e)])
                                    break;

        # len(acts_params)
        return (pred_entities)

  

    def alt_effects(self, eff, params, subsegments):  # eff is the segment's direct effect e.g read ?inf
        pred_entities = self.get_pred_entities(subsegments)
        for alt in pred_entities:
            chosen_alt = None
            if eff.find(str(alt[0])) > -1:  # find the action in the direct effect
                chosen_alt = alt
                if (chosen_alt != None):  # check if the param is part of the params in the same action
                    params = str(" ".join(params))
                    if (params.find(chosen_alt[1]) > -1):
                        effect = "(" + chosen_alt[0] + space + chosen_alt[1] + ")"
                        return effect

        return None

    def get_effects(self, eff, params, subsegments):
        states = []
        #     check if the effect contains the player name (?pla)
        # check if the effect contains ?non
        # check if the effect contains "none"
        # check if the obj is one of the params
        a = eff.lower().find("?pla")
        b = eff.lower().find("?non")
        c = eff.lower().find("none")
        # if it does search the alternative effects.py .
        if a > -1 or b > -1 or c > -1:
            effect = self.alt_effects(eff, params, subsegments)
            # save to states
            states.append(effect)
            # print(effect)
            return effect

        effect = "(" + str(eff) + ")"
        states.append(effect)
        # print(effect)
        return effect

