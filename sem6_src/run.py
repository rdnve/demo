import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plot
import numpy as np

def main():
    df = pd.read_csv("1russian_demo(1).csv", sep=";")
    df.head()

    # 1. Вынесите отдельно от таблицы среднее по npg (прирост населения) и gdw (количество трудоспособного населения) для
    # каждого региона.
    avg = df.groupby("region")[["npg", "gdw"]].mean().reset_index()
    print(avg)

    # 2. Посчитайте для этих столбцов X-Mx, Y-My, (X-Mx)^2, (Y-My)^2, (X-Mx)(Y-My)
    mean_npg = df["npg"].mean()
    mean_gdw = df["gdw"].mean()

    df["X-Mx"] = df["npg"] - mean_npg
    df["Y-My"] = df["gdw"] - mean_gdw
    df["(X-Mx)^2"] = df["X-Mx"] ** 2
    df["(Y-My)^2"] = df["Y-My"] ** 2
    df["(X-Mx)(Y-My)"] = df["X-Mx"] * df["Y-My"]

    res_col = ["region", "X-Mx", "Y-My", "(X-Mx)^2", "(Y-My)^2", "(X-Mx)(Y-My)"]
    res_df = df[res_col].drop_duplicates()
    print(res_df.head())

    # 3. Вычислите на основе этих подсчетов коэффициент корреляции.
    # я заюзал это https://habr.com/ru/articles/557998/
    sum_npg_gdw = df['(X-Mx)(Y-My)'].sum()
    sum_square = df['(X-Mx)^2'].sum()
    sum_square2 = df['(Y-My)^2'].sum()

    print(sum_npg_gdw / ((sum_square * sum_square2) ** 0.5))

    # 4. С помощью надстройки для анализа данных посчитайте матрицу корреляции для столбцов: npg, birth_rate, death_rate,
    # gdw, urbanization.
    raw_mattr = df[['npg', 'birth_rate', 'death_rate', 'gdw', 'urbanization']].corr()
    print(raw_mattr)

    x, y = df['npg'], df['gdw']

    plot.figure(figsize=[12, 8])
    sns.regplot(x=x, y=y, scatter_kws={'alpha':0.6}, line_kws={"color": "blue"})
    plot.title("диаграмма с линией тренда между npg и gdw")
    plot.xlabel("Прирост npg")
    plot.ylabel("количество gdw")
    plot.show()


if __name__ == "__main__":
    main()
