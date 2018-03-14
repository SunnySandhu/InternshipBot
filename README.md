# InternshipBot V0.2
A reddit bot designed to help find internships for students in their college city.
Supported Subreddits:
* /r/CarletonU
## Files:
There are three files  included in this repository
  * reddit_bot.py : This is the script, it runs in an infinite loop checking the 10 latest posts.
  * info.py : This file is used where the api keys and login info are located. 
  * history.txt : This file is used to keep track of comment reply history so the bot doesn't reply more than once to the same comment.

## Dependencies
* Python 3.x
* PRAW

Install PRAW with [pip](https://pypi.python.org/pypi/pip)
```
>git clone git@github.com:SunnySandhu/IntershipBot.git
>cd InternshipBot
>pip install praw
```
## Usage
Run the following: 
```
>python reddit_bot.py
```



## Credits
The credits for this goes to [busterroni11](https://www.youtube.com/channel/UCBN_m9Ygp2y6ndNoO4O2Nww)
I've used his tutorial to build an understanding of praw, and to layout the program structure.




   
