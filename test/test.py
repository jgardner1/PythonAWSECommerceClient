#!/usr/bin/env python
from awsecommerceclient import AWSECommerceClient

client = AWSECommerceClient(
    '1KHB4V2W5HGHCAHD2M82',
    'onlyeee-20',
    'wx+WYK5aXWBJQmlut0886531i3THLP0CY2SRfxrX')

response = client.ItemLookup(
    ItemId='B000H6SXMY',
    ResponseGroup='Reviews')

from pprint import pprint
pprint(response['Items'])
