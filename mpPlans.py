
import requests

# import json
# import sys
# from threading import Thread
import time
# import utils
# import utilsSch

import imp
utilsSch = imp.load_source('utilsSch', '/home/user1/mygit/airflow/utils/utilsSch.py')


# sql_connection_linux
# Берем из MemberClubVisits. Не забываем $expand=member. Там еще есть contracts.


# initializing vars
startTime = int(time.time())
# username = "apiuser"
# password = "h7lR.'M8xA"
countPaymentPlanNotFound = 0
fileName = "gym-visits-new.json"
start = True
count = 0
visitsList = []
token = "DFdYRZlgx8HGLjDzKrHb6YHMKYL-vu4utxsBYZ8ZP7VQYVSMZs3AwFTm1Ma_bnmNqmnZJysHauLuJQ-TGC4NbsmtNZbg3-1J8IBcVYkOcx7jv5gfnCbuOPDN833Mh2VH5ITofhDJ-fKcDfaDfL_FMemVswO3Syw9QKRL_MTgTy2q9Uv4Jyn0s1HaZhVxG5HhFYSmvtbKeym_bj6sa1F5_6DMXQb-IItiZ7CwQ6hL1OHO5beEN7kKLIGcHWlpqhykEkfBprd-y_g7NibbMWd3twSFZuwrkbt_sp-9U6WNIS9Y1aoa"

# ------------------
url = "https://api.mp.kz/authenticate"
username = "atameken"
password = "pIz62uKPFJndfJBPN30CR5hgLlsSC507"
# -----------------

### getting token

print("getting token...")
# tokenUrl = "https://invictusfitness.perfectgym.com/Api/oauth/authorize"
tokenUrl = "https://api.mp.kz/authenticate"

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
    # "Content-Type": "application/json"
}

tokenData = "password=" + password + "&username=" + username + "&grant_type=password"
response = ""
while response == "":
    try:
        # response = requests.post(tokenUrl, data=tokenData, headers=headers)

        tokenUrl += '?username=atameken&password=pIz62uKPFJndfJBPN30CR5hgLlsSC507'
        response = requests.get(tokenUrl)

        break
    except:
        print("going to sleep")
        time.sleep(5)
        print("continue")
        continue

print('response:', response)

token = response.headers['Authorization']
print(token)

headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json"
}
# connecting to db 'GS', 'PBI'
conn = utilsSch.connect('GS', case='linux')

count = 0
errorList = []

mainUrl = "https://api.mp.kz/odata/"
url = "https://api.mp.kz/odata/TenderLotPlan?$count=true&$orderby=id desc"
mainUrl2 = "https://api.mp.kz/odata/TenderLotPlan?$count=true&$orderby=id desc&$skip="


isStart = True
odataCount = 0
tableName = "gs.dbo.mpPlans_temp_copy"

while count < odataCount or isStart:
    isStart = False
    response = requests.get(url, headers=headers, verify=False)
    jsonik = response.json()
    print(jsonik)

    odataCount = jsonik['@odata.count']

    print('value:', jsonik['value'])

    value = jsonik['value']
    print('len(value):', len(value))
    print('value[0]:', value[0])

    for v in value:
        count += 1
        cursor = conn.cursor()
        # 18 params
        try:
            cursor.execute("""insert into {}( 
                    [deliveryEntityId]
                   ,[initiatorCompanyId]
                   ,[planningYear]
                   ,[quantity]
                   ,[name]
                   ,[description]
                   ,[initiatorCompanyName]
                   ,[id]
                   ,[currencyId]
                   ,[categoryId]
                   ,[measureUnitId]
                   ,[budget]
                   ) 
                   values(
                   ?,?,?,?,?,?,?,?,?,?,
                   ?,?
                   )
                   """.format(tableName)
                           ,
                           v.get('deliveryEntityId'),
                           v.get('initiatorCompanyId'),
                           v.get('planningYear'),
                           v.get('quantity'),
                           v.get('name'),
                           v.get('description'),
                           v.get('initiatorCompanyName'),
                           v.get('id'),
                           v.get('currencyId'),
                           v.get('categoryId'),
                           v.get('measureUnitId'),
                           v.get('budget')
                           )
        except:
            errorList.append(v)

    try:
        odataNextLink = jsonik['@odata.nextLink']
        # url = mainUrl + odataNextLink
        url = mainUrl2 + str(count)
    except:
        print('finished, no next link')
        break
print('errorList:', errorList)








