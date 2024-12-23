import re
url = input("URL: ").strip()

username = re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)", url)

if username:
    print(username.group(1))