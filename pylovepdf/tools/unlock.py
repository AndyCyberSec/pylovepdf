from pylovepdf.task import Task


class Unlock(Task):

    def __init__(self, public_key, verify_ssl, proxies):

        self.tool = 'unlock'
        super(Unlock, self).__init__(public_key, True, verify_ssl, proxies)



