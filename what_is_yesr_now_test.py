from unittest.mock import patch, MagicMock
import json
from what_is_year_now import what_is_year_now

SAMPLE_JSON_STR = '{"$id":"1","currentDateTime":"2022-10-06T14:43Z","utcOffset":"00:00:00","isDayLightSavingsTime":false,"dayOfTheWeek":"Thursday","timeZoneName":"UTC","currentFileTime":133095409866323607,"ordinalDate":"2022-279","serviceResponse":null}'

def test_wiyn_load_cases():
    test_json = json.loads(SAMPLE_JSON_STR)
    mock = MagicMock( side_effect = [test_json])
    with patch("what_is_year_now.urllib.request.urlopen") as test_resp:
        with patch("json.load", mock) as test_json_load:
            test_json_load.get.return_value.text = SAMPLE_JSON_STR
            assert what_is_year_now() == 2022
        
test_wiyn_load_cases()