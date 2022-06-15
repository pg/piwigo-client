import json
from pathlib import Path

import pytest


@pytest.fixture(scope="function")
def json_response(request):
    return json.loads(
        Path(f"tests/fixtures/{request.function.__name__}.json").read_bytes()
    )
