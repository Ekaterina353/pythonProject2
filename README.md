# Bank Operations Widget

## Описание
Этот проект предоставляет функции для маскирования номеров банковских карт и ключей счета, а также для обработки данных о банковских операциях.

## Установка
- Убедитесь, что у вас установлен Python (3.7 или выше).
- Установите необходимые зависимости:

bash
pip install -r requirements.txt


## Использование
### Маскировка карт и счетов

python

from src.widget.py import mask_account_card
=======
from src.widget import mask_account_card



masked_card = mask_account_card("Visa Platinum 7000792289606361")
print(masked_card)


### Фильтрация операций

python

from src.processing.py import filter_by_state
=======
from src.processing import filter_by_state



filtered_data = filter_by_state(data, 'EXECUTED')


### Сортировка операций

python

from src.processing.py import sort_by_date
=======
from src.processing import sort_by_date



sorted_data = sort_by_date(data)



## Примеры


## Тестирование

Проект покрыт автоматическими тестами, использующими pytest.

### Запуск тестов

Для запуска всех тестов выполните следующую команду в корневой директории проекта:

bash
pytest


### Покрытие тестами

Общее покрытие тестами составляет [XX%]. Используйте команду `pytest --cov=your_module` (замените `your_module` на имя вашего модуля) для оценки покрытия.

### Типы тестов

*   **Модульные тесты:** Проверяют отдельные функции и классы.
*   **Интеграционные тесты:** Проверяют взаимодействие между различными модулями. (Если они у вас есть)

### Структура тестов

Тесты организованы в соответствии со структурой проекта. Для каждого модуля (`masks`, `widget`, `processing`) существует соответствующий файл тестов (`test_masks.py`, `test_widget.py`, `test_processing.py`, и т.д.).

### Фикстуры

Для упрощения написания тестов используются фикстуры pytest, предоставляющие тестовые данные и окружение.  Они определены в файле `conftest.py`.

=======
## Примеры

