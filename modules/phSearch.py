import random
from pornhub_api import PornhubApi

url_key = 'https://es.pornhub.com/view_video.php?viewkey='
api = PornhubApi()

def video_hub(name, _page) :
    title = []
    id_hub = []
    data = api.search.search(
        q=name,
        ordering="most relevant",
        period="alltime",
        page=_page,
        thumbsize= "big"
        # tags=['anal','teen','big ass'])
    )
    for vid in data.videos :
        title.append(vid.title)
        id_hub.append(vid.video_id)
    return title, id_hub


def hub_video_rand() :
    title = []
    id_hub = []

    tags = random.sample(api.video.tags("f").tags, 5)
    category = random.choice(api.video.categories().categories)
    result = api.search.search(ordering="mostviewed", tags=tags, category=category)

    # print(result.size())
    for vid in result.videos :
        # print(vid.title, vid.url)
        title.append(vid.title)
        id_hub.append(vid.url)
        break

    return title, id_hub