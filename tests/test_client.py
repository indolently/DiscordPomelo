from unittest.mock import Mock, patch

import pytest

from discord_pomelo import DiscordPomelo


def test_get_username_suggestion_unauthed():
    client = DiscordPomelo()

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"username": "example_user"}

    with patch("discord_pomelo.client.requests.get", return_value=mock_response) as mock_get:
        result = client.get_username_suggestion()

    assert result == "example_user"

    mock_get.assert_called_once_with(
        "https://discord.com/api/unique-username/username-suggestions-unauthed",
        timeout=10,
    )


def test_get_username_suggestion_with_token():
    client = DiscordPomelo()

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"username": "example_user"}

    with patch("discord_pomelo.client.requests.get", return_value=mock_response) as mock_get:
        result = client.get_username_suggestion("test_token")

    assert result == "example_user"

    mock_get.assert_called_once_with(
        "https://discord.com/api/users/@me/pomelo-suggestions",
        headers={"Authorization": "test_token"},
        timeout=10,
    )


def test_get_username_suggestion_invalid_token():
    client = DiscordPomelo()

    mock_response = Mock()
    mock_response.status_code = 401

    with patch("discord_pomelo.client.requests.get", return_value=mock_response):
        with pytest.raises(ValueError, match="Unauthorized or invalid token"):
            client.get_username_suggestion("invalid_token")


def test_get_username_suggestion_http_error():
    client = DiscordPomelo()

    mock_response = Mock()
    mock_response.status_code = 500
    mock_response.raise_for_status.side_effect = Exception("Server error")

    with patch("discord_pomelo.client.requests.get", return_value=mock_response):
        with pytest.raises(Exception, match="Server error"):
            client.get_username_suggestion()


def test_get_username_suggestion_missing_username():
    client = DiscordPomelo()

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {}

    with patch("discord_pomelo.client.requests.get", return_value=mock_response):
        with pytest.raises(KeyError):
            client.get_username_suggestion()
