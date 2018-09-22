import datetime
import numpy as np

class REPL:
    def __init__(self):
        print('Welcome, press help for instructions')
        print('Press Ctrl-C Ctrl-C to quit for the terminal or Ctrl-D from the REPL.')
        self.help_message = 'Here are the available commands: \n help \n time \n dotproduct'

        while 1:
            print(self.eval(self.read()))

    def read(self):
        return input('>> ')
    def eval(self, user_input):
        result = 'Command not recognized. ' + self.help_message

        fn_name = user_input.split(' ')[0]

        if fn_name == 'time':
            result = datetime.date.today()
        if fn_name == 'help':
            result = self.help_message
        if fn_name == 'dotproduct':
            vect1 = user_input.split(' ')[1]
            vect2 = user_input.split(' ')[2]
            # TODO refactor this
            result = print(eval("np.dot(" + vect1 + "," + vect2 + ")"))

        return result


REPL()
