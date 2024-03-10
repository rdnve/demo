import csv
import statistics
import typing as ty


def main():
    data: ty.List[ty.Dict[str, ty.Any]] = []
    with open("MovieData.csv", "r", encoding="cp1252") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            raw = {}
            for k, v in row.items():
                if str(v).isdigit():
                    v = int(v)
                raw[k] = v
            data.append(raw)


    headers = list(data[0].keys())
    headers.extend(
        [
            "Mean Value",
            "Good Comedy",
            "adults_only",
            "Wishlist",
        ]
    )

    for i, x in enumerate(data):
        imdb, rotten = float(x["IMDb"]), float(x["Rotten Tomatoes"])

        # 1. Создайте столбец Mean Value, где будет средняя оценка фильма с IMDb и Rotten Tomatoes по 100-балльной
        # шкале;
        mean_value = statistics.mean([imdb * 10, rotten])

        # 4. Создайте переменную Wishlist, в котором будет:
        wishlist = "Must watch"
        if mean_value < 40:
            wishlist = "Trash"
        elif 41 <= mean_value <= 60:
            wishlist = "Normal"
        elif 61 <= mean_value <= 79:
            wishlist = "Good"

        x.update(
            {
                "Mean Value": mean_value,
                # 2. Создайте переменную Good Comedy, в котором будет 1, если фильм comedy c оценкой выше 8 по IMDb.
                # В противном случае 0.
                "Good Comedy": 1 if imdb > 8 else 0,
                # 3. Создайте переменную adults_only, в котором будет 1, если фильм "18+". В противном случае 0. Если
                # в столбце ничего нет, то в столбец ничего не ставится.
                "adults_only": 1 if x.get("Rating", "") == "18+" else 0,
                # 4. Создайте переменную Wishlist, в котором будет: (расчет выше)
                "Wishlist": wishlist,
            }
        )

    print(
        "5. Выведите фильмы, удовлетворяющие следующим условиям: Good Comedy - 1, Wishlist - Must watch, "
        "Adults only - 0"
    )
    already_showed = set()
    for i, x in enumerate(data):
        title = x["Title"]

        if (
            x["Good Comedy"] == 1
            and x["Wishlist"] == "Must watch"
            and x["adults_only"] == 0
        ):
            if title not in already_showed:
                print(f" - {title}")
                already_showed.add(title)

    print("\n6.Какая комедия удовлетворяет следующим условиям? Good Comedy - 1, Wishlist - Must watch, Adults only - 1, "
          "Amazon Prime Video - 1")
    already_showed = set()
    for i, x in enumerate(data):
        title = x["Title"]

        if (
            x["Good Comedy"] == 1
            and x["Wishlist"] == "Must watch"
            and x["adults_only"] == 1
            and x["Amazon Prime Video"] == 1
        ):
            if title not in already_showed:
                print(f" - {title}")
                already_showed.add(title)


if __name__ == "__main__":
    main()
