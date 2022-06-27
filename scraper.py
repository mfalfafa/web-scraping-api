import pandas as pd
import requests
import json
import time


FILENAME = "mens_sunglasses"
URL = "https://www.sunglasshut.com/wcs/resources/plp/10152/byCategoryId/3074457345626651837"
QUERYSTRING = {"isProductNeeded":"true","orderBy":["default","default","default"],"pageSize":"18","responseFormat":"json","isChanelCategory":"false","currency":"USD","pageView":"image","viewTaskName":"CategoryDisplayView","DM_PersistentCookieCreated":"true","beginIndex":"0","categoryId":"3074457345626651837","catalogId":"20602","langId":"-1","currentPage":["1","1"],"storeId":"10152","top":"Y"}
HEADERS = {
    "cookie": "aka-cc=ID; aka-ct=JAKARTA; aka-zp=; ak_bmsc=F051535FB44F8D258D261FCA19175803~000000000000000000000000000000~YAAQT6gEcsv9FI6BAQAAx%2BS0oxACWGHM6BkMn1knhsLCDv0jugeZWae7VNnyfFzGILYJs2brcfK3itrG4mfgZNEgM1K6mYpSzGwVeupeQ1XZLGZWgcSnXIzzGWd%2BPFAS%2BNE%2BtHRxKmNtQ4%2BMfwypjS%2BTPt8IiHm1hn8hDJ9L%2BpXu%2FXE755zD%2F2su5Jg7pdOAkH7rJAW9N7zazIrwtX9rKtQFoGfcG7fK1VLFAaD%2Bju0g6jAK0Pxzpaix5r15mhyb69ESS3zq5viWMmUSGKccpzRwypEQ74534hlajXw2lx%2BSxGCH7EyTN7429QxhDg%2FxxBAU%2FP0c3R3Awi408Z%2FBuVuO%2FaSssl0oASmdPoWGNkSoI%2BTlgrYLZgB3f0NPBbFWGnnvqwN80rT5K3eUGviQ",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
    }

start_time = time.time()
res = []
for pg in range(1,76+1):
    r = requests.request("GET", URL, headers=HEADERS, params=QUERYSTRING)
    data = r.json()["plpView"]["products"]["products"]["product"]
    res = res + data
    print("Page {} completed.".format(pg))
    # print(data)
    # break

# print(res[:3])
# print(len(res))

with open("{}.json".format(FILENAME), "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False, indent=4)

df = pd.json_normalize(res)
df.to_excel("{}.xlsx".format(FILENAME))

print("Scraping result is saved in {}.xlsx and {}.json".format(FILENAME, FILENAME))
print("Finished in %.3f seconds" % (time.time() - start_time))