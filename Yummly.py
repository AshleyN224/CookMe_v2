import sys
import auth

# search recipes based on ingredients --> preset or enter ingredient
# search recipes based on inegrients with food restrictions

class UseageOptions:
    def options(self):
        '''Display usage options to user on invalid input or when -h is called.'''
        print('\nUsage Options\n'
            #+'- Get top trends of a geographical location:\n'
            #+'\t> python geotweets.py -trends\n'
            #+'\t> python geotweets.py -trends [city | country]\n\n'
            #+'- Fetch Where On Earth ID (WOEID) of a geographical location:\n'
            #+'\t> python geotweets.py -woeid\n'
            #+'\t> python geotweets.py -woeid [city | country]\n\n'
            #+'- Enter command line interface of the program:\n'
            #+'\t> python geotweets.py'
            #+'\n\nNote: Locations that have more than one word should be put in quotes. Example:\n'
            #+'\t> python geotweet.py -trends \'Los Angeles\'')
        )

class FoodSearch:
    def IngredientSearch(self):
        pass

    def RestrictedSearch(self):
        pass

class CookMe:
    def app(self):
        if len(sys.argv) == 1:

            # loop that prompts user what they would like to do
            while True:
                choice = input('\nHow would you like to search?\n(1) Based on ingredients\n(2) Based on food restrictions\n(3)Exit program')
                
                # if choice == '1':
                    #try:
                    #except
                # elif choice == '2':
                # elif choice == '3':
                # else:
                    #print('Input not recognized. Select valid input.')

        # display usage options
        elif sys.argv[1] == '-h':
            UseageOptions()

        # Search by Ingredient
        elif sys.argv[1] == '-i':
            FoodSearch.IngredientSearch()

        # Search by food restrictions
        elif sys.argv[1] == '-r':
            FoodSearch.RestrictedSearch()

        else:
            print('\n! ERROR: Input not recognized. use the -h flag for usage instructions.\n')