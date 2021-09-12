import requests
from bs4 import BeautifulSoup
import webbrowser

def get_html(url):
    _html = ""
    resp = requests.get(url)
    if resp.status_code == 200:
        _html = resp.text
    return _html

# 채널은 json으로 따로 만들어야할 것 같음
# 생방 안뜨면 스트리머 이름이랑 시청중인 사람 에러뜨니 다시 해야함 <<< 중요

mio = "UCp-5t9SrOQwXMU7iIjQfARg"
calliope = "UCL_qhgtOy0dy1Agp8vkySQg"
okayu = "UCvaTdHTWBGv3MKj3KVqJVCw"
aqua = "UC1opHUrw8rvnsadT-iGp7Cg"
baelz = "UCgmPnx-EEeOrZSg5Tiw7ZRQ"
kronii = "UCmbs8T6MWqUHP1tIQvSgKrg"
pekora = "UC1DCedRgGHBdm81E1llLhOQ"
flare = "UCvInZx9h3jC2JzsIzoOebWg"
polka = "UCK9V2B22uJYu3N7eR_BT9QA"
inanis = "UCMwGHR0BTZuLsmjY_NT5Pwg"
suisei = "UC5CwaMl1eIgY8h02uZw7u8A"

Url = "https://www.youtube.com/channel/" + polka
html = get_html(Url)
soup = BeautifulSoup(html, 'html.parser')
soup = str(soup)
sources = soup.split('"content"')

video_info = sources[2]
print(video_info)
def split_item(item):
    result = video_info.split(item)
    #print(result)
    result_part = result[1]
    info = result_part.split('"')
    return info

get_video_id = split_item('"videoId":')
get_thumbnail = split_item('"thumbnails":')

#print(split_item('"ownerText":'))
get_name = split_item('"ownerText":')


get_viewer = split_item('"viewCountText":')
videoid = get_video_id[1]
thumbnail = get_thumbnail[3]
streamer = get_name[5]
viewer = get_viewer[5]

live_url = "https://youtube.com/watch?v=" + videoid

def get_title():
    get_title_parts = split_item('"simpleText":')
    title = get_title_parts[1]
    return title

print("채널 주소 : " + Url)
print("스트림 제목 : " + get_title())
print("라이브 주소 : " + live_url)
print("썸네일 : " + thumbnail)
print("스트리머 이름 : " + streamer)
print(viewer + "명 시청중")
