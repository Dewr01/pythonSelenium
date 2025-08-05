# Автоматизация тестирования с Selenium (Stepik)

Выполнение практических заданий с курса **"Автоматизация тестирования с помощью Selenium и Python"** на Stepik.

## 📌 Особенности выполнения
1. **Формат заданий**:
   - Теоретические вопросы (выбор вариантов)
   - Написание Python-кода с использованием Selenium WebDriver
   - Автоматическая проверка решений на платформе

2. **Типовые задачи**:
   - Авторизация на тестовых страницах
   - Поиск элементов разными методами (ID, CSS, XPath)
   - Взаимодействие с формами и динамическими элементами
   - Работа с AJAX и ожиданием элементов

3. **Пример решения**:
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
...
button = browser.find_element(By.ID, "submit_button")
button.click()
browser.quit()
```
###🛠 Мои решения
Все задания выполнены на Python 3.x

Использованы паттерны Page Object для сложных задач

Реализованы кастомные ожидания для динамических элементов