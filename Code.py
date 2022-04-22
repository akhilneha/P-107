import pandas as pd
import csv
import plotly.graph_objects as pg

df = pd.read_csv("Data.csv")
print(df.groupby("level")["attempt"].mean())

fig = pg.Figure(pg.Scatter(
    x = df.groupby("level")["attempt"].mean(),
    y = ['Level 1','Level 2','Level 3','Level 4'],orientation = 'h'
))

fig.show()