import requests
from time import sleep

result = requests.post('http://localhost:3490/v1/pulse').json()
sleep(5)
request = requests.get('http://localhost:3490/v1/account-totals').json()
keys = request['keys']
clicks = request['clicks']
download = request['download']
upload = request['upload']
uptime = int(request['uptime'])
uptime = uptime/60/60/24*100
uptime = round(uptime)
uptime = uptime/100

rank_clicks = request['ranks']['rank_clicks']
rank_download = request['ranks']['rank_download']
rank_keys = request['ranks']['rank_keys']
rank_upload = request['ranks']['rank_upload']
rank_uptime = request['ranks']['rank_uptime']
ranks = {'Clicks':rank_clicks, 'Download':rank_download, 'Keys':rank_keys, 'Upload':rank_upload, 'Uptime':rank_uptime}
winner = min(ranks, key=ranks.get)

print("Tasten: {} Tasten gedrückt\nKlicks: {} Klicks gemacht\nDownload: {} Mb heruntergeladen\nUpload: {} Mb hochgeladen\nUptime: {} Tagen angeschaltet\nBester Rang: {} mit dem {}. Platz".format(keys, clicks, download, upload, uptime, winner, ranks.get(winner)))