def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты."""
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Номер карты должен состоять из 16 цифр")

    masked_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return masked_card


def get_mask_account(account_number: str) -> str:
    """Маскирует номер банковского счета."""
    if len(account_number) < 4 or not account_number.isdigit():
        raise ValueError("Номер счета должен состоять минимум из 4 цифр")

    masked_account = f"**{account_number[-4:]}"
    return masked_account
