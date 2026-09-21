# DiscordPomelo

A lightweight Python wrapper for making requests to Discord's Pomelo username API.

## Features

- Get a username suggestion without authentication.
- Get a username suggestion using a bot token.
- Simple interface built on top of `requests`.
- Handles invalid/unsupported authentication responses.

## Installation

Clone the repository and install the dependency:

```
git clone https://github.com/indolently/DiscordPomelo.git
cd DiscordPomelo
pip install requests
```

 ## API Endpoints

| Name | Endpoint | Authentication |
| --- | --- | --- |
| `POMELO_SUGGESTIONS` | `/users/@me/pomelo-suggestions` | Bot token |
| `POMELO_SUGGESTIONS_UNAUTHED` | `/unique-username/username-suggestions-unauthed` | None |

The base URL used by the library is:

```
https://discord.com/api
```

 ## Usage

 ### Unauthenticated Username Suggestion

 No token is required to request an unauthenticated username suggestion.

```
from discord_pomelo import DiscordPomelo

discord_pomelo = DiscordPomelo()

username = discord_pomelo.get_username_suggestion()

print(username)
```

### Authenticated Username Suggestion

A Discord bot token can be supplied to request a username suggestion for the authenticated account.

```
from discord_pomelo import DiscordPomelo

discord_pomelo = DiscordPomelo()

username = discord_pomelo.get_username_suggestion(
    token="put_your_bot_token_here"
)

print(username)
```

 > **Important:** Keep your bot token private. Do not commit tokens to your repository or expose them in source code.

 ## Example

 The repository can also be run directly:

```
python discord_pomelo.py
```

 This performs both an unauthenticated request and an authenticated request:

```
if __name__ == "__main__":
    discord_pomelo = DiscordPomelo()

    print(discord_pomelo.get_username_suggestion())
    print(
        discord_pomelo.get_username_suggestion(
            token="put_your_bot_token_here"
        )
    )
```

 ## Response Handling

 `get_username_suggestion()` returns the suggested username as a string.

 For example:

```
someusername
```

 If an authenticated request returns HTTP `401`, the library returns:

```
Invalid token, or is a user token.
```

 ## Requirements

 - Python 3.8+
- `requests`

 Install `requests` with:

```
pip install requests
```

 ## Disclaimer

 This project is an unofficial Python wrapper around Discord's Pomelo API endpoints. It is not affiliated with, endorsed by, or sponsored by Discord.

 Discord may change, restrict, or remove these endpoints at any time.

 ## License

 See the repository's license file for licensing information.
