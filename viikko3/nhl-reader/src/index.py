import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    # print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    print("Oliot:")

    players.sort(key=lambda x: getattr(x, 'goals') + getattr(x, 'assists'), reverse=True)

    #for player in players:
    #    print(player)

    suomalaiset = filter(lambda x: getattr(x, 'nationality') == 'FIN', players)
    
    for player in suomalaiset:
        print(player)

if __name__ == "__main__":
    main()