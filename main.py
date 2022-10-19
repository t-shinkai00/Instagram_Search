from get_ig_urls import get_ig_urls
from search_ig import search_ig


def main():
  # 検索
  key = '"#銀座" "#髪質改善"'
  ig_urls = get_ig_urls(key)
  for i, url in enumerate(ig_urls):
    print(i, url)

if __name__ == '__main__':
  main()