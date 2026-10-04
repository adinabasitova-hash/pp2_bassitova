import re
import json

with open('raw.txt', encoding="utf-8") as f:
  text = f.read()

prices = re.findall(r'Стоимость\s+([\d ]+,\d{2})', text)

items = re.findall(r'\d+\.\s+(.+)',text)
items = [n.strip() for n in items]

m = re.search(r'Чек №(\d{10})',text)
receipt_number = m.group(1)

nums = []
for p in prices:
  p = re.sub(r'\s', '', p)
  p = p.replace(',', '.')
  nums.append(float(p))

my_total = sum(nums)


m = re.search(r'Время:\s(\d{2}\.\d{2}\.\d{4})\s(\d{2}:\d{2}:\d{2})', text)
date = m.group(1)
time = m.group(2)

p = re.search(r'(.+):\s+[\d ]+,\d{2}\s+ИТОГО:', text)
payment = p.group(1)

result = {
  'receipt_number': receipt_number,
  'date' : date,
  'time':time,
  'payment_method' : payment,
  'items' : items,
  'total_calulated': my_total

}

js = json.dumps(result,ensure_ascii = False, indent=2)
print(js)