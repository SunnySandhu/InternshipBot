# InternshipBot V0.2

A reddit bot designed to help find internships for students in their college city.

Supported Subreddits:
/r/CarletonU


Files:
There are three files  included in this repository
  1. reddit_bot.py : This is the script, it runs in an infinite loop checking the 10 latest posts.
  2. info.py : This file is used where the api keys and login info are located. 
  3. history.txt : This file is used to keep track of comment reply history so the bot doesn't reply more than once to the same comment.
  
Usage:
The user must create a comment that includes the string "!internship" on a supported subreddit. The bot will then reply to that very comment. 
