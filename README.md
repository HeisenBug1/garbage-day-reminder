# Garbage Day Reminder
 Remind yourself of what garbage to take out to the curb

## About

If you don't live in an appartment, then you most likely have to take out your own garbage to the curb for the sanitation department to pick it up once every week. and what garbage you can put outside depends. it usually alternated between Waste only or Both Waste and Recycle. and if your like me who forgets which one it is during that week, then this little python script can be helpful to you. it's also very helpful for people who came back from a long vacation and can't remember.

just run the script, and it will ask you what day your last garbage was and what type. it'll save that info in your home directory and with that bit of information it can tell you accurately for the rest of the year guaranteed.

## How to use

Open your terminal or command prompt and run

`python /path/to/trash.py`

OR

`python3 /path/to/trash.py`

It'll ask you a few questions, answer them. (date, garbge type, etc)<br>
you can also choose to enter a `sender` email address along with its `password` and a `recipient` email address if you want to get notified through email

If you do want to get notified through email, then you'll have to create a scheduled task like a `cronjob` for linux or `LaunchD` MacOS. Not sure about Windows, but im sure you can google and find out.

Otherwise everytime you run the script from terminal, it'll tell you when the next garbage day is and what type.
