import pandas as pd
import datetime

data_log = open('data.log', 'w')

df_log = pd.read_csv("test.log", delimiter=' ', header=None, names=["Month", "Date", "Time", "Id", "Code", "State", "ON/OFF/ERR"])

unique_id = df_log["Id"].unique().tolist()

month_dict = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}
for uid in unique_id:
    df_temp = df_log.loc[df_log["Id"] == uid]
    a = -1
    b = -1
    f = 0
    f1 = 0
    count = 0
    for i in df_temp.index:
        t = df_temp.at[i, "Time"].split(":")
        if df_temp.at[i, "ON/OFF/ERR"] == "ON":
            a = datetime.datetime(2021, month_dict[df_temp.at[i, "Month"]], int(df_temp.at[i, "Date"]), int(t[0]), int(t[1]), int(t[2]), int(t[3]))
            f1 = 1
        elif df_temp.at[i, "ON/OFF/ERR"] == "OFF":
            b = datetime.datetime(2021, month_dict[df_temp.at[i, "Month"]], int(df_temp.at[i, "Date"]), int(t[0]), int(t[1]), int(t[2]), int(t[3]))
            f = 1
        if f == 1 and f1 == 0:
            f = -1
            continue
        if a != -1 and b != -1:
            c = b - a
            count += int(c.total_seconds())
            a = -1
            b = -1
    
    ans = df_temp.loc[df_temp["ON/OFF/ERR"] == "ERR"]

    if count != 0:
        data_log.write("\nDevice {} was on for {} seconds.".format(uid.replace('[', "").replace(']', ""), count))
        if not ans.empty:
            data_log.write("\nDevice {} had following error events:".format(uid.replace('[', "").replace(']', "")))
            for j in ans.index:
                str_write = "\n\t" + str(ans.at[j, "Month"]) + ' ' + str(ans.at[j, "Date"]) + ' ' + str(ans.at[j, "Time"])
                data_log.write(str_write)
        else: 
            data_log.write("\nDevice {} had no error events.\n".format(uid.replace('[', "").replace(']', "")))


