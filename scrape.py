import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://kmpdc.go.ke/Registers/General_Practitioners.php"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
}
response = requests.get(url, headers=headers)


if response.status_code == 200:
    
    htmlDoc = BeautifulSoup(response.content, "html.parser")
    
    table = htmlDoc.find("table")
   

    headers = [header.text.strip() for header in table.find_all("th")]

    rows = []
    for row in table.find_all("tr")[1:]:
        rows.append([cell.text.strip() for cell in row.find_all("td")])

   
    df = pd.DataFrame(rows, columns=headers)

    
    excel_filename = "pythonScraping.xlsx"
    df.to_excel(excel_filename, index=False)

    print("Data has been scraped and saved to " + excel_filename +  " successfully.")
else:
    print("Failed to retrieve data from the website.")
