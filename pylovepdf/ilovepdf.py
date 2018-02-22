from pylovepdf.request import Request

import importlib


class ILovePdf(object):
    """This class is used to init the API

        The public method you will use from this class is :func: `new_task`

        - **parameters**, **types**, **return** and **return types**::

              :param public_key: This is the API key to get on http://developers.ilovepdf.com
              :param verify_ssl: This parameter is used to enable or disable SSL during http requests
              :type public_key: String
              :type verify_ssl: Bool
              :return: return description
              :rtype: the return type description

        :Example:

            from pylovepdf.ilovepdf import ILovePdf

            ilovepdf = ILovePdf('public_key', verify_ssl=True)
            task = ilovepdf.new_task('compress')
            task.add_file('pdf_file')
            task.set_output_folder('output_directory')
            task.execute()
            task.download()
            task.delete_current_task()

        Here below is the results of the :func:`new_task` docstring.

        """

    def __init__(self, public_key, verify_ssl=True):

        # auto explaining
        self.public_key = public_key
        self.ssl = verify_ssl

        # Currently not used
        self.secret_key = ''

        self.api_version = 'v1'
        self.start_server = 'api.ilovepdf.com'
        self.working_server = ''

        # ilovepdf access token
        self.token = ''

        # headers which will contain access token to be sent for every task
        self.headers = None

    def _get_jwt(self):
        # TBD
        pass

    def _set_token(self, token):

        self.token = token

    def _set_headers(self):

        self.headers = {"Authorization": "Bearer " + self.token}

    def _set_working_server(self, working_server):

        self.working_server = working_server

    def _send_request(self, method, endpoint, payload, headers=None, start=False, files=None, stream=None):

        server = self.start_server

        if not start and self.working_server:
            server = self.working_server

        url = 'https://' + server + '/' + self.api_version + '/' + endpoint
        response = Request.send(method, url, payload, headers, files, stream, verify_ssl=self.ssl)

        return response

    def _set_verify_ssl(self, verify):

        self.ssl = verify

    def new_task(self, tool):
        """Returns Used tool Object

            This function instance a new object with the selected tool properties.

            - **parameters**, **types**, **return** and **return types**::

                  :param tool: name of the tool to be used
                  :type tool: String
                  :rtype: Tool Object

        """

        module_name = importlib.import_module('.tools.' + tool.lower(), package='pylovepdf')
        class_name = getattr(module_name, tool.title())

        return class_name(self.public_key, self.ssl)
