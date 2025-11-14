import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    link = re.search(r'^<iframe.+src="(https?://(www\.)?youtube\.com/embed/([^"]+))".+/iframe>$',s,re.IGNORECASE)
    if link:
        video_id = link.group(3)
        return f"https://youtu.be/{video_id}"
    else:
        return None



if __name__ == "__main__":
    main()
