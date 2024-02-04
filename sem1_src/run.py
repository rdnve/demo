import os
import typing as ty

import pandas as pd

if ty.TYPE_CHECKING:
    from pandas.core.frame import DataFrame

FILENAME: str = "ASIA-GDP(1).csv"
if not os.path.exists(FILENAME):
    raise FileNotFoundError(
        f"Файл {FILENAME} не найден, положите его рядом "
        f"с кодом и запустите снова скрипт (или укажите полный путь)."
    )

kwargs: ty.Dict[str, ty.Any] = dict(
    filepath_or_buffer=FILENAME,
    # 1. Откройте файл в формате .csv и выберите нужный разделитель
    delimiter="|",
    # 2. Дайте название колонкам "RegionalMember","Year","GDP growth", "Subregion";
    names=["RegionalMember", "Year", "GDP growth", "Subregion"],
    # 3. Настройте десятичный разделитель – точка (.);
    decimal=".",
)

df: "DataFrame" = pd.read_csv(**kwargs)
df = df.reset_index()

# 4. Сделайте срез данных по региону "The Pacific";
df = df.query("Subregion == 'The Pacific'")

# 5. В этом срезе сделайте срез данных только за 2017 год;
df = df[df["Year"].str.startswith("2017")]

# 6. Отсортируйте в порядке возрастания данные в колонке "GDP Growth";
df = df.sort_values(by="GDP growth", ascending=True)

# 7. Отсортируйте в порядке убывания данные в колонке "RegionalMember";
df = df.sort_values(by="RegionalMember", ascending=False)

# 8. В полученном срезе посчитайте средний процент в пункте "GDP Growth".
avg_gdp_growth: float = df["GDP growth"].mean()

# 9. Посчитайте медиану "GDP Growth" для всех стран Центральной Азии (Central Asia) за 2020 год.
df: "DataFrame" = pd.read_csv(**kwargs)
df = df.reset_index()

df = df[df["Year"].str.startswith("2020")]
df = df.query("Subregion == 'Central Asia'")
median_gdp_growth: float = df["GDP growth"].median()
