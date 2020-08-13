import requests

url = "$IP"
fin = open('file.txt', 'rb')
files = {'file': fin}
try:
  r = requests.post(url, files=files)
  print (r.text)
finally:
	fin.close()
