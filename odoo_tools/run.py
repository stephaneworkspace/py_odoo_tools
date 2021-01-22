"""
import os
"""
import xmlrpc.client

"""
    Author: Stéphane Bressani (s.bressani@bluewin.ch)
"""
# The absolute path of the directoy for this file:
#_ROOT = os.path.abspath(os.path.dirname(__file__))

class Connect:
    def __init__(self, host, db, username, password):
        """ Connect via xml-rpc """
        self.host = host
        self.db = db
        self.username = username
        self.password = password
        self.common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(self.host))
        self.version = common.version()
        self.uid = common.authenticate(self.db, self.username, self.password, self.host)

    def say_hello(self):
        return "Hello, World!"

class Model:
    def __init__(self, connect, 

"""
def open_image(self):
        print("Reading image.gif contents:")

        # Get the absolute path of the image's relative path:
        absolute_image_path = os.path.join(_ROOT, 'images/hello.gif')

        with open(absolute_image_path, "r") as f:
            for line in f:
                print(line)
"""
