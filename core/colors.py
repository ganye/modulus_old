class Color:
    def __init__(self):
        self.enable()

    def disable(self):
        self.bold = ''
        self.underline = ''

        self.white = ''
        self.black = ''

        self.dark_red = ''
        self.red = ''
        self.red_bg = ''
        self.light_red = ''
        
        self.dark_green = ''
        self.green = ''
        self.green_bg = ''
        self.light_green = ''

        self.dark_yellow = ''
        self.yellow = ''
        self.yellow_bg = ''
        self.light_yellow = ''

        self.dark_blue = ''
        self.blue = ''
        self.blue_bg = ''
        self.light_blue = ''

        self.dark_purple = ''
        self.purple = ''
        self.purple_bg = ''
        self.light_purple = ''

        self.dark_cyan = ''
        self.cyan = ''
        self.cyan_bg = ''
        self.light_cyan = ''

    def enable(self):
        self.bold = '\033[1m'
        self.underline = '\033[4m'

        self.white = '\033[0m'
        self.black = '\033[30m'

        self.dark_red = '\033[31m'
        self.red = '\033[91m'
        self.red_bg = '\033[41m'
        self.light_red = '\033[101'
        
        self.dark_green = '\033[32m'
        self.green = '\033[92m'
        self.green_bg = '\033[42m'
        self.light_green = '\033[102m'

        self.dark_yellow = '\033[33m'
        self.yellow = '\033[93m'
        self.yellow_bg = '\033[43m'
        self.light_yellow = '\033[103m'

        self.dark_blue = '\033[34m'
        self.blue = '\033[94m'
        self.blue_bg = '\033[44m'
        self.light_blue = '\033[104m'

        self.dark_purple = '\033[35m'
        self.purple = '\033[95m'
        self.purple_bg = '\033[45m'
        self.light_purple = '\033[105m'

        self.dark_cyan = '\033[36m'
        self.cyan = '\033[96m'
        self.cyan_bg = '\033[46m'
        self.light_cyan = '\033[106m'