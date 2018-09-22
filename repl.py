import datetime

class REPL:
    def __init__(self):
        print('Press Ctrl-C Ctrl-C to quit for the terminal or Ctrl-D from the REPL.')

        while 1:
            print(self.eval(self.read()))

    def read(self):
        return input('>> ')
    def eval(self, user_input):
        help_message = 'Here are the available commands: \n help \n time \n dotproduct'
        result = 'Command not recognized. ' + help_message

        if user_input == 'time':
            # Using our datetime import
            result = datetime.date.today()
        if user_input == 'help':
            result = help_message

        return result

REPL()

