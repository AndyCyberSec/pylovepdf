from pylovepdf.task import Task


class Split(Task):

    def __init__(self, public_key, verify_ssl):

        self.tool = 'split'
        self.split_mode = 'ranges'
        self.ranges = None
        self.fixed_range = 1
        self.remove_pages = None
        self.merge_after = False

        super(Split, self).__init__(public_key, True, verify_ssl)

    @property
    def allowed_properties(self):

        allow = ['split_mode', 'ranges', 'fixed_range', 'remove_pages', 'merge_after']

        if self.split_mode == 'ranges':
            allow.remove('fixed_range')
        elif self.split_mode == 'fixed_range':
            allow.remove('ranges')

        if self.remove_pages == 'null':
            allow.remove('remove_pages')

        return allow

    @property
    def split_mode_values(self):
        return 'ranges', 'fixed_range', 'remove_pages'

    def process(self):
        payload = super(Split, self).process()
        payload = self.as_dict(payload, self.allowed_properties)

        return payload




