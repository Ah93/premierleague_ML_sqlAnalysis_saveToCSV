import mysql.connector
import pandas as pd

#Prepare Mysql connection and query
connection = mysql.connector.connect(host='localhost',
                                         database='pl_data',
                                         user='root',
                                         password='')
mycursor = connection.cursor()
cName = input("Enter club name: ")
# res = mycursor.execute("select sum(Pld) as Pld, sum(W) as W, sum(D) as D, sum(L) as L, sum(Pts) as Pts, sum(F) as F from pldata where team = %s", ("%" + cName + "%",))
mycursor.execute("select sum(Pld) as Pld, sum(W) as W, sum(D) as D, sum(L) as L, sum(Pts) as Pts, sum(F) as F from pldata where team LIKE %s", ("%" + cName + "%",))
res = mycursor.fetchall()

#Fetch columns
for row in res:
    n_pldg = row[0]

    n_win = row[1]

    n_draw = row[2]

    n_loss = row[3]

    n_goals = row[4]


#Calculate win_rate, lose_rate and draw_rate througout past 30 years 
win_rate = (n_win) / (n_pldg) * 100

lose_rate = (n_loss) / (n_pldg) * 100

draw_rate = (n_draw) / (n_pldg) * 100

# #Print out the results
print("Number of games played past 30 seasons: ", (n_pldg))
print("Number of win games past 30 seasons: ", (n_win))
print("Number of draw games past 30 seasons: ", (n_draw))
print("Number of loss games past 30 seasons: ", (n_loss))
print("Number of goals past 30 seasons: ", (n_goals))
print("----------------------------------------------------------------")
print("Win rate is: ", float(win_rate))
print("Loss rate is: ", float(lose_rate))
print("Draw rate is: ", float(draw_rate))
