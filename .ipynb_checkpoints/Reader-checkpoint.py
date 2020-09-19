import pandas as pd
import numpy as np

dfdata = pd.read_csv('file.csv', sep=';',header=18, encoding="utf_8",skip_blank_lines=True)

dfdata.

#usecols=['Дата транзакции','Операция','Сумма','Валюта','Дата операции по счету','Комиссия/Money-back','Обороты по счету','Цифровая карта','Категория операции']