from collections import Counter

import spacy
from src.helpers import Helpers
from src.effects import Effects


class Segmentation:


    def __init__(self, story, entities):
        self.story = story
        self.entities = entities

    def subsegmentation(self, segments, player_name):

        nlp = spacy.load("en_core_web_lg")
        story = nlp(self.story.lower())
        player_name = player_name.lower()
        # append segment number to the  action of the player
        # so that we can know which segments the action belongs to
        # load segments
        all_segments = [nlp(segment) for segment in segments]
        all_subsegments = []
        all_actions = {}
        all_actionss = []
        lemma_actionss = []
        objects = []
        for count, segment in enumerate(segments):
            # print(count, segment)
            segment = nlp(segment)
            actions = []

            action = ''

            for token in segment:
                if token.dep_ is "nsubj" and token.text == player_name and token.head.pos_ == "VERB" :
                    act = [token.head.text, token.i]
                    actions.append(act)

                    all_actions[count] = actions
                    all_actionss.append([count, token.head.text])

                    action = token.head.text
                    act_obj = Effects().get_obj([action, str(segment)])
                    objects.append(act_obj)


        for i, actions in enumerate(all_actionss):
            action = actions[1]  # current action
            act_segment = str(all_segments[actions[0]])  # segment containing the action
            if (i < len(all_actionss) - 1):
                nxtaction = all_actionss[i + 1]  # next action
                # find location of the current action
                act_loc = act_segment.find(action)
                # reverse the segment
                begtoact = act_segment[:act_loc]
                # find where the player is mentioned last between the beginnig and the action
                r_player = player_name[::-1]
                player_loc = len(begtoact) - begtoact[::-1].find(r_player) - len(player_name)
                #       the last name where the player is mentioned before the action
                if (act_segment[act_loc:].find('.') > -1):
                    nxt_stop = len(act_segment[:act_loc]) + act_segment[act_loc:].find('.') + 1
                    print(i, act_segment[player_loc:nxt_stop], "\n")
                    all_subsegments.append(act_segment[player_loc:nxt_stop])
                else:
                    print(i, act_segment[player_loc:], "\n")
                    all_subsegments.append(act_segment[player_loc:])



            else:
                act_loc = act_segment.find(action)

                begtoact = act_segment[:act_loc]
                # find where the player is mentioned last between the beginnig and the action
                r_player = player_name[::-1]
                player_loc = len(begtoact) - begtoact[::-1].find(r_player) - len(player_name)
                #         print(act_segment[player_loc:])
                #       the last name where the player is mentioned before the action
                #         print(len(act_segment),len(act_segment[act_loc:]) )
                if (act_segment[act_loc:].find('.') > -1):
                    nxt_stop = len(act_segment[:act_loc]) + act_segment[act_loc:].find('.') + 1
                    print(i, act_segment[player_loc:nxt_stop], "\n")
                    all_subsegments.append(act_segment[player_loc:nxt_stop])
                else:
                    print(i, act_segment[player_loc:], "\n")
                    all_subsegments.append(act_segment[player_loc:])

        return all_subsegments

    def segmentation(self, story, entities):
        monitor = 0
        seg_length = 0
        segments = list()

        #  identify location points
        locations = []
        for entity in entities:
            if entities[entity] == 'location':
                locations.append(entity)

        locations_no = {}

        # Get number of every location
        for location in locations:
            loc_no = story.find(location)
            if loc_no is not  -1:
                locations_no[location] = loc_no



        # sort location by number
        sorted_locations = []
        sorted_loc = {k: v for k, v in sorted(locations_no.items(), key=lambda item: item[1])}

        for loc in sorted_loc:
            sorted_locations.append(loc)
        # print(sorted_locations)

        # Get first segment #
        loc1 = story.find(location) + len(location)+1
        loc2 = story.find(sorted_locations[1])


        last_stop  = story[:loc2][::-1].find(".")   # last stop before location2
        first_boundary = loc2 - last_stop

        story_after_loc1 = story[first_boundary:]

        segment_1 = story[:first_boundary]
        print("segment"+"0", ":", segment_1)

        monitor = 1
        seg_length = len(segment_1)

        #Get for segment two then replicate for others
        if monitor > 0:

            #last and next location
            loc1 = story_after_loc1.find(sorted_locations[1])+len(sorted_locations[1])+1
            loc2 = story_after_loc1.find(sorted_locations[2])


            # inverse
            rev_story = story_after_loc1[:loc2][::-1]
            nxt_stop = rev_story.find(".")

            # reverse inverse
            segment = rev_story[nxt_stop:][::-1]
            seg_length = seg_length + len(segment)
            print("segment"+"1", ":", segment , "\n")


            story_after_loc1 = story[seg_length:]
            # print(story_after_loc1)

        #Get segments from three to four
            #to check if a location has gone with the initial location's sentence
            #check if which of the locations is present in the sentence and remove from the list
        locs_length = len(sorted_locations[2:])
        for a, location in enumerate(sorted_locations[2:], 2):
            #if location is not the last location

            if a < locs_length+1:
                # this and next location
                loc1 = story_after_loc1.find(sorted_locations[a]) + len(sorted_locations[a]) + 1
                loc2 = story_after_loc1.find(sorted_locations[a + 1])


                # invert
                rev_story = story_after_loc1[:loc2][::-1]
                nxt_stop = rev_story.find(".")

                # reverse the inverse
                segment = rev_story[nxt_stop:][::-1]
                seg_length = seg_length + len(segment)
                print("segment" + str(a), ":", segment, "\n")
                segments.append(segment)

                story_after_loc1 = story[seg_length:]

            else:
                print("segment" + str(a), ":", story_after_loc1, "\n")
                segment = story_after_loc1
                segments.append(segment)
        return segments











    def create(self):
        story = self.story
        entities = self.entities
        player_name = ' '
        ##   Clean the data ##
        story = story.lower()
        lower_entities = dict()
        for ent in entities:
            lower_entities[ent.lower()] = entities[ent].lower()
        for ent in entities:
            if entities[ent].lower() == 'player':
                player_name = ent


        ##  Segmentation ##
        segments = self.segmentation(story, lower_entities)
        print("\n Subsegmentation...\n \n" )
        ## Sub-segmentation
        all_subsegments = self.subsegmentation(segments, player_name)
        return  all_subsegments


