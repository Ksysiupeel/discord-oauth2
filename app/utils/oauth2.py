import requests
from config import (
    CLIENT_ID,
    CLIENT_SECRET,
    SCOPE,
    REDIRECT_URL,
    DISCORD_TOKEN_URL,
    DISCORD_API_URL,
)


class Oauth2:
    @staticmethod
    def get_token(code):
        payload = {
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": REDIRECT_URL,
            "scope": SCOPE,
        }

        token = requests.post(url=DISCORD_TOKEN_URL, data=payload)
        json = token.json()
        return json.get("access_token")

    @staticmethod
    def get_user(token):
        url = DISCORD_API_URL + "/users/@me"

        headers = {"Authorization": f"Bearer {token}"}

        user_obj = requests.get(url=url, headers=headers)

        user_json = user_obj.json()
        return user_json
