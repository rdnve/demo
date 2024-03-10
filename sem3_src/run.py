import typing as ty
from openpyxl import load_workbook


def value_to_float(x):
    if isinstance(x, (float, int)):
        return x
    if "K" in x:
        if len(x) > 1:
            return float(x.replace("K", "")) * 1000
        return 1000.0
    if "M" in x:
        if len(x) > 1:
            return float(x.replace("M", "")) * 1000000
        return 1000000.0
    if "B" in x:
        return float(x.replace("B", "")) * 1000000000
    try:
        return float(x)
    except ValueError:
        return 0.0


def main():
    wb = load_workbook("youtube.xlsx")
    ws = wb.active

    need_to_convert = {
        "Subscribers",
        "avg views",
        "avg likes",
        "avg comments"
    }

    headers = []
    data = []
    for i, x in enumerate(ws.rows):
        if i == 0:
            for idx, c in enumerate(x[1 : len(x)]):
                headers.append(c.value)
            continue

        raw = {}
        for idx, c in enumerate(x[1 : len(x)]):
            # 1. Переведите текстовые данные в колонках Subsсribers, AvgViews, AvgLikes, AvgComments в числа.
            key = headers[idx]
            if key in need_to_convert:
                v = value_to_float(c.value)
            else:
                v = c.value
            raw[key] = v
        data.append(raw)

    # 2. На отдельном листе (или в отдельной переменной в Python) создайте таблицу, в которой посчитаете количество
    # видео по жанрам:
    genres_raw = "Animation,Daily vlogs,Humor,Movies,Music & Dance,News & Politics,Toys,Video games"
    genres_raw = {k:0 for k in set(genres_raw.split(","))}
    for i, x in enumerate(data):
        genre = x["Category"]
        if genre in genres_raw:
            genres_raw[genre] += 1

    for genre, count in genres_raw.items():
        print(f"{genre} - {count}")



if __name__ == "__main__":
    main()
