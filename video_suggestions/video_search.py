import os
import random
import requests
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from connection.connect import mysql_connect


RESULTS = []


class SevicesWithTheBestYield:
    def __init__(self) -> None:
        self.conn = mysql_connect()
        self.selected_services = []

    def get_services(self):
        cursor = self.conn.cursor()
        sql = "SELECT * from video_search_services"
        cursor.execute(sql)
        services = cursor.fetchall()
        return services

    def sort_services(self):
        services = self.get_services()
        self.selected_services = sorted(services, key=lambda x: x[3])
        return self.selected_services
    
    def select_services(self):
        sorted_services = self.sort_services()
        selected_services = []
        selected_services.append(sorted_services[0])
        random_selector = random.sample(range(1, len(sorted_services)), k=2)
        selected = [selected_services.append(sorted_services[x]) for x in random_selector]

        return selected_services
    
#print(SevicesWithTheBestYield().select_services())


class SearchKeywordsWithTheBestYield:
    def __init__(self, level) -> None:
        self.level = level
        self.conn = mysql_connect()
        self.selected_keywords = []

    def get_keywords(self):
        cursor = self.conn.cursor()
        sql = "SELECT * from keywords"
        cursor.execute(sql)
        services = cursor.fetchall()
        return services
    
    def keywords_for_level(self):
        services = self.get_keywords()
        return {'keyword #' + str(i+1) : [v[1], v[3]] for i, v  in enumerate(services) if v[2] == self.level}

    def sort_keywords(self):
        keywords_and_rating = self.keywords_for_level()
        self.selected_services = sorted(keywords_and_rating.items(), key=lambda x: x[1][1])
        return self.selected_services
    
    def select_keywords(self):
        sorted_keywords = self.sort_keywords()
        selected_keywords = []
        selected_keywords.append(sorted_keywords[0])

print(SearchKeywordsWithTheBestYield('beginner').select_keywords())

class RawSearchResults:
    def __init__(self) -> None:
        self.conn = mysql_connect()
        self.services = []

    def sevice_url_generator(self):
        cursor = self.conn.cursor()
        sql = "SELECT * from video_search_services"
        cursor.execute(sql)
        services = cursor.fetchall()

        return self.services


# print(RawSearchResults().sevice_url_generator())

class IsWatched:
    def __init__(self, client_mail, input_url) -> None:
        self.client_mail = client_mail
        self.input_url = input_url

    def boolean_result(self):
        return True


class SelectAndSortResults:
    """
    sort po brok=ju laskova i pregleda
    """

    def __init__(self) -> None:
        pass


class FinalSixResults:
    pass
