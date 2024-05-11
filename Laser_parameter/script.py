import pandas as pd

number_of_pass = [1,2,3]
level_power_laser = [25,50,75,100]
speed_rate = [1000,1500,2000,3000,10000,25000,50000]


column_passes=[]
column_level=[]
column_rate=[]

for number in number_of_pass :
    for level in level_power_laser :
        for rate in speed_rate :
            column_passes.append(number)
            column_level.append(level)
            column_rate.append(rate)
            
d = {'Passes':column_passes, 'Power':column_level,'Speed':column_rate}
df = pd.DataFrame(data=d)
print(df)
df.to_csv("20240511_export.csv", sep=";",index=False)
