import pytest


@pytest.fixture
def method_under_test():
    """Return the method under test"""
    from hardpoints import mod_mech_hardpoints
    return mod_mech_hardpoints

@pytest.fixture
def json():
    """Return a json module"""
    import json
    return json

@pytest.fixture
def parse_test_data_json_folder(json):
    def _parse_test_data_json_folder(folder_name, json_parse=True):
        from pathlib import Path
        
        test_file_dir = Path(__file__).parent.resolve()
        test_data_folder = test_file_dir.joinpath( "..", "test-data", folder_name).resolve()

        test_data = {}
        for afile in test_data_folder.iterdir():
            if afile.is_file() and afile.suffix == ".json":
                with open(afile) as json_data: 
                    try:
                        if json_parse:
                            test_data[afile.name] = json.loads(json_data.read())
                        else:
                            test_data[afile.name] = json_data.read()
                    except json.decoder.JSONDecodeError as e:
                        print("Error parsing {}/{} -- <{}>".format(folder_name, afile.name, afile))
                        raise e
                    json_data.close()
        return test_data

    return _parse_test_data_json_folder


def test_hardpoint_generation(method_under_test, parse_test_data_json_folder):
    """Loops through JSON in test-data/hardpoints/input and ensures that what gets returned is from """
    hardpoint_test_input = parse_test_data_json_folder("input")
    hardpoint_test_output = parse_test_data_json_folder("output", False)

    for chassis_filename, chassisdef in hardpoint_test_input.items():
        modded_value = method_under_test(chassisdef)
        error_msg = "Given test-data/{} input does not match test-data/{} \\\\ Return value = <{}>".format(chassis_filename, chassis_filename, modded_value)
        assert modded_value == hardpoint_test_output[chassis_filename], error_msg