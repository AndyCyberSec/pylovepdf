from pylovepdf.task import Task


class Merge(Task):

    def __init__(self, public_key, verify_ssl):

        self.tool = 'merge'
        super(Merge, self).__init__(public_key, True, verify_ssl)





