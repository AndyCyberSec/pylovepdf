from pylovepdf.task import Task


class Watermark(Task):

    def __init__(self, public_key, verify_ssl):

        self.tool = 'watermark'

        self.vertical_position = 'middle'
        self.horizontal_position = 'center'
        self.font_family = 'Arial Unicode MS'
        self.font_style = None
        self.layer = 'above'

        self.mode = None
        self.text = ''
        self.image = ''
        self.pages = ''
        self.vertical_position_adjustment = 0
        self.horizontal_position_adjustment = 0
        self.mosaic = False
        self.rotation = 0
        self.font_size = 14
        self.font_color = '#000000'
        self.transparency = 100

        super(Watermark, self).__init__(public_key, True, verify_ssl)

    @property
    def allowed_properties(self):
        return ['vertical_position', 'horizontal_position', 'font_family', 'font_style', 'layer', 'mode', 'text',
                'image', 'pages', 'vertical_position_adjustment', 'horizontal_position_adjustment', 'mosaic',
                'rotation', 'font_size', 'font_color', 'transparency']

    @property
    def vertical_position_values(self):
        return 'bottom', 'top', 'middle'

    @property
    def horizontal_position_values(self):
        return 'left', 'center', 'right'

    @property
    def font_family_values(self):
        return 'Arial', 'Arial Unicode MS', 'Verdana', 'Courier', 'Times New Roman', \
               'Comic Sans MS', 'WenQuanYi Zen Hei', 'Lohit Marathi'

    @property
    def font_style_values(self):
        return None, 'Bold', 'Italic'

    @property
    def layer_values(self):
        return 'above', 'below'

    def process(self):

        payload = super(Watermark, self).process()
        payload = self.as_dict(payload, self.allowed_properties)

        return payload






