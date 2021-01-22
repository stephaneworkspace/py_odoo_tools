import xmlrpc.client

"""
    Author: Stéphane Bressani (s.bressani@bluewin.ch)
"""

class Connect:
    def __init__(self, host, db, username, password):
        """ Connect via xml-rpc """
        self.host = host
        self.db = db
        self.username = username
        self.password = password
        self.common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(self.host))
        self.uid = self.common.authenticate(self.db, self.username, self.password, {})

    def get_version(self):
        """ Version of odoo """
        return self.common.version()

    def get_uid(self):
        """ Get uid """
        return self.uid

class Model:
    def __init__(self, connect, model):
        """ Model binding """
        self.connect = connect
        self.model = model
        self.models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object',format(self.connect.host))

    def execute_method(self, method, arr_params, map_params):
        """ Execute mehod on the model """
        return self.models.execute_kw(self.connect.db, self.connect.uid, self.connect.password,
            self.model, method,
            ['read'], {'raise_exception': False})
