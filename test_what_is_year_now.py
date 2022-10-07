from unittest.mock import patch, MagicMock
import json
import pytest
from what_is_year_now import what_is_year_now

JSON_STR_FORMAT_1 = '{"$id":"1","currentDateTime":"2022-10-06T14:43Z","utcOffset":"00:00:00","isDayLightSavingsTime":false,"dayOfTheWeek":"Thursday","timeZoneName":"UTC","currentFileTime":133095409866323607,"ordinalDate":"2022-279","serviceResponse":null}'
JSON_STR_FORMAT_2 = '{"$id":"1","currentDateTime":"01.03.2022T14:43Z","utcOffset":"00:00:00","isDayLightSavingsTime":false,"dayOfTheWeek":"Thursday","timeZoneName":"UTC","currentFileTime":133095409866323607,"ordinalDate":"2022-279","serviceResponse":null}'
JSON_STR_FORMAT_ERR = '{"$id":"1","currentDateTime":"2022.01.03T14:43Z","utcOffset":"00:00:00","isDayLightSavingsTime":false,"dayOfTheWeek":"Thursday","timeZoneName":"UTC","currentFileTime":133095409866323607,"ordinalDate":"2022-279","serviceResponse":null}'

@pytest.mark.parametrize("test_json_str",[JSON_STR_FORMAT_1,JSON_STR_FORMAT_2])
def test_wiyn_load_cases(test_json_str):
    test_json = json.loads(test_json_str)
    mock = MagicMock( side_effect = [test_json])
    with patch("what_is_year_now.urllib.request.urlopen") as test_resp:
        with patch("json.load", mock) as test_json_load:
            test_json_load.get.return_value.text = test_json_str
            assert what_is_year_now() == 2022

@pytest.mark.parametrize("test_json_str",[JSON_STR_FORMAT_ERR])
def test_wiyn_load_cases_error(test_json_str):
    test_json = json.loads(test_json_str)
    mock = MagicMock( side_effect = [test_json])
    with patch("what_is_year_now.urllib.request.urlopen") as test_resp:
        with patch("json.load", mock) as test_json_load:
            test_json_load.get.return_value.text = test_json_str
            with pytest.raises(ValueError):
                what_is_year_now()