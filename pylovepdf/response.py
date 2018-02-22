import json


class Response(object):

    def __init__(self, response):

        self.status = response.status_code

        try:
            params = json.JSONDecoder().decode(response.text)

            for attr, value in params.items():
                setattr(self, attr, value)

        except json.decoder.JSONDecodeError:
            # if it's not json, it's the incoming pdf file or empty response
            # deleting a task will not output anything from ilovepdf.com, so:
            if 'application/pdf' in response.headers['content-type']:
                setattr(self, 'headers', response.headers)
                setattr(self, 'iter_content', response.iter_content)
            elif 'application/zip' in response.headers['content-type']:
                setattr(self, 'headers', response.headers)
                setattr(self, 'iter_content', response.iter_content)
            elif 'image/jpeg'in response.headers['content-type']:
                setattr(self, 'headers', response.headers)
                setattr(self, 'iter_content', response.iter_content)
            else:
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
