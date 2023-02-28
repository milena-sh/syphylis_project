import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np


rosstat_df: pd.DataFrame = pd.read_csv(
    'rosstat_data.csv',
    index_col=0,
    header=None,
)
rosstat_line: plt.Axes = rosstat_df.plot.line(
    legend=False,
    xlabel='Год',
    ylabel='Число заболевших на 100к',
    title='Данные Росстата по заболеваемости сифилисом',
)

plt.figure()

interest_countries: dict[str, str] = {
    'RUS': 'Россия',
    'KAZ': 'Казахстан',
    'UKR': 'Украина',
    'GEO': 'Грузия',
    'BLR': 'Беларусь',
    'LVA': 'Латвия',
    'TJK': 'Таджикистан',
    'CIS': 'СНГ',
}

hfa_df: pd.DataFrame = pd.read_csv(
    'hfa_data.csv',
    header=None,
    names=['Страна', 'Группа стран', 'Год', 'Число заболевших на 100к'],
    usecols=[0, 1, 3, 4],
    index_col=2,
)
# Добавляем значение СНГ в столбик "Страна", чтобы было легко добавить СНГ на график
hfa_df['Страна'] = np.where((hfa_df['Группа стран'] == 'CIS'), hfa_df['Группа стран'], hfa_df['Страна'])

interest_countries_df: pd.DataFrame = hfa_df[
    hfa_df['Страна'].isin(interest_countries.keys())
]
interest_countries_df = interest_countries_df.sort_values(['Число заболевших на 100к'], ascending=False)
interest_countries_df = interest_countries_df.replace({'Страна': interest_countries})

sns.lineplot(
    interest_countries_df,
    x='Год',
    y='Число заболевших на 100к',
    hue='Страна',
).set(xlabel='Год', ylabel='Число заболевших на 100к', title='Данные HFA по заболеваемости сифилисом')

plt.show()
