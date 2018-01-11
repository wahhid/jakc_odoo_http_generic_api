import xmlrpclib
from xmlrpclib import Error
from odoo.connection import Connection

class ResUsers(Connection):

    def __init__(self, server, port, dbname, user, pwd):
        Connection.__init__(self, server, port, dbname, user, pwd)

    def get_users(self):
        return self.get_list('res.users')

    def get_user(self, id):
        return self.get_one('res.users', id)

