import json


class Response(object):

    def __init__(self, response):

        self.status = response.status_code
        try:
            headers = response.headers['content-type']
            if 'application/pdf' in headers:
                setattr(self, 'headers', response.headers)
                setattr(self, 'iter_content', response.iter_content)
            elif 'application/zip' in headers:
                setattr(self, 'headers', response.headers)
                setattr(self, 'iter_content', response.iter_content)
            elif 'image/jpeg'in headers:
                setattr(self, 'headers', response.headers)
                setattr(self, 'iter_content', response.iter_content)
            else:
                raise KeyError
        except KeyError:
            try:
                params = json.JSONDecoder().decode(response.text)

                if params:
                    for attr, value in params.items():
                        setattr(self, attr, value)
                        
            except json.decoder.JSONDecodeError:
                pass

    def __str__(self):

        message = ''

        for element in dir(self):
            if '__' not in element and element:
                # in case we are validating pdfa we need more formatting controls
                if 'validations' in element:
                    value = getattr(self, element)
                    message += "%s: %s \n" % (element, value[0]['status'])
                # in case of errors we need more formatting
                elif 'error' in element:
                    message += 'Error '
                    for attr, val in getattr(self, element).items():
                        if 'code' not in attr:
                            if 'param' in attr:
                                if 'list' not in str(type(val)):
                                    for k, v in val.items():

                                        message += "%s: %s\n" % (k, v)
                                else:
                                    message += "Error: %s\n" % val[0]['error']
                            else:
                                message += "%s: %s\n" % (attr, val)

                else:
                    message += "%s: %s \n" % (element, getattr(self, element))

        return message
