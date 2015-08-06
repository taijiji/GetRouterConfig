# -*- coding: utf-8 -*-
"""Definition Router."""
from Exscript.protocols import SSH2
from Exscript.Account import Account

class Router:

    """Router class."""

    Command_List = {}

    def __init__(self, router_info):
        """Initialize."""
        self.hostname = router_info['hostname']
        self.username = router_info['username']
        self.password = router_info['password']
        self.ipv4 = router_info['ipv4']
        self.os_name = router_info['os']
        self.session = None
	self.result = None

    def login(self):
        """login."""
        self.session = SSH2()
        self.session.connect(self.ipv4)
        self.session.login(Account(name=self.username, password=self.password))

    def logout(self):
        """logout."""
        if self.session:
            self.session.send('exit\r')
            self.session.close()
        else:
            raise AttributeError('cannot find a living session.')

    def get_config(self):
        """get configuration."""
        command_key = 'get-config'
        if (not self.Command_List.has_key(command_key)):
            raise NameError(command_key + ' not supported')

	for cmd in self.Command_List[command_key]:
            self.session.execute(cmd)
            result = self.session.response
        self.result = result

        return self.result
