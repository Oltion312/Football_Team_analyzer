"""
Copyright 2021 - Oltion Rrecaj

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


import pprint

from datetime import datetime
from football_data_api import data_fetchers


data = data_fetchers.CompetitionData()
# Set the data fetch to Premier League English football
data.competition = 'premier league'

date_today = datetime.today()
matches = data.get_info('matches', dateFrom='2018-07-01', dateTo=date_today)

#all_teams = data.get_info('teams')

#available_competitions = data.get_available_competitions()

#pprint.pprint(matches.get('matches')[0])
away_win_counter1 = 0
away_lost_counter1 = 0
away_draw_counter1 = 0
team1 = 'Chelsea FC'

away_win_counter2 = 0
away_lost_counter2 = 0
away_draw_counter2 = 0
team2 = 'Manchester United FC'

for k,v in matches.items():
    if 'matches' in k:
        for event in v:
            if team1 in event["awayTeam"]["name"]:
                # write the code to check which Team won from the data structure
                # add to the away win counter + 1
                # example if man united won then add +1 to away_win_countr
                pprint.pprint(event)
                if 'AWAY_TEAM' in event["score"]["winner"]:
                    away_win_counter1 = away_win_counter1 +1

                elif 'HOME_TEAM' in event["score"]["winner"]:
                    away_lost_counter1 = away_lost_counter1 +1

                elif 'Draw' in event["score"]["winner"]:
                    awy_draw_counter1 = away_draw_counter1 +1

for k,v in matches.items():
    if  'matches' in k:
        for event in v:
            if team2 in event["awayTeam"]["name"]:
                pprint.pprint(event)

                if 'AWAY_TEAM' in event["score"]["winner"]:
                    away_win_counter2 = away_win_counter2 +1

                elif 'HOME_TEAM' in event["score"]["winner"]:
                    away_lost_counter2 = away_lost_counter2 +1

                elif 'Draw' in event["score"]["winner"]:
                    away_draw_counter2 = away_draw_counter2 +1

                      
print(f'The Team {team1} draw away from home a total of {away_draw_counter1} time. ') 

print(f'The Team {team1} lost away from home a total of {away_lost_counter1} time. ')
                
print(f'The Team {team1} won away from home a total of {away_win_counter1} time. ')

print(f'The Team {team2} draw away from home a total of {away_draw_counter2} time. ') 

print(f'The Team {team2} lost away from home a total of {away_lost_counter2} time. ')
                
print(f'The Team {team2} won away from home a total of {away_win_counter2} time. ')
