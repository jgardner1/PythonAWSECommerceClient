#!/usr/bin/env python
from awsecommerceclient import AWSECommerceClient

client = AWSECommerceClient(
    '1KHB4V2W5HGHCAHD2M82',
    'deal-digger.com-20',
    'wx+WYK5aXWBJQmlut0886531i3THLP0CY2SRfxrX')

response = client.ItemSearch(
    Keywords="potato",
    ItemId='B000H6SXMY',
    SearchIndex='Blended')

from pprint import pprint
pprint(response)
