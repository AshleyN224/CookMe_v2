import os
import requests
import json
import spoonacular as sp

# set keys for authentication
# Hidden API key guide: https://towardsdatascience.com/how-to-hide-your-api-keys-in-python-fb2e1a61b0a0

API_SECRET = os.environ.get('SECRET_KEY')
api = sp.API(API_SECRET)
api_root = 'https://api.spoonacular.com/'
headers = {'Content-Type':'application/json'}

# API authentication
class search_API():
    def __init__(self, api_key):
        """ Spoonacular API call
            
        :param api_key: key prvided by spoonacular (str)
        """
        self.api_key = os.environ.get('SECRET_KEY')
        self.api_root = 'https://api.spoonacular.com/'

    def requests(self, path, method='GET', endpoint=None,
                query_=None, params_=None, json_=None):
                """ Make a request to the API """
                
                uri = self.api_root + path
                if params_:
                    params_['apiKey'] = self.api_key
                else:
                    params_ = {'apiKey': self.api_key}
                response = self.session.request(method, uri, data=query_, params=params_, json=json)
                return response
                

    def search_recipes_by_ingredients(self, ingredients, fillIngredients=None, limitLicense=None, number=None, ranking=None):
        """ Find recipes that use as many of the given ingredients
            as possible and have as little as possible missing
            ingredients.
            https://spoonacular.com/food-api/docs#search-recipes-by-ingredients
        """
        endpoint = "recipes/findByIngredients"
        url_query = {}
        url_params = {"fillIngredients": fillIngredients, "ingredients": ingredients, "limitLicense": limitLicense, "number": number, "ranking": ranking}
        return self._make_request(endpoint, method="GET", query_=url_query, params_=url_params)
    
#response = api.search_recipes_by_ingredients('chicken, lemon')
#data = response.json()
#print(data[0])