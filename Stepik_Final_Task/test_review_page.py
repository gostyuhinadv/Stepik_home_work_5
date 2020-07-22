import pytest
from pages.review_page import ReviewPage

@pytest.mark.xfail
@pytest.mark.need_review_custom_scenarios
def test_write_review_by_guest(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/reviews/add/#addreview"
    page = ReviewPage(browser, link)
    page.open()
    page.write_review()
