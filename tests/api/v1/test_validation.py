import unittest
import datetime
from src.modules.helper import check_is_valid, decode_data, get_uuid, get_time


class TestValidation(unittest.TestCase):

    def setUp(self) -> None:
        self.placeholder = "Test"

    def test_good_case_is_valid(self):
        request = {"ident": 1}
        expected = None
        response = check_is_valid(id=request.get("ident"))
        self.assertIsNone(expected, response)

    def test_bad_case_is_valid(self):
        request = [{"ident": ""}, {"ident": None}]
        expected = "Following parameters should not be None or '':"

        for elm in request:
            response = check_is_valid(id=elm.get("ident"))
            self.assertIsNotNone(expected, response)

    def test_get_json_body_good_case(self):
        input_data = b"{\"ident\": 1}"
        output_error, output_data = decode_data(input_data)
        expected_output = (None, {'ident': 1})
        self.assertEqual((output_error, output_data), expected_output)

    def test_get_json_body_bad_case(self):
        input_data = b"this is not a valid dictionary"
        output_error, output_data = decode_data(input_data)
        self.assertIsNone(output_data)
        self.assertIsInstance(output_error, str)

    def test_get_uuid_datatype(self):
        self.assertIsInstance(get_uuid(), str)

    def test_get_time_datatype_utc(self):
        self.assertIsInstance(get_time(), datetime.datetime)

    def test_get_time_datatype_europe_berlin(self):
        self.assertIsInstance(get_time("Europe/Berlin"), datetime.datetime)


if __name__ == '__main__':
    unittest.main()
