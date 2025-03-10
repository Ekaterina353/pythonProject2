import logging
import os

LOG_DIR = 'logs'
LOG_FILE = os.path.join(LOG_DIR, 'masks.log')

# Создаем директорию для логов, если ее нет
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Настраиваем логгер
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,  # Уровень логирования: INFO, DEBUG, WARNING, ERROR, CRITICAL
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filemode='w'  # 'w' - перезаписывать файл при каждом запуске
)

logger = logging.getLogger(__name__)


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты."""
    logger.info(f"Вызвана функция get_mask_card_number с card_number: {card_number}")
    try:
        if len(card_number) != 16 or not card_number.isdigit():
            logger.error(f"Неверный номер карты: {card_number}. Номер карты должен состоять из 16 цифр.")
            raise ValueError("Номер карты должен состоять из 16 цифр")

        masked_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        logger.info(f"Номер карты успешно замаскирован. Результат: {masked_card}")
        return masked_card

    except ValueError as e:
        logger.exception(f"Ошибка при маскировании номера карты: {e}")
        raise


def get_mask_account(account_number: str) -> str:
    """Маскирует номер банковского счета."""
    logger.info(f"Вызвана функция get_mask_account с account_number: {account_number}")
    try:
        if len(account_number) < 4 or not account_number.isdigit():
            logger.error(f"Неверный номер счета: {account_number}. Номер счета должен состоять минимум из 4 цифр.")
            raise ValueError("Номер счета должен состоять минимум из 4 цифр")

        masked_account = f"**{account_number[-4:]}"
        logger.info(f"Номер счета успешно замаскирован. Результат: {masked_account}")
        return masked_account
    except ValueError as e:
        logger.exception(f"Ошибка при маскировании номера счета: {e}")
        raise
