import os
import pytest
import tempfile

@pytest.fixture
def tmp_file():
    def create():
        temp = tempfile.NamedTemporaryFile(delete=False)
        return temp.name
    return create

def test_file(tmp_file):
    path = tmp_file()
    assert os.path.exists(path)

"""
Ámbito de módulo

@pytest.fixture(scope="module")
def tmp_file():
    def create(contents):
        temp = tempfile.NamedTemporaryFile(delete=False)
        return temp.name
    return create
"""

"""
Ámbito de módulo
Limpieza

@pytest.fixture(scope="module")
def tmp_file(request):
    temp = tempfile.NamedTemporaryFile(delete=False)
    def create():
        return temp.name

    def cleanup():
        os.remove(temp.name)

    request.addfinalizer(cleanup)
    return create
"""