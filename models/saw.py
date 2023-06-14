from models.exceptions import AlreadyIsException
from abc import ABC, abstractmethod
import logging


def exception_logger(mode):
    def decorator(func):
        def wrapper(*args):
            try:
                return func(*args)
            except AlreadyIsException as e:
                if mode == "file":
                    logging.basicConfig(filename="exceptions.txt", level=logging.ERROR)
                    logging.error(e)
                elif mode == "console":
                    logging.basicConfig(level=logging.ERROR)
                    logging.error(e)
                else:
                    raise ValueError("Invalid logging mode")
        return wrapper
    return decorator


class Saw(ABC):
    """
    abstract class which describes all other types of saws which are also described in this project
    """
    def __init__(self, brand, power, worktime, types_of_supply, is_working=False):
        """
        :param brand: brand of saw
        :param power: power of saw in watts
        :param worktime: how much time (in hours) can this saw work
        :param types_of_supply: which types of supply are available for this saw
        :param is_working: is this saw working now
        """
        self.brand = brand
        self.power = power
        self.worktime = worktime
        self.types_of_supply = types_of_supply
        self.is_working = is_working

    def __getitem__(self, item):
        print(type(item), item)

    @abstractmethod
    def get_remaining_working_time(self):
        """
        :return: how much time in hours could this saw continue working
        """
        pass

    @exception_logger("file")
    def start(self):
        """
        make saw working
        if it already is, raises exception
        """
        if self.is_working:
            raise AlreadyIsException("Already works")
        else:
            self.is_working = True

    @exception_logger("console")
    def stop(self):
        """
        make saw not working
        if it already is, raises exception
        """
        if not self.is_working:
            raise AlreadyIsException("Already doesn't work")
        else:
            self.is_working = True
