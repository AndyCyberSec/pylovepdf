from pylovepdf.task import Task


class OfficeToPdf(Task):

    def __init__(self, public_key, verify_ssl):

        self.tool = 'officepdf'
        super(OfficeToPdf, self).__init__(public_key, True, verify_ssl)





