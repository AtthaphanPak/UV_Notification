from oauth2client.service_account import ServiceAccountCredentials
import gspread
import pprint

url = "https://docs.google.com/spreadsheets/d/1WJEOfHH5TXH1-EuWHqPptbt4tVG43VXqwBnzkqbujbQ/edit#gid=0"
scope = ['https://www.googleapis.com/auth/spreadsheets']
credentials = ServiceAccountCredentials.from_json_keyfile_name('keys.json', scope) #ชื่อไฟล์ต้องเขียนให้ตรงกับที่โหลดมา
client = gspread.authorize(credentials)
sheet = client.open_by_url(url) #ใส่ url ของหน้า Google Sheets
worksheet = sheet.get_worksheet(0)
results = worksheet.get_all_records()
print(results)
#print(results[-1]["UV"])
#pp = pprint.PrettyPrinter()
#pp.pprint(results)