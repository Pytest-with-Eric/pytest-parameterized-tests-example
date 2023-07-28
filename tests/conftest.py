import pytest

@pytest.fixture()
def user(name, username, password) -> dict:
    """Return a user object."""
    return {"name": name, "username": username, "password": password}