'''
Created on 26 nov. 2019

@author: Ecarvallo
'''

class pythonMessage():
    def __init__(self):
        self.type="Text"        
    def message(self, msg):
        print(msg)
        print(self.type)
if __name__ == '__main__':
    newMessage = pythonMessage()
    newMessage.message("HelloWorld")
    
    