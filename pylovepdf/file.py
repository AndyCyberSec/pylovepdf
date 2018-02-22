

class File(object):

    def __init__(self):

        self.filename = ''
        self.server_filename = ''
        self.rotate = 0
        self.password = None
        # file_encryption_key TBD
        self.file_encryption_key = None
        self.metas = {}

    @property
    def metas_values(self):

        return "Title", "Author", "Subject", "Keywords", "Creator", "Producer", "CreationDate", "ModDate", "Trapped"

    def get_file_options(self):
        pass

    def set_metas(self, key, value):

        if key in self.metas_values:
            self.metas[key] = value
        else:
            raise ValueError("'%s' is not a meta tag: %s" % (key, self.metas))

    def as_dict(self):

        for k in dir(self):
            if getattr(self, k) and \
                    'set_metas' not in k and 'get_file_options' not in k and 'as_dict' not in k \
                    and '__' not in k and '_values' not in k:
                yield(k, getattr(self, k))

