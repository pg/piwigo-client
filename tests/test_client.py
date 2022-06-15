import pytest
from pytest_httpx import HTTPXMock

from piwigo import PiwigoClient, PiwigoError


def test_invalid_username(httpx_mock: HTTPXMock, json_response):
    httpx_mock.add_response(json=json_response)

    with pytest.raises(PiwigoError, match="Invalid username/password"):
        PiwigoClient("https://fake", "bad_user", "pw")
