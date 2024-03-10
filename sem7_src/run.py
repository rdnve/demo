import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plot


def main():
    df = pd.read_excel("russian_demo(2).xlsx")
    print(df.head())
    avg_birth = df.groupby('region')['birth_rate'].mean().reset_index()
    avg_birth_total = df['birth_rate'].mean()
    print(avg_birth)

    plot.figure(figsize=(10, 8))
    plot.plot(avg_birth['region'], avg_birth['birth_rate'], label='Средний уровень рождаемости в регионе', marker='o')
    plot.axhline(y=avg_birth_total, color='r', linestyle='-', label='Средний уровень рождаемости (общий)')

    plot.xticks(rotation=90)
    plot.ylabel('Средний уровень рождаемости')
    plot.title('Средний уровень рождаемости в регионах')
    plot.legend()
    plot.tight_layout()
    plot.show()

if __name__ == "__main__":
    main()



import pandas
import matplotlib.pyplot as p

df = pandas.read_excel("russian_demo(2).xlsx")
print(df.head())
avg_birth = df.groupby('region')['birth_rate'].mean().reset_index()
avg_birth_total = df['birth_rate'].mean()
print(avg_birth)

regions_above_avg_birth_rate = df[avg_birth['birth_rate'] > avg_birth_total]
print(regions_above_avg_birth_rate)

p.figure(figsize=(10, 8))
p.plot(avg_birth["region"], avg_birth["birth_rate"], label="Средний уровень рождаемости в регионе", marker="o")
p.axhline(y=avg_birth_total, linestyle='-', label='Средний уровень рождаемости')

p.xticks(rotation=90)
p.ylabel('Средний уровень рождаемости')
p.title('Средний уровень рождаемости в регионах')
p.legend()
p.tight_layout()
p.show()


regions_above_avg_birth_rate = df[avg_birth['birth_rate'] > avg_birth_total]
print(regions_above_avg_birth_rate)

# Merging the filtered regions with the original dataframe to calculate average death rate for these regions
avg_death_rate_for_filtered_regions = df[df['region'].isin(regions_above_avg_birth_rate['region'])].groupby('region')['death_rate'].mean().reset_index()

# Calculate the average death rate for the filtered regions
avg_death_rate_filtered_regions = avg_death_rate_for_filtered_regions['death_rate'].mean()
