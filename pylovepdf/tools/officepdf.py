from pylovepdf.task import Task


class Officepdf(Task):

    def __init__(self, public_key, verify_ssl, proxies):

        self.tool = 'officepdf'
        super(Officepdf, self).__init__(public_key, True, verify_ssl, proxies)
