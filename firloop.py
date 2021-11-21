import requests
# url = "http://www.google.com"
#
# # timeout = 5
# try:
# 	request = requests.get(url, )
# 	print("Connected to the Internet")
# except (requests.ConnectionError) as exception:
# 	print("No internet connection.")

url = "http://www.google.com"
# timeout = 10
try:
	request = requests.get(url, timeout=10)

except (requests.ConnectionError, requests.Timeout) as exception:
	print("No internet connection.")