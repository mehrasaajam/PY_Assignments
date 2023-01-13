
import instaloader
import getpass

followers_file = open("followers.txt", "r")
old_followers = []
for line in followers_file:
    old_followers.append(line)
followers_file.close()

L = instaloader.Instaloader()

username = input("enter username: ")
password = getpass.getpass("enter password: ")

L.login(username, password)

profile=instaloader.Profile.from_username(L.context, "mehrasa_ajm")

new_followers = []
for folloewr in profile.get_followers():
    new_followers.append(follower)

for new_follower in new_followers:
    if new_follower not in old_followers:
        print(new_follower)

followers_file = open("followers.txt", "w")
for follower in new_followers:
    followers_file.write(folloewr + "\n")
followers_file.close()
