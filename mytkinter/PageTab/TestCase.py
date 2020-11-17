
class TestCase:
    param_name = None
    def __init__(self):
        self.param_name = None

    def set_param_name(self, p_name):
        self.param_name=p_name

    def get_param_name(self):
        return self.param_name