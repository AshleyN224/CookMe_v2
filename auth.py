import os

# set keys for authentication
# Keys are used to add authentication, but are removed for security purposes as this is a public repo.
API_SECRET = os.environ.get('SECRET_KEY')
endpoint = 'https://api.spoonacular.com/recipes/findByIngredients'