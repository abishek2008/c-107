import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import csv

df=pd.read_csv('studentlevel_data.csv')
print(df.groupby("level")["attempt"].mean())

fig=go.Figure(go.Scatter(
    x=["Level 1","Level 2","Level 3","Level 4"],
    y=df.groupby("level")['attempt'].mean(),
))

fig.show()