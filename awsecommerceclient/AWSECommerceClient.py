from boto.connection import AWSQueryConnection
from Parser import Parser
import time
import urllib

class AWSECommerceClient(object):

    def __init__(self,
            aws_access_key_id,
            aws_associate_tag,
            aws_secret_access_key,
    ):
        self.aws_access_key_id = aws_access_key_id
        self.aws_associate_tag = aws_associate_tag
        self.aws_secret_access_key = aws_secret_access_key

    def method(self, operation, **kwargs):
        aws_conn = AWSQueryConnection(
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key, is_secure=False,
            host='ecs.amazonaws.com')

        aws_conn.SignatureVersion = '2'
        kwargs.update(dict(
            Service='AWSECommerceService',
            Version=Parser.version,
            SignatureVersion=aws_conn.SignatureVersion,
            AWSAccessKeyId=self.aws_access_key_id,
            AssociateTag=self.aws_associate_tag,
            Timestamp=time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime()),
            Operation=operation,
        ))
        verb = 'GET'
        path = '/onca/xml'
        qs, signature = aws_conn.get_signature(kwargs, verb, path)
        qs = path + '?' + qs + '&Signature=' + urllib.quote(signature)

        return Parser.parse_file(aws_conn._mexe(verb, qs, None, headers={}))

    def Help(self, **kwargs):
        return self.method('Help', **kwargs)

    def ItemSearch(self, **kwargs):
        return self.method('ItemSearch', **kwargs)

    def ItemLookup(self, **kwargs):
        return self.method('ItemLookup', **kwargs)

    def BrowseNodeLookup(self, **kwargs):
        return self.method('BrowseNodeLookup', **kwargs)

    def ListSearch(self, **kwargs):
        return self.method('ListSearch', **kwargs)

    def ListLookup(self, **kwargs):
        return self.method('ListLookup', **kwargs)

    def CustomerContentSearch(self, **kwargs):
        return self.method('CustomerContentSearch', **kwargs)

    def CustomerContentLookup(self, **kwargs):
        return self.method('CustomerContentLookup', **kwargs)

    def SimilarityLookup(self, **kwargs):
        return self.method('SimilarityLookup', **kwargs)

    def SellerLookup(self, **kwargs):
        return self.method('SellerLookup', **kwargs)

    def CartGet(self, **kwargs):
        return self.method('CartGet', **kwargs)

    def CartAdd(self, **kwargs):
        return self.method('CartAdd', **kwargs)

    def CartCreate(self, **kwargs):
        return self.method('CartCreate', **kwargs)

    def CartModify(self, **kwargs):
        return self.method('CartModify', **kwargs)

    def CartClear(self, **kwargs):
        return self.method('CartClear', **kwargs)

    def TransactionLookup(self, **kwargs):
        return self.method('TransactionLookup', **kwargs)

    def SellerListingSearch(self, **kwargs):
        return self.method('SellerListingSearch', **kwargs)

    def SellerListingLookup(self, **kwargs):
        return self.method('SellerListingLookup', **kwargs)

    def TagLookup(self, **kwargs):
        return self.method('TagLookup', **kwargs)

    def VehicleSearch(self, **kwargs):
        return self.method('VehicleSearch', **kwargs)

    def VehiclePartSearch(self, **kwargs):
        return self.method('VehiclePartSearch', **kwargs)

    def VehiclePartLookup(self, **kwargs):
        return self.method('VehiclePartLookup', **kwargs)

    def MultiOperation(self, **kwargs):
        return self.method('MultiOperation', **kwargs)
