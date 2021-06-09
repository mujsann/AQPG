# Extraction from subsegmentation
import spacy
import random

from src.helpers import Helpers
from src.effects import Effects
from src.data.entities import *
from src.files_creator import *

nlp = spacy.load("en_core_web_lg")
VERB = "VERB"
space = ' '


class Extraction:

    def __init__(self, all_subsegments):
        self.all_subsegments = all_subsegments
        self.ext_subsegments = ' '
        # input story
        # output subsegments = [action, subsegment, entities, parameters]
        # take sentences where the player is performing actions
        # save the action, the sentence, the entities and their parameters

    def extract(self):
        subsegments = []
        for sent in self.all_subsegments:
            for token in nlp(sent):
                if token.dep_ is "nsubj" and token.text == player_name and token.head.pos_ is "VERB":
                    # get parameters and entity preconditions
                    # if token.dep_ is "nsubj" and token.text == player_name:
                    param_ents = []
                    r_entities = []
                    params = []
                    ent_preconds = []
                    for entity in Entities:
                        e = str(sent).find(entity.lower())
                        if e > -1:
                            param_ents.append(entity)
                            r_entities.append(Entities[entity])
                            params.append(Helpers.label(Entities[entity]))
                            ent_preconds.append(Entities[entity] + space + Helpers.label(Entities[entity]))
                    s = [token.head, sent, param_ents, r_entities, params, ent_preconds]
                    subsegments.append(s)

        # for i, subsegment in enumerate (subsegments):
        #     effects = Effects.get_dob_effect(subsegment)
        #     subsegments[i].append(effects)

        for s in subsegments:
            a = Effects().get_dob_effect(s)
            if a:
                s.insert(2, a)
        self.ext_subsegments = subsegments

        for s in subsegments:
            print(s, "\n", "\n")
        # print(subsegments)

    def get_preconditions(self, precos):
        preconditions = ""
        pars = {}
        for p in precos:
            param = p[p.find(' '):]
            b4_param = p[:p.find(' ')]
            if param in pars:
                pars[param] += 1
                preconditions += "(" + b4_param + param + str(pars[param]) + ")" + space
            else:
                pars[param] = 0
                #             print(pars)
                preconditions += "(" + b4_param + param + ")" + space
        return preconditions

    def get_parameters(self, params):  # adds one to param count
        parameters = "("
        pars = {}
        for p in params:
            if p in pars:
                pars[p] += 1
                parameters += p + str(pars[p]) + space
            else:
                pars[p] = 0
                parameters += p + space

        return parameters + " "

    def get_operators(self):
        subsegments = self.ext_subsegments
        operators = "(:functions" + "\n" + "(total-cost))\n \n"
        for subsegment in subsegments:
            a = Effects().get_effects(subsegment[2], self.get_parameters(subsegment[-2]), self.all_subsegments)
            if (a != None):
                operators += ("(:action " + Helpers.lemmat(str(subsegment[0])) + "\n  " +
                              ":parameters " + self.get_parameters(subsegment[-2]) + ")" + "\n  " +
                              ":precondition (and " + self.get_preconditions(subsegment[-1]) + ")" + "\n" +
                              ":effect (and " + Effects().get_effects(subsegment[2], subsegment[-2],
                                                                      self.all_subsegments) + " (increase (total-cost) " + str(
                            Helpers.random_cost('x')) + ")))" + "\n"
                              ) + "\n"

        return operators

    # predicates
    def param_preds(self):
        predicates = []
        for segment in self.ext_subsegments:
            preds = segment[-1]
            for pred in preds:
                predicates.append("(" + pred + ")")
        predicates = Helpers.unduplicate(predicates)
        return predicates

    def state_preds(self, subsegments):
        # get state preds from alt effects
        state_preds = []
        for subsegment in subsegments:
            state = Effects().get_effects(subsegment[2], self.get_parameters(subsegment[-2]), self.all_subsegments)
            # print(state)
            state_preds.append(state)
        state_preds = Helpers.unduplicate(state_preds)
        state_preds.remove(None)
        # print(state_preds)
        return state_preds

    def get_all_preds(self, subsegments):
        # param_preds(subsegments)
        all_preds = self.param_preds() + self.state_preds(self.ext_subsegments)
        return all_preds

    def get_predicates(self, preds):
        predicates = ""
        for pred in preds:
            predicates += pred + "\n"

        return ("(define (domain " + storyname + "land)" + "\n" +
                "(:requirements :action-costs)" + "\n" +
                "(:predicates" + "\n" +
                predicates + ")")

    # => change entities here, puth hyphen for the ones that have space
    def init_objects(self):
        initial_objects = []
        objects = ""
        for entity in Entities:
            if entity.lower() != player_name:
                initial_objects.append(entity.replace(" ", "-").lower())
        initial_objects = Helpers.unduplicate(initial_objects)
        for obj in initial_objects:
            objects += obj + " "
        return ("(define (problem " + player_name + ")" + "\n" +
                "(:domain " + storyname + "land)" + "\n" +
                "(:objects you " + objects + ") \n")

    def initial_state(self):
        init_state = ""
        inits = []
        for entity in Entities:
            if entity.lower() != player_name:
                inits.append(
                    "(" + Entities[entity].replace(" ", "-").lower() + space + entity.replace(" ", "-").lower() + ")")
        inits = Helpers.unduplicate(inits)
        for init in inits:
            init_state += init + "\n"
        return ("(:init (player you) \n" + "(= (total-cost) 0) \n" + init_state + ")\n")

    def goal_objects(self):
        goal_objects = []
        for entity in Entities:
            goal_objects.append([entity, Helpers.label(Entities[entity])])
        # print(goal_objects)
        return goal_objects

    def gobj(self):
        go = self.goal_objects()
        random.shuffle(go)
        return go

    def get_goals(self):
        goals = []
        ext_subsegments = self.ext_subsegments
        state_preds = self.state_preds(ext_subsegments)
        for i in range(1, 6):
            no = random.randint(0, len(state_preds) - 1)
            sp = state_preds[no]
            labl = sp[sp.find(" "):-1]
            act = sp[1:sp.find("?") - 1]
            for s in self.gobj():
                new_s = " ".join(s)
                s_labl = new_s[new_s.find("?") - 1:]
                if str(s_labl) == str(labl):
                    obj = new_s[:new_s.find(labl)]
                    actobj = "(" + act + space + obj.replace(" ", "-") + ")"
                    goals.append(actobj)
                    break;

        goals = Helpers.unduplicate(goals)
        # print(goals)
        g = ""
        for goal in goals:
            g += goal.lower() + " "
        return ("(:goal (and " + g + "))\n" +
                "(:metric minimize (total-cost))")

    def create(self):
        self.extract()

        init_objects = self.init_objects()
        init_state = self.initial_state()
        goals = self.get_goals()
        make_problem(init_objects, init_state, goals)

        predicates = self.get_predicates(self.get_all_preds(self.ext_subsegments))
        operators = self.get_operators()
        make_domain(predicates, operators)
