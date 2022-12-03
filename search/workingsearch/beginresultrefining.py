from isolateactualsearch import IsolateResults
import json

isolatingresults = IsolateResults()

class BeginRefiningSearch:

    def __init__(self):
        self.boop = "Boop"
        self.object_to_return = {}
        self.object_to_pass = {}
        self.final_object_with_arrays = {}
        self.finaljson = "objecttoiterate.json"

#####################################

    def finish_up(self):
        with open(self.finaljson, "w", encoding='utf-8') as finaljson:
            json.dump(self.object_to_pass, finaljson, ensure_ascii=False)

# Here is where I add the fields that we're actually going to be searching through for the key phrases
# Note that I'm forcing the dictionary object (object_to_pass[count]) into a list

    def get_array_field_name(self, field):
        field_size = len(field)
        field_array_name = field[:field_size - 9]
        return field_array_name

    def add_fields_to_object_to_pass(self):
        base_count = len(self.object_to_pass)
        count = 0
        while count < base_count:
            for items in list(self.object_to_pass[count]):
                if items == 'episode_title':
                    continue
                else:
                    # print(items)
                    # print("this is an item to be created")
                    field_to_add = self.get_array_field_name(items)
                    # print(field_to_add)
                    # print("this is the field name I'm adding")
                    self.object_to_pass[count][field_to_add] = []
                count += 1

# In this section I am just looping over the results to filter out the data which matches the query
# So:
# Begin refining - has the entire object returned during search
# Loop through all results - extracts which fields contain a match with the original search term and then pass only those fields along
# After that and the above are done we pass it over to the Isolate Search class to whittle it down

    def loop_through_search_results(self, returned_items, count):
        for k, v in returned_items.items():
            if "b class=\"match term" in v:
                self.object_to_pass[count][k] = v
            else:
                continue

    def begin_refining(self, search_results, queries):
        self.final_object_with_arrays = {}
        self.object_to_pass = {}
        count = 0
        if type(queries) == list:
            for i in search_results:
                self.object_to_pass[count] = {}
                self.object_to_pass[count]['episode_title'] = search_results[count]['episode_title']
                self.loop_through_search_results(i, count)
                count += 1
            self.finish_up()
            self.add_fields_to_object_to_pass()
            # isolatingresults.begin_isolation(self.object_to_pass, search_results, queries)
        else:
            # print("BOOP")
            self.object_to_pass[count] = {}
            print(search_results[0]['episode_title'])
            print("This is our episode title")
            self.object_to_pass[count]['episode_title'] = search_results[0]['episode_title']
            self.loop_through_search_results(search_results[0], count)
            # print("This is the item")
            self.add_fields_to_object_to_pass()
            # isolatingresults.begin_isolation(self.object_to_pass, search_results, queries)
        # self.finish_up()
        # print(self.object_to_pass)
        # print("FINAL OBJECT TO PASS")
        
