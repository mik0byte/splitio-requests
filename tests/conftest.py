import json
import pathlib

import pytest

from splitiorequests import AdminAPI


@pytest.fixture(scope="class")
def splits():
    splits_json_path = pathlib.Path(__file__).parent.joinpath('test_data').joinpath('splits.json')

    with open(str(splits_json_path), 'r') as file:
        splits_json = json.load(file)

    return splits_json


@pytest.fixture(scope="class")
def split_definitions():
    split_definitions_json_path = pathlib.Path(__file__).parent.joinpath('test_data').joinpath(
        'split_definitions.json')

    with open(str(split_definitions_json_path), 'r') as file:
        split_definitions_json = json.load(file)

    return split_definitions_json


@pytest.fixture(scope="class")
def environments():
    environments_json_path = pathlib.Path(__file__).parent.joinpath('test_data').joinpath('environments.json')

    with open(str(environments_json_path), 'r') as file:
        environments_json = json.load(file)

    return environments_json


@pytest.fixture(scope="class")
def workspaces():
    workspaces_json_path = pathlib.Path(__file__).parent.joinpath('test_data').joinpath('workspaces.json')

    with open(str(workspaces_json_path), 'r') as file:
        workspaces_json = json.load(file)

    return workspaces_json


@pytest.fixture(scope="class")
def traffic_types():
    traffic_types_json_path = pathlib.Path(__file__).parent.joinpath('test_data').joinpath('traffic_types.json')

    with open(str(traffic_types_json_path), 'r') as file:
        traffic_types_json = json.load(file)

    return traffic_types_json


@pytest.fixture(scope="class")
def tags():
    tags_json_path = pathlib.Path(__file__).parent.joinpath('test_data').joinpath('tags.json')

    with open(str(tags_json_path), 'r') as file:
        tags_json = json.load(file)

    return tags_json


@pytest.fixture(scope="class")
def admin_api():
    session = AdminAPI('verysecretkey')
    return session
