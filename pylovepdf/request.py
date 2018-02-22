import requests
from pylovepdf.response import Response

# linew below are to disable ssl warning when verify_ssl is set to False
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class Request(object):

    @staticmethod
    def send(method, url, payload, headers=None, files=None, stream=None, verify_ssl=True):

        if method == 'post':
            response = requests.post(url, headers=headers, data=payload, files=files, verify=verify_ssl, stream=stream)
        else:
            response = requests.get(url, headers=headers, data=payload, files=files, verify=verify_ssl, stream=stream)

        return Response(response)

