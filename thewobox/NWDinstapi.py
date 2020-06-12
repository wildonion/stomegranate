

# https://github.com/LevPasha/Instagram-API-python/tree/master/examples

# TODO: time schedualing feature - use asyncio 
# TODO: unfollow targets after a specific time from down to up with a delay time like 10 secs : i think we should use DB or file for this 

from InstagramAPI import InstagramAPI
import requests , bs4, re, sys

def getid(username):
    url = requests.get(f"https://instagram.com/{username}")
    soup = bs4.BeautifulSoup(url.text)
    try:
        a = str(soup.findAll("script")[3])
        find = re.findall(r'"id":"\d*\d"',a)
        userid = find[0].split('"')
        return userid[3]
    except:
        return False

def getTotalFollowers(api, user_id, limit):
    followers = []
    next_max_id = True
    while next_max_id:
        if next_max_id is True:
            next_max_id = ''
        _ = api.getUserFollowers(user_id, maxid=next_max_id)
        a = api.LastJson.get('users', [])
        for i in a:     
            followers.append(getid(i["username"]))
            if len(followers) >= limit: return followers
        next_max_id = api.LastJson.get('next_max_id', '')


def main():
    # username = str(input("UsernameTarget > "))
    targets = [str(input("\t[+] UsernameTarget >> ")) for t in range(int(input("[+] Enter the number of target username >> ")))]
    myuser = str(input("[+] Username(myacc) >> "))
    mypass = str(input("[+] password(myacc) >> "))
    limit = int(input("[+] count >> "))

    print("[+] Processing ....")
    api = InstagramAPI(myuser, mypass)
    api.login()
    userid = []
    for t in targets:
        userid.append(getid(t))
    for uid in userid:
        if uid:
            followers_id = getTotalFollowers(api, uid, limit)
            for f in followers_id:
                api.follow(f)

    # user_id = '146129517'
    # userid = getid(username)
    # if userid:
    #     followers_id = getTotalFollowers(api, userid, limit)
        # for f in followers_id:
        #     api.follow(f)
    else:
        print("Username Error")
        return    

    print("done!")


if __name__ == "__main__":
    main()
    input("Press somthing to exit")
