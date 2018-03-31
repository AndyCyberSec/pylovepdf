from pylovepdf.ilovepdf import ILovePdf
from pylovepdf.file import File
import re


class Task(ILovePdf):

    tool = ''

    def __init__(self, public_key, start=False, verify_ssl=True):

        self.files = []
        self.downloaded_file_extension = ''
        self.downloaded_filename = ''
        self.download_path = ''
        self.task = ''
        self.status = ''

        super(Task, self).__init__(public_key)

        self.begin = start
        self.file = None

        # Process task variables
        self.debug = False
        self.ignore_errors = True
        self.ignore_password = False
        # {date} = current date {n} = file number {filename} = original filename {tool} = current processing tool
        self.output_filename = '{filename}_{app}_{date}'
        # {date} = current date {n} = file number {filename} = original filename {app} = current processing action
        self.packaged_filename = 'archive_{app}_{date}'
        self.file_encryption_key = None
        self.try_pdf_repair = True
        self.custom_int = None
        self.custom_string = None
        self.webhook = None

        if self.begin:
            self._set_verify_ssl(verify_ssl)
            self.auth()
            self.start()

    def auth(self):

        payload = {"public_key": self.public_key}

        response = self._send_request('post', 'auth', payload, None, self.begin)
        self._set_token(response.token)
        self._set_headers()

    def start(self):

        headers = self.headers
        response = self._send_request('get', 'start/' + self.tool, None, headers, self.begin)
        self._set_working_server(response.server)

        self.task = response.task

    def add_file(self, file_path):

        self.file = File()

        self.file.filename = file_path
        self.files.append(self.file)

    def upload(self):

        payload = {"task": self.task}

        for file in self.files:

            with open(file.filename, 'rb') as f:
                response = self._send_request('post', 'upload', payload=payload, headers=self.headers,
                                              files={"file": f})

            file.server_filename = response.server_filename

    def add_file_from_url(self):
        pass

    def check_values(self, p, p_list_of_values):

        value = getattr(self, p)
        try:
            list_of_values = getattr(self, p_list_of_values)
        except AttributeError:
            # for example self.mode does not have self.mode_values
            return True

        if value in list_of_values:
            return True
        else:
            return False

    def as_dict(self, payload, allowed_properties):

        """Builds a dictionary payload

        It uses allowed properties from and object to build a payload dictionary.
        Payload is a command to be sent to get ilovepdf.com working
        It is called inside tools

        :param payload: commands
        :param allowed_properties:
        :type payload: dict
        :type allowed_properties: tuple, list
        :return: payload
        :rtype: dict
        """

        for k in allowed_properties:
            if self.check_values(k, k + '_values'):
                payload[k] = getattr(self, k)
            else:
                raise ValueError("'%s' is not allowed in '%s' property valid values: (%s)"
                                 % (getattr(self, k), k, getattr(self, k + '_values')))

        return payload

    def process(self):

        """Builds payload commands to get ilovepdf.com working

        :return: payload
        :rtype: dict
        """

        payload = {'task': self.task, 'tool': self.tool, 'ignore_errors': self.ignore_errors,
                   'ignore_password': self.ignore_password, 'output_filename': self.output_filename,
                   'packaged_filename': self.packaged_filename, 'try_pdf_repair': self.try_pdf_repair,
                   'custom_string': self.custom_string, 'webhook': self.webhook}

        if self.debug:
            payload['debug'] = True
            print("n of files: %s" % len(self.files))
            print(self.files)

        i = 0
        # adding commands for each file filtering some file object properties
        for file in self.files:
            for attribute, value in iter(file.as_dict()):
                if attribute != 'password' and attribute != 'file_encryption_key' and attribute != 'metas':
                    index = "files[%s][%s]" % (i, attribute)
                    payload[index] = value
                elif attribute == 'password':
                    if value:
                        payload[attribute] = value
                elif attribute == 'file_encryption_key':
                    if value:
                        payload['file_encryption_key'] = value
                elif attribute == 'metas':
                    for k, v in value.items():
                        if v:
                            index = "metas[%s]" % k
                            payload[index] = v
            i += 1

        if self.debug:
            print("\nBuilt Payload: %s" % payload)

        return payload

    def execute(self):

        print('Uploading file...')
        self.upload()

        payload = self.process()

        response = self._send_request('post', 'process', payload, self.headers)

        print("File uploaded! Below file stats:")
        self.status = response.status

        print(response)

    def set_output_folder(self, path):

        self.download_path = path

    def check_task_status(self, printall=False):

        response = self._send_request('get', 'task/%s' % self.task, None, self.headers, False,
                                      None, stream=False)

        if printall:
            print(response)
        else:
            return response.status

    def clean_filename(self, filename):

        name = filename.split('_')
        return name[len(name)-3] + '_' + name[len(name)-2] + '_' + name[len(name)-1]

    def download(self):

        if len(self.files) > 0 and not self.debug and self.status == 'TaskSuccess':

            print('Downloading processed file...')

            response = self._send_request('get', 'download/%s' % self.task, None, self.headers, False,
                                          None, stream=True)

            # file_ext = str(response.headers['content-type']).split('/')

            filename = self.clean_filename(re.search(r'(filename=\")(.+\.\w+)(\")',
                                                     str(response.headers['content-disposition'])).group(2))

            with open(self.download_path + '\\' + filename, 'wb') as f:
                for chunk in response.iter_content(10):
                    f.write(chunk)

            print('File downloaded!')

            return True

        else:
            print("no file to be downloaded")

    def delete_current_task(self):

        response = self._send_request('post', 'task/' + self.task, None, headers=self.headers)
        print("Task delete %s" % response)



