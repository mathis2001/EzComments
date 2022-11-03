# EzComments

EzComments is a tool allowing you to get all html and comments of each url given to him.

## Install:
```bash
$ git clone https://github.com/mathis2001/EzComments.git
```

## Usage:
```bash
$ cat urls.txt | python3 ezcomments.py

or with an other tool like WebHackUrls

$ python3 webhackurls.py -d target.com | python3 ezcomments.py
```

## Screenshots:

![Capture d’écran 2022-09-26 132049](https://user-images.githubusercontent.com/40497633/192264821-c5c9a145-3e73-413e-8703-1e70d749f071.jpg)
![Capture d’écran 2022-09-26 133518](https://user-images.githubusercontent.com/40497633/192266723-3170a0b5-4a35-4c98-bb16-0f28967237b4.jpg)

## ToDo:

Find a way to reduce false positive (exp: js comment regex match href=<b>//exemple.com</b>)
