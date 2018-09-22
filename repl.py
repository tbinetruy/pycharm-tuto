import datetime

class REPL:
    def __init__(self):
        print('Press Ctrl-C Ctrl-C to quit for the terminal or Ctrl-D from the REPL.')

        while 1:
            print(self.eval(self.read()))

    def read(self):
        return input('>> ')
    def eval(self, user_input):

        return user_input


REPL()
