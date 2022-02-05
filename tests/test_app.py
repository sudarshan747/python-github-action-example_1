from app import index


def test_index():
    assert index() == "Hello, world! from Heroku cloud"
