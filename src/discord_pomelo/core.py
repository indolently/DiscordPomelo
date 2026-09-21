from __future__ import annotations
import requests

class DiscordPomelo:
    def __init__(self) -> None:
        self.base_url = 'https://discord.com/api'

    def get_username_suggestion(self: DiscordPomelo, token: str = None) -> str:
        if token is None:
            _username_request = requests.get(
                self.base_url + '/unique-username/username-suggestions-unauthed',
                timeout=10
            )
            username_request = _username_request.json()
            username = username_request['username']
        else:
            _username_request = requests.get(
                self.base_url + '/users/@me/pomelo-suggestions',
                headers={
                    "Authorization": token
                },
                timeout=10
            )
            if _username_request.status_code == 401:
                return "Invalid token, or is a user token."
            username_request = _username_request.json()
            username = username_request['username']

        return username

if __name__ == "__main__":
    discord_pomelo = DiscordPomelo()
    print(discord_pomelo.get_username_suggestion())
    print(discord_pomelo.get_username_suggestion(token="put_your_bot_token_here"))
