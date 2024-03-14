import pandas as pd

data = []
with open(r'E:\MyDesktop\ThaiTran\Personal_Project\High-Occupancy-Itemset\code\mushroom\mushroom.txt', 'r') as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        tid = f"T{i+1}"
        items = line.strip().split(' ')
        data.append([tid, items])

df = pd.DataFrame(data, columns=['Tid', 'Items'])
# df = df.head(10000)
print(df)
# df.to_csv(r'E:\MyDesktop\ThaiTran\Personal_Project\High-Occupancy-Itemset\code\fruithut.csv')