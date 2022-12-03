import json

class IsolateResults:

    def __init__(self):
        self.boop = "Boop"
        self.object_passed_to_class = {}
        self.final_object = {}
        self.episode_title_to_search = ""

    def assign_results_to_final_object(self, key, value, queries):
        self.final_object[self.episode_title_to_search][key] = []
        if type(queries) == list:
            for query in queries:
                for item in value:
                    if query in item:
                        self.final_object[self.episode_title_to_search][key].append(item)
        else:
            query = queries
            for item in value:
                if query in item:
                    self.final_object[self.episode_title_to_search][key].append(item)
        
    def loop_through_all_results(self, key, value, raw_results, query):
        for result in raw_results:
            for k,v in raw_results[0].items():
                if k == key:
                    self.assign_results_to_final_object(k, v, query)
                else:
                    continue

    def begin_isolation(self, filteredsearchresults, allsearchresults, query):
        self.final_object = {}
        self.object_passed_to_class = allsearchresults
        for item in filteredsearchresults:
            for k,v in filteredsearchresults[item].items():
                self.episode_title_to_search = filteredsearchresults[item]['episode_title']
                self.final_object[self.episode_title_to_search] = {}
                if v == []:
                    self.loop_through_all_results(k, v, allsearchresults, query)
                self.episode_title_to_search = ""
        print(self.final_object)
        print("This should be our final object")