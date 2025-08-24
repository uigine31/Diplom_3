import allure
from pages.feed_page import FeedPage
from helpers.order_helpers import validate_order_counters

@allure.feature("Счётчики заказов")
class TestOrderCounter:

    @allure.story("Проверка счётчиков заказов")
    @allure.title("Проверяем, что счётчики 'Выполнено за всё время' и 'Выполнено за сегодня' отображаются")
    def test_order_counters_visibility(self, browser):
        feed_page = FeedPage(browser)
        feed_page.open_feed_page()
        
        with allure.step("Проверяем счётчики заказов"):
            validate_order_counters(feed_page)