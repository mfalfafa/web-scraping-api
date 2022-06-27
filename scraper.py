import pandas as pd
import requests
import json
import time

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }
FILENAME = "mens_sunglasses"

start_time = time.time()
res = []
for pg in range(1,76+1):
    r = requests.get(
        "https://www.sunglasshut.com/wcs/resources/plp/10152/byCategoryId/3074457345626651837?isProductNeeded=true&pageSize=18&responseFormat=json&isChanelCategory=false&currency=USD&pageView=image&viewTaskName=CategoryDisplayView&beginIndex=0&categoryId=3074457345626651837&catalogId=20602&langId=-1&storeId=10152&top=Y&orderBy=default&currentPage={}".format(pg), 
        headers=HEADERS
        )
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