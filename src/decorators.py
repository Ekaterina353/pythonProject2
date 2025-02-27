import functools
import logging


def log(filename=None):
    """
    Декоратор для логирования работы функции, ее аргументов и результатов.

    :param filename: Имя файла для записи логов. Если None, логи выводятся в консоль.
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logger = logging.getLogger(func.__name__)
            logger.setLevel(logging.INFO)

            if filename:
                file_handler = logging.FileHandler(filename)
                formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
                file_handler.setFormatter(formatter)
                logger.addHandler(file_handler)
            else:
                stream_handler = logging.StreamHandler()
                formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # Added timestamp
                stream_handler.setFormatter(formatter)
                logger.addHandler(stream_handler)

            try:
                result = func(*args, **kwargs)
                logger.info(f"{func.__name__} ok. Result: {result}")
                return result
            except Exception as e:
                logger.error(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")
                raise  # Re-raise the exception after logging

        return wrapper

    return decorator
