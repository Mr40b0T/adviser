# adviser
Q3 ფაილში გამოყენებულია:
* sqlite3
* <https://api.adviceslip.com> API<br>
* json

API ყოველ get მოთხოვნაზე აბრუნებს მსგავს JSON -ს
```bash
{"slip": { "id": 104, "advice": "Do, or do not. There is no try."}}
```
main ფაილში განთავსებულია Flask მოდული საიდანაც ეშვება ლოკალურად საიტი
იმისთვის რომ html სკრიპტი დარენდერდეს აუცილებელია განთავსდეს templates დირექტორიაში, ხოლო css static/css
