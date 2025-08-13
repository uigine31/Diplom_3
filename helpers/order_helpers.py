import allure

def validate_order_counters(feed_page):
    """Вспомогательная функция для проверки счётчиков заказов"""
    counters = {
        "Общее количество заказов": feed_page.get_total_orders_count(),
        "Количество заказов за сегодня": feed_page.get_today_orders_count()
    }
    
    for name, value in counters.items():
        assert value is not None and value >= 0, f"{name} отсутствует или меньше 0"