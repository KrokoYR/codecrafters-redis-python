from app.resp.datatypes.array_dt import ArrayDatatype
from app.resp.datatypes.bulk_string_dt import BulkStringDatatype
from app.resp.datatypes.error_dt import ErrorDatatype
from app.resp.datatypes.integer_dt import IntegerDatatype
from app.resp.datatypes.simple_string_dt import SimpleStringDatatype

CRLF = '\r\n'

data_types = {
    '*': ArrayDatatype(),
    '$': BulkStringDatatype(),
    '-': ErrorDatatype(),
    ':': IntegerDatatype(),
    '+': SimpleStringDatatype(),
}
keys = list(data_types.keys())


class Resp:
    @staticmethod
    def _map_to_command(input_str: str):
        return input_str

    def _parse(self, input_str: str):
        if any(input_str.startswith(key) for key in keys):
            data_types['*'].parse(input_str)
        else:
            self._map_to_command(input_str)

    def parse_input(self, input_str: str):
        chunks = input_str.split(CRLF)
        for chunk in chunks:
            self._parse(input_str)
