import allure
from pages.base_page import BasePage
from locators import MainPageLocators
from seletools.actions import drag_and_drop
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class MainPage(BasePage):

    @allure.step("Открываем главную страницу")
    def open_main_page(self):
        self.open()

    @allure.step("Переходим в раздел 'Конструктор'")
    def click_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Переходим в раздел 'Лента заказов'")
    def click_orders_feed(self):
        self.click(MainPageLocators.ORDERS_FEED_BUTTON)

    @allure.step("Кликаем по первому ингредиенту (булке)")
    def click_first_ingredient(self):
        self.js_click(MainPageLocators.BUN_INGREDIENT)

    @allure.step("Проверяем, что окно деталей ингредиента отображается")
    def is_ingredient_details_open(self):
        return self.is_displayed(MainPageLocators.INGREDIENT_DETAILS)

    @allure.step("Закрываем окно деталей ингредиента")
    def close_ingredient_details(self):
        # 1. Ждём исчезновения оверлея (если он есть)
        try:
            self.wait_for_invisibility(MainPageLocators.MODAL_OVERLAY)
        except Exception:
            pass  # Если оверлея нет — продолжаем
        # 2. Ждём кликабельности кнопки
        close_btn_locator = MainPageLocators.CLOSE_POP_UP_INGREDIENT_DETAILS_BUTTON
        self.wait_for_clickable(close_btn_locator)
        # 3. Обычный клик
        self.click(close_btn_locator)
        assert self.is_ingredient_details_closed(), "Модальное окно не закрылось после клика по крестику"

    def is_ingredient_details_closed(self):
        return self.is_not_displayed(MainPageLocators.INGREDIENT_DETAILS)

    @allure.step("Получаем счётчик ингредиента (булка)")
    def get_bun_ingredient_counter(self):
        text = self.find(MainPageLocators.COUNTER).text
        try:
            return int(text)
        except ValueError:
            return 0

    @allure.step("Добавляем булку в заказ (перетаскиваем булку в конструктор и закрываем модальное окно)")
    def add_bun_ingredient_to_order(self):
        source = self.find(MainPageLocators.BUN_INGREDIENT)
        target = self.find(MainPageLocators.CONSTRUCTOR_FIELD)
        drag_and_drop(self.driver, source, target)
        # Если после dnd появляется модальное окно с деталями, закрываем её
        if self.is_displayed(MainPageLocators.INGREDIENT_DETAILS, timeout=2):
            self.close_ingredient_details()

    @allure.step("Получаем номер созданного заказа")
    def get_order_id(self):
        return self.find(MainPageLocators.ORDER_ID).text.strip()

    @allure.step("Проверяем, отображается ли текст 'Соберите бургер'")
    def is_create_burger_text_displayed(self):
        return self.is_displayed(MainPageLocators.CREATE_BURGER_TEXT)
    
    @allure.step("Дожидаемся загрузки конструктора")
    def wait_for_constructor_loaded(self):
        """Дожидаемся загрузки главной страницы конструктора"""
        self.wait_for_visibility(MainPageLocators.CREATE_BURGER_TEXT)

    @allure.step("Ожидаем, что кнопка 'Оформить заказ' станет кликабельной")
    def wait_for_order_button_clickable(self, timeout=10):
        self.wait_for_clickable(MainPageLocators.ORDER_BUTTON, timeout)

    @allure.step("Ожидаем видимость поп-апа заказа")
    def wait_for_order_popup_visible(self, timeout=10):
        self.wait_for_visibility(MainPageLocators.ORDER_POP_UP, timeout)

    @allure.step("Ожидаем, что поп-ап заказа станет невидимым")
    def wait_for_order_popup_invisible(self, timeout=10):
        self.wait_for_invisibility(MainPageLocators.ORDER_POP_UP, timeout)