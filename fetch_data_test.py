from get_data import get_players_data

from datetime import datetime
startTime = datetime.now()

df = get_players_data()

print(datetime.now() - startTime)
print('----')
print(df.shape)
print(df.head())