#!/usr/bin/env python
from awsecommerceclient import AWSECommerceClient

client = AWSECommerceClient(
    '1KHB4V2W5HGHCAHD2M82',
    'onlyeee-20',
    'wx+WYK5aXWBJQmlut0886531i3THLP0CY2SRfxrX')

print client.itemSearch(
    SearchIndex='Electronics',
    Manufacturer='Asus',
    Keywords='Asus Eee PC',
    Order='-price',
    ResponseGroup='ItemAttributes,Images')
