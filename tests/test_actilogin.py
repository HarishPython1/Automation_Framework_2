import pytest
from pages.actitimeloginpage import ActiTimeloginPage

@pytest.mark.usefixtures("test_set_up")
class TestLogin:
    def test_login(self):
        driver=self.driver
        lp=ActiTimeloginPage(driver)
        lp.enter_user_name()
        lp.enter_pasword()
        lp.click_on_login_btn()