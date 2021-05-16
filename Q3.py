import requests
import json
import sqlite3

conn = sqlite3.connect("advices.sqlite")
cur = conn.cursor()

url = "https://api.adviceslip.com/advice"
r = requests.get(url)

print(f"status code {r.status_code}")
res = r.text
print(f"headers {r.headers}")
res1 = json.loads(res)
res2 = json.dumps(res1, indent=4)
with open('hungry.json', 'w') as f:
    json.dump(res1, f, indent=4)
print(res2)
adv = r.json()["slip"]["advice"]
print(r.json()["slip"]["advice"])
# კოდის გაშვებისას შეიქმნება ცხრილი სახელწოდებით advices.
# რომ არ წარმოიშვას კომფლიქტი ყოველ ახალ გაშვებაზე ვამოწმებ ბაზაში არსებობს თუ არა ეს ცხრილი.
conn.execute('''CREATE TABLE IF NOT EXISTS advices (adv TEXT) ''')
# მას შემდეგ რაც ცხრილი შეიქმნება adv სვეტში ვამატებ adv ცვლადს ტექსტის სახით.
cur.execute('INSERT INTO advices (adv) VALUES (?)', (adv,))
conn.commit()
conn.close()
