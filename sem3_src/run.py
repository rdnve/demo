import os
import typing as ty

import pandas as pd

if ty.TYPE_CHECKING:
    from pandas.core.frame import DataFrame

FILENAME: str = "youtube.csv"
if not os.path.exists(FILENAME):
    raise FileNotFoundError(
        f"Файл {FILENAME} не найден, положите его рядом "
        f"с кодом и запустите снова скрипт (или укажите полный путь)."
    )


def value_to_float(x):
    if isinstance(x, (float, int)):
        return x
    if 'K' in x:
        if len(x) > 1:
            return float(x.replace('K', '')) * 1000
        return 1000.0
    if 'M' in x:
        if len(x) > 1:
            return float(x.replace('M', '')) * 1000000
        return 1000000.0
    if 'B' in x:
        return float(x.replace('B', '')) * 1000000000
    try:
        return float(x)
    except ValueError:
        return 0.0


kwargs: ty.Dict[str, ty.Any] = dict(
    filepath_or_buffer=FILENAME,
    delimiter=";",
    names=["index", "youtuber", "channel", "category", "subscribers", "country", "avg_views", "avg_likes", "avg_comments"],
    decimal=".",
    na_values={"nan": 0, "NaN": 0},
    keep_default_na=True,
)

df: "DataFrame" = pd.read_csv(**kwargs)
df = df.reset_index()
df = df.fillna(0)
