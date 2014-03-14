import re

from core.options.base import BaseOption
from core.excep import ModulusError

class MatchedOption(BaseOption):
    pattern = re.compile(r'.')
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self.validate(value)
        
    def validate(self, value):
        if value is None:
            return
        elif self.pattern.match(value):
            self._value = value
        else:
            raise ModulusError("'%s' is not a valid value." % value)