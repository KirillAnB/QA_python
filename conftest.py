import pytest


@pytest.fixture(params=[44,45,46])
def ultimate_param(request):
    return request.param

def pytest_addoption(parser):
    parser.addoption("--answer", action="store", default='42', help="The ultimate answer")

@pytest.fixture
def answer_gen(request):
    data = int(request.config.getoption("--answer"))
    yield data

