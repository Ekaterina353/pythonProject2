# src/processing/__init__.py
def filter_by_state(data, state='EXECUTED'):
    """
    Возвращает новый список словарей, содержащий только те словари,
    у которых ключ 'state' соответствует указанному значению.
    :param data: Список словарей.
    :param state: Строка с состоянием (по умолчанию 'EXECUTED').
    :return: Новый список словарей с отфильтрованными значениями.
    """
    return [item for item in data if item.get('state') == state]


def sort_by_date(data, reverse=True):
    """
    Возвращает новый список, отсортированный по дате ('date').
    :param data: Список словарей.
    :param reverse: Логическое значение, определяющее порядок сортировки (по умолчанию True - убывание).
    :return: Новый отсортированный список словарей.
    """
    return sorted(data, key=lambda x: x['date'], reverse=reverse)
