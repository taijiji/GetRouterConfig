# -*- coding: utf-8 -*-
"""  for Cisco """
from base import Router

class Cisco(Router):
    Command_List = {
      'get-config' : ['terminal length 0', 'show running-config']
    }
class IOS(Cisco): pass

class IOSXR(Cisco): pass

class IOSXE(Cisco): pass

