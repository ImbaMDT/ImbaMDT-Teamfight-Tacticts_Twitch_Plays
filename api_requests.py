import json
import requests


def check_GameStart():
    try:
        allrespones = requests.get('https://127.0.0.1:2999/liveclientdata/allgamedata', timeout=10, verify=False)
        for events in allrespones.json()['events']['Events']:
            if events['EventName'] == "GameStart":
                return True
        return False
    except Exception:
        return False


def check_GameLoading():
    try:
        allrespones = requests.get('https://127.0.0.1:2999/liveclientdata/allgamedata', timeout=10, verify=False)
        if allrespones.json()['httpStatus'] == 404:
                return True
        return False
    except Exception:
        return False

def player_Names():
    try:
        allrespones = requests.get('https://127.0.0.1:2999/liveclientdata/allgamedata', timeout=10, verify=False)
        for names in allrespones.json()['allPlayers']:
            print(names['summonerName'])
    except Exception:
        return False
