from pylovepdf.task import Task


class Pagenumber(Task):

    def __init__(self, public_key, verify_ssl):

        self.facing_pages = False
        self.first_cover = False
        self.pages = 'all'
        self.starting_number = 1
        self.vertical_position = 'bottom'
        self.horizontal_position = 'center'
        self.vertical_position_adjustment = 0
        self.horizontal_position_adjustment = 0
        self.font_family = 'Arial Unicode MS'
        self.font_style = None
        self.font_size = 14
        self.font_color = '#000000'
        self.text = '{n}'

        self.tool = 'pagenumber'
        super(Pagenumber, self).__init__(public_key, True, verify_ssl)

    @property
    def allowed_properties(self):

        return ('facing_pages', 'first_cover', 'pages', 'starting_number', 'vertical_position', 'horizontal_position',
                'vertical_position_adjustment', 'horizontal_position_adjustment', 'font_family', 'font_size',
                'font_style', 'font_color', 'text')

    @property
    def vertical_position_values(self):
        return 'bottom', 'top'

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

    def process(self):

        payload = super(Pagenumber, self).process()
        payload = self.as_dict(payload, self.allowed_properties)

        return payload






