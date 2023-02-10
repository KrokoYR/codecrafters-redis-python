class BaseDatatype:
    def build_response(self):
        raise NotImplementedError()

    def parse(self, input_str: str):
        raise NotImplementedError()
