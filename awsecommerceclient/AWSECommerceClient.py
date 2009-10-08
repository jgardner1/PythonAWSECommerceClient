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

    def itemSearch(self, **kwargs): 
        return self.method('ItemSearch', **kwargs)

