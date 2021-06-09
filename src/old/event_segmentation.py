from collections import Counter

import random
import spacy
# nlp = spacy.load("en_core_web_sm")


class Segmentation:

    def __init__(self, story, entities):
        self.story = story
        self.entities = entities

    # random cost
    def random_cost(self):
        return random.randint(1, 4)
        print(random_cost())



    def segmentationB(self, segments, entities):
        player_name = "slayer"
        player_name = str(player_name.lower())
        storyname = "doometernal"



    def segmentationA(self, story, entities):
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











    def create(self):
        story = self.story
        entities = self.entities
        ##   Clean the data ##
        story = story.lower()
        lower_entities = dict()
        for ent in entities:
            lower_entities[ent.lower()] = entities[ent].lower()
        # print(entities)
        # print(len(lower_entities))

        ##  Segmentation A ##
        self.segmentationA(story, lower_entities)
        # self.segmentationB()
