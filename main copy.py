import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

scope = ['https://www.googleapis.com/auth/spreadsheets']
ID = "1WJEOfHH5TXH1-EuWHqPptbt4tVG43VXqwBnzkqbujbQ"

def main():
    credentials = None
    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file("token.json", scope)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", scope)
            credentials = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(credentials.to_json())
    
    try:
        service = build("sheets", "v4", credentials=credentials)
        sheets = service.spreadsheets()
        result = sheets.values().get(spreadsheetId=ID, range="Sheet1!A1:C4").execute()

        values = result.get("values", [])

        for row in values:
            print(values)
    except HttpError as error:
        print(error)


if __name__ == "__main__":
    main()