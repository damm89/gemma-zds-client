import jwt

from zds_client import ClientAuth


def test_credentials_header():
    auth = ClientAuth(client_id="client_id", secret="secret")
    credentials = auth.credentials()

    assert "Authorization" in credentials
    parts = credentials["Authorization"].split(" ")
    assert parts[0] == "Bearer"


def test_client_id_in_body():
    auth = ClientAuth(client_id="client id", secret="secret")
    credentials = auth.credentials()["Authorization"]

    token = credentials.split(" ")[1]

    payload = jwt.decode(token, verify=False)

    assert "client_id" in payload
    assert "zds" not in payload
    assert payload["client_id"] == "client id"
