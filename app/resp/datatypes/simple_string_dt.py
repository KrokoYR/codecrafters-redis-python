from app.resp.datatypes.base_datatype import BaseDatatype


class SimpleStringDatatype(BaseDatatype):
    def build_response(self):
        return ''

    def parse(self, input_str: str):
        return ''
