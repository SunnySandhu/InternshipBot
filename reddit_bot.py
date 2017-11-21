import praw
import info
import time
import os


def run(instance, tracker):
    for comment in instance.subreddit('carletonu').comments(limit=10):
        if "!internship" in comment.body and comment.id not in tracker and comment.author != instance.user.me():
            print ("String related to internships found in comment")
            reply = ("Hey, Internship Bot here to help you find internships!\n\n")
            reply1 = ("Here is a collection of internship postings in your city: \n\n")
            reply2 = ("[Internships in Ottawa found on Monster.ca](https://www.monster.ca/jobs/search/?q=internship&where=Ottawa)\n\n")
            reply3 = ("[Internships in Ottawa found on Indeed.ca](https://ca.indeed.com/Intern-jobs-in-Ottawa,-ON)\n\n")
            reply4 = ("[Internships in Ottawa found on TalentEgg.ca](https://talentegg.ca/find-a-job/city/ottawa/role/internship)\n\n")
            reply5 = ("[Internships in Ottawa found on GlassDoor.ca](https://www.glassdoor.ca/Job/ottawa-intern-jobs-SRCH_IL.0,6_IC2286068_KO7,13.htm)\n\n")
            reply6 = ("I hope you find something that's right for you. If you ever need to summon me again just comment \"!internship\" anywhere on this subreddit.")
            reply = reply + reply1 + reply2 + reply3 + reply4 + reply5 + reply6
            comment.reply(reply)
            tracker.append(comment.id)
            print ("Replied!")
            print(tracker)
            with open("history.txt", "a") as f:
                f.write(comment.id + "\n")
            print("Sleeping for 5 seconds")
            time.sleep(5)
    print ("sleeping for 3 seconds")
    time.sleep(3)
def retrieveHistory():
    if not os.path.isfile("history.txt"):
        tracker = []
    else:
        with open("history.txt", "r") as f:
            tracker = f.read()
            tracker = tracker.split("\n")
            tracker = list(filter(None, tracker))
    return tracker


instance = praw.Reddit(username = info.username,
                        password = info.password,
                        client_id = info.client_id,
                        client_secret = info.client_secret,
                        user_agent = "Sunny's internship bot v0.2")
tracker = retrieveHistory()
print (tracker)
while True:
    run(instance, tracker)
