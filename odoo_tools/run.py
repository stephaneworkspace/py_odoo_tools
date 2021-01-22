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
        self.uid = self.common.authenticate(self.db, self.username, self.password, self.host)

    def get_version(self):
        """ Version of odoo """
        return self.common.version()

    def get_uid(self):
        """ Get uid """
        return self.uid

class Model:
    def __init__(self, connect, method, arr_params, map_params):
        """ Model binding """
        self.connect = connect
        self.method = method
        self.arr_params = arr_params
        self.map_params = map_params
        self.models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object',format(self.connect.host))

    def execute_method(self):
        """ Execute mehod on the model """
        return self.models.execute_kw(self.connect.db, self.connect.uid, self.connect.password,
            'res.partner', 'check_acces_rights',
            ['read'], {'raise_exception': False})
