import requests
import bs4
import numpy as np
import matplotlib.pyplot as plt

#These are the index number when calling specific categories
#stats
games_played_in_season = 0
games_played_in_career = 1
ppg_season = 2
ppg_career = 3
rpg_season = 4
rpg_career = 5
apg_season = 6
apg_career = 7
#percentages
fgp_season = 8
fgp_career = 9
threepp_season = 10
threepp_career = 11
ftp_season = 12
ftp_career = 13
efgp_season = 14
efgp_career = 15

def get_player_info(player_name):
    base_url = "http://basketball-reference.com/players/"
    player = player_name.lower()
    player_last_initial = str(player.split(' ')[1][0])
    player_last_name = str(player.split(' ')[1][0:5])
    player_first_two = str(player.split(' ')[0][0:2])
    url = base_url + player_last_initial + '/' + player_last_name + player_first_two + '01.html'

    result = requests.get(url)
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    stats = soup.select('.stats_pullout')

    player_stats = []
    for stat in stats:
        var = stat.select('div')[2]
        nvar = var.select('p')
        for i in nvar:
            i=str(i)
            x=i.split('<p>')[1]
            x=x.split('</p>')[0]
            player_stats.append(x)
    for stat in stats:
        var = stat.select('div')[7]
        nvar = var.select('p')
        for i in nvar:
            i=str(i)
            x=i.split('<p>')[1]
            x=x.split('</p>')[0]
            player_stats.append(x)
    return player_stats



def main():
    print('Welcome to an NBA stat comparison program. You will enter two NBA players to compare and be shown'
          'their current season and carrer averages in 12 different categories!\n')
    play1 = input('Enter a currently active NBA player: ')
    play2 = input('Enter another currently active NBA player: ')
    player1 = get_player_info(play1)
    player2 = get_player_info(play2)
    player1_stats = []
    player2_stats = []
    for i in player1:
        i = float(i)
        player1_stats.append(i)
    for x in player2:
        x = float(x)
        player2_stats.append(x)
        
    info_matrix = [player1_stats,player2_stats]
    
    color = ['black', 'blue']
    
    print()
    print(f'{play1} = {color[0]}\n{play2} = {color[1]}')
    plt.figure()
    for i in range(2):
        s=2
        w=0.8
        plt.bar(np.arange(len(info_matrix[0][2:8]))*s+(i*w), info_matrix[i][2:8], color=color[i])
        plt.xticks(ticks=[0,2,4,6,8,10],
                   labels=['PPG_S','PPG_C','RPG_S','RPG_C','APG_S','APG_C']);
    print()
    print()
    plt.figure()
    for i in range(2):
        s=2
        w=0.8
        plt.bar(np.arange(len(info_matrix[0][8:14]))*s+(i*w), info_matrix[i][8:14], color=color[i])
        plt.xticks(ticks=[0,2,4,6,8,10],
                   labels=['FG%_S','FG%_C','3P%_S','3P%_C','FT%_S','FT%_C']);
    
main()
