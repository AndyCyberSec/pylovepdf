from pylovepdf.task import Task


class ImageToPdf(Task):

    def __init__(self, public_key, verify_ssl):

        self.orientation = 'portrait'
        self.margin = 0
        self.pagesize = 'fit'
        self.merge_after = True

        self.tool = 'imagepdf'
        super(ImageToPdf, self).__init__(public_key, True, verify_ssl)

    @property
    def allowed_properties(self):

        return 'orientation', 'margin', 'pagesize', 'merge_after'

    @property
    def pagesize_values(self):
        return 'fit', 'A4', 'letter'

    def process(self):

        payload = super(ImageToPdf, self).process()
        payload = self.as_dict(payload, self.allowed_properties)

        return payload






