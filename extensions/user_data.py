from loader import curr_list
from config_data.resources import Msgs
from extensions.errors import NotCurrencyError, AmbiguousCurrencyError


class UserData:

    def __init__(self, user_id: int, base: str, quote: str, amount: int) -> None:
        self.user_id = user_id
        self.base = base
        self.base_code = ""
        self.quote = quote
        self.quote_code = ""
        self.amount = amount
        self.curr_list = None

    def get_codes(self) -> None:
        if self.base_code == "":
            self.base_code = self.__get_code(self.base)
        if self.quote_code == "":
            self.quote_code = self.__get_code(self.quote)

    def __get_code(self, name: str) -> str:
        currs: list = curr_list.get(name)
        if not currs:
            raise NotCurrencyError(Msgs.ERROR_CURRENCY_NOT_FOUND.format(name))
        if len(currs) > 1:
            cur_list = "\n".join(["{0}. {1} - {2}".format(i + 1, val[0], val[1]) for i, val in enumerate(currs)])
            msg = "{0}\n{1}\n{2}".format(Msgs.ERROR_AMBIGUOUS_CURRENCY.format(name), cur_list, Msgs.SELECT)
            self.curr_list = currs
            raise AmbiguousCurrencyError(msg)
        return currs[0][0]