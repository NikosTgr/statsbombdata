


from statsbombpy import sb

sb.competitions()


sb.matches(competition_id=43,season_id=3)

events=sb.events(match_id=8657)

events.head()

events.dropna(inplace=True)

events.columns


events=events[['team','type','minute','location', 'pass_end_location', 'player', 'pass_outcome' ]]
events = events[events['team'] == 'England']

events.head()

events.dropna(inplace=True)


events.head()



