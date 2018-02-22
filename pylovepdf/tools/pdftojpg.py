from pylovepdf.task import Task


class PdfToJpg(Task):

    def __init__(self, public_key, verify_ssl):

        self.pdfjpg_mode = 'pages'

        self.tool = 'pdfjpg'
        super(PdfToJpg, self).__init__(public_key, True, verify_ssl)

    @property
    def allowed_properties(self):
        return 'pdfjpg_mode',

    @property
    def pdfjpg_mode_values(self):
        return 'pages', 'extract'

    def process(self):

        payload = super(PdfToJpg, self).process()
        payload = self.as_dict(payload, self.allowed_properties)

        return payload






