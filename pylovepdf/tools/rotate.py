from pylovepdf.task import Task


class Rotate(Task):

    def __init__(self, public_key, verify_ssl):

        self.tool = 'rotate'
        super(Rotate, self).__init__(public_key, True, verify_ssl)





