import instaloader
from sys import argv

# this script is not finished

username, password = argv[1:]

L = instaloader.Instaloader()
L.login(username, password)
profile = instaloader.Profile.from_username(L.context, username)
print(profile.username)

for followee in profile.get_followees():
    print(followee.username)

