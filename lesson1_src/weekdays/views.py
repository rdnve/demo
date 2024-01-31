import typing as ty

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

WEEKDAYS: ty.Dict[str, str] = dict(
    monday="Пн-день тяжелый",
    tuesday="Вт-буду учится",
    wednesday="Ср-ух, уже среда",
    thursday="Чт-почти пятница",
    friday="Пт-уже пятница!",
    saturday="Сб-почти конец недели",
    sunday="Вс-последний день отдыха",
)


def get_weekday(request: HttpRequest, weekday: str) -> HttpResponse:
    """Простая вьюшка"""

    result: ty.Optional[str] = WEEKDAYS.get(weekday)
    if result is None:
        result = (
            f"Вы ввели какой-то день странный `{weekday}`, "
            f"такого нет.<br />Попробуйте один из этих: "
            f"{', '.join(WEEKDAYS.keys())}."
        )

    return HttpResponse(content=result)
