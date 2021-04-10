import re
from custom_exception import UserInputTextException

def text_input(string):
    result = input(string)
    if len(re.findall('[^A-Z^a-z^\d]', result)):
        return UserInputTextException
    return result
        
def get_input_function():
    try:
        input_function = raw_input
    except NameError:
        input_function = input
        
    return input_function