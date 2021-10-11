"""
Notes about clean code.
 - Format name variables, functions and class
 - Function struct to clean code
    {Typing / Docstring / }

Some bibliography
- https://stackoverflow.com/questions/472000/usage-of-slots

"""

import traceback, sys, logging

# Format

nameVariable = 0

def function_sum(firstVal:int, secondVal:int) -> int:
    """
        This function return value by sum two integer number.
    """
    try:
        return firstVal+secondVal
    except Exception as Err:
        logging.error(f"Error into :\n {function_sum.__name__} | \n | {traceback.format_exc()}")


class MyClassName():
    __slots__ = ['nothing']
    def __init__(self, nothing:str):
        self.nothing = nothing
    
    def msg_upper(self, val:str) -> str:
        """
            This function return upper case text.
        """
        return val.upper()

class AnotherClass():
    def __init__(self, nothing:str):
        self.nothing = nothing
    
    def msg_upper(self, val:str) -> str:
        """
            This function return upper case text.
        """
        return val.upper()