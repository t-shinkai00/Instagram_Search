from variables import IG_USER, IG_PASS
from instaloader import Instaloader, Profile

def search_ig(id_):
  L = Instaloader()
  L.login(IG_USER, IG_PASS)

  profile = Profile.from_username(L.context, id_)

  username = profile.username
  userid = profile.userid
  mediacount = profile.mediacount
  followers = profile.followers
  followees = profile.followees
  bio = profile.biography
  external_url = profile.external_url

  return username, userid, mediacount, followers, followees, bio, external_url

if __name__ == '__main__':
  id_ = "sins_tatsuyahino"
  search_ig(id_)