import typing as ty


def plural(value: int, quantitative: ty.List[str]) -> str:
    """Плюрализм!"""

    if value % 100 in (11, 12, 13, 14):
        return quantitative[2]
    if value % 10 == 1:
        return quantitative[0]
    if value % 10 in (2, 3, 4):
        return quantitative[1]

    return quantitative[2]
