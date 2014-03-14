class BaseOption(object):
    def __init__(self, is_required, info, value=None):
        self.is_required = is_required
        self.info = info
        self.value = value