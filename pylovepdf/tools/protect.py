from pylovepdf.task import Task


class Protect(Task):

    def __init__(self, public_key, verify_ssl, proxies):

        self.tool = 'protect'

        super(Protect, self).__init__(public_key, True, verify_ssl, proxies)
