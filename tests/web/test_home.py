import pytest


@pytest.mark.web
@pytest.mark.smoke
def test_home_page(page):
    assert page.title() == "Swag Labs"