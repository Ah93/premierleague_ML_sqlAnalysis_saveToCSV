import mysql.connector
import pandas as pd

connection = mysql.connector.connect(host='localhost',
                                         database='pl_data',
                                         user='root',
                                         password='')
cursor = connection.cursor()

query = "select W, D, L, Pts, F, team from pldata"
cursor.execute(query)

myallData = cursor.fetchall()

all_win = []
all_draws = []
all_loss = []
all_pts = []
all_goals = []
all_teams = []
for  W,D,L,Pts,F,team in myallData:
    all_win.append(W)
    all_draws.append(D)
    all_loss.append(L)
    all_pts.append(Pts)
    all_goals.append(F)
    all_teams.append(team)

#we need to store this data to CSV
dic = {'Win' : all_win , 'Draw':all_draws, 'Loss':all_loss, 'Points':all_pts, 'Goals Scored':all_goals, 'team':all_teams}
df = pd.DataFrame (dic)
df_csv = df.to_csv('C:\PL_ML\PL_Data.csv')