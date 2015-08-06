# -*- coding: utf-8 -*-
""" Juniper """
from base import Router

class JUNOS(Router):
    Command_List = {
      'get-config' : ['show configuration | no-more']
    }

