# QA Тестовое задание 
*Открытый доступ для работодателей*     

## Состав проекта

| Файл | Описание                                                                                                                                    |
|------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **`test-cases_payment.md`** | **Тест-кейсы оплаты**<br>Позитив/негатив/валидация/граничные/3DS<br>Формат: ID, Название, Приоритет, Предусловия, Шаги, Ожидаемый результат |
| **`test_title.py`** | **Playwright автотест**<br>Проверка заголовка playwright.dev<br>Chromium + Firefox (2 теста)                                                |
| **`test_chance.md`** | **Теория вероятностей**<br>Перебор + формула биномиального распределения                                                                    |
| **`requirements.txt`** |                                                                                                                                             |
| **`README.md`** |                                                                                                                                             |
| **`.gitignore`** |                                                                                                                                             |

## 🚀 Запуск
```bash
pip install -r requirements.txt
playwright install chromium firefox
python -m pytest test_title.py -v 
```
## Стек     
Python 3.11 + venv      
Playwright 1.58.0   
Pytest 9.0.2
macOS | PyCharm
