class BaseModule(object):
    def __init__(self, console):
        self.info = {}
        self.options = []
        self.console = console
        
        self.initialize()
        
    def initialize(self):
        raise NotImplementedError()
    
    def run(self):
        raise NotImplementedError()
    
    def update_info(self, info):
        for key, value in info.items():
            self.info[key] = value
            
    def set_options(self, options):
        for key, value in options.items():
            setattr(self, key, value)
            self.options.append(key)
            
    def set(self, key, value):
        option = getattr(self, key)
        option.value = value
        
    @property
    def help(self):
        for key in self.options:
            option = getattr(self, key)
            self.console.writeln("|-- %s%s" % (key.ljust(16), option.help))