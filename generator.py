from random import randint, choice
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from typing import Optional

def __symbols__(
        lowercase: Optional[bool] = True,
        uppercase: Optional[bool] = True,
        digits_: Optional[bool] = True,
        punctuation_: Optional[bool] = True,
        exclude: Optional[str] = None
) -> list:
    symbols_list = list(
        (ascii_uppercase * uppercase)
        +
        (ascii_lowercase * lowercase)
        +
        (digits * digits_)
        +
        (punctuation * punctuation_)
    )

    if exclude:
        symbols_list = [symbol for symbol in symbols_list if not symbol in exclude]

    return symbols_list


def password(
        characters_list: list,
        length: int | None,
        min_length: int | None = 12,
        max_length: int | None = 20,
) -> str:
    if length is None:
        length = randint(min_length, max_length)

    if characters_list:
        return ''.join(choice(characters_list) for _ in range(length))
    else:
        return ""


def passwords(
        lowercase: Optional[bool] = True,
        uppercase: Optional[bool] = True,
        digits_: Optional[bool] = True,
        special: Optional[bool] = True,
        exclude: Optional[str] = None,
        length: Optional[int] = None,
        min_length: Optional[int] = 12,
        max_length: Optional[int] = 20,
        number: Optional[int] = 1,
) -> list[str]:
    symbols_list = __symbols__(
        lowercase=lowercase,
        uppercase=uppercase,
        digits_=digits_,
        punctuation_=special,
        exclude=exclude
    )

    return [
        password(symbols_list, length, min_length, max_length) for _ in range(number)
    ]
