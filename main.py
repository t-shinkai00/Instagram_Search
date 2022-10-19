from get_ig_urls import get_ig_urls
from search_ig import search_ig

import time


def main():
  # 検索
  key = '"#銀座" "#髪質改善"'
  ig_urls = get_ig_urls(key)
  for i, url in enumerate(ig_urls):
    # print(i, url)
    id_ = url.split("/")[3]
    username, userid, mediacount, followers, followees, bio, external_url = search_ig(id_)
    print("--------------------------------------")
    print(username, userid, mediacount, followers, followees, bio, external_url)

if __name__ == '__main__':
  main()