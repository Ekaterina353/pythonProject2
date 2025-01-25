from src.masks import get_mask_account, get_mask_card_number

def mask_account_card(info: str) -> str:
    """
    Маскирует номер карты или счета в зависимости от типа.

    :param info: Строка, содержащая тип и номер карты или счета.
    :return: Строка с замаскированным номером.
    """
    if "Счет" in info:
        account_number = info.split()[-1]
        return f"Счет {get_mask_account(account_number)}"
    else:
        card_number = info.split()[-1]
        return f"{' '.join(info.split()[:-1])} {get_mask_card_number(card_number)}"


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата "YYYY-MM-DDTHH:MM:SS.ssssss" в "DD.MM.YYYY".

    :param date_str: Строка с датой в формате "YYYY-MM-DDTHH:MM:SS.ssssss".
    :return: Строка с датой в формате "DD.MM.YYYY".
    """
    date_part = date_str.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"