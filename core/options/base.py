class BaseOption(object):
    def __init__(self, is_required, info, value=None):
        self.is_required = is_required
        self.info = info
        self.value = value
        
    @property
    def info(self):
        return self.info
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = value
        
    @property
    def is_required(self):
        return self.is_required