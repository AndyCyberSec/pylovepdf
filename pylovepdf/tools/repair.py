from pylovepdf.task import Task


class Repair(Task):

    def __init__(self, public_key, verify_ssl, proxies):

        self.tool = 'repair'
        
        super(Repair, self).__init__(public_key, True, verify_ssl, proxies)
