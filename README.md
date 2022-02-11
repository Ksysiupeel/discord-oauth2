[![Ksysiupeel](https://badgen.net/badge/Developer/Ksysiupeel/blue?icon=github)](https://github.com/ksysiupeel/) 

# About
discord-oauth2 is a Flask based application that allows you to authorize the discord application and view user data.

# Configuration
You have to configure **config.py** before running the application.
```
CLIENT_ID = ""
CLIENT_SECRET = ""
SCOPE = ""
REDIRECT_URL = ""
DISCORD_LOGIN_URL = ""
DISCORD_TOKEN_URL = ""
DISCORD_API_URL = ""
SECRET_KEY = ""
```
and then install requirements:
```
pip install -r requirements.txt
```

# Run

```
python main.py
```
