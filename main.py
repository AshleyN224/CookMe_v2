from pyfiglet import Figlet
from clint.textui import colored
import pyfiglet
import Yummly

title = Figlet(font='slant')
print(colored.green(title.renderText('CookMe')))
print('-' * 50)

if __name__ == '__main__':
    Yummly.CookMe()