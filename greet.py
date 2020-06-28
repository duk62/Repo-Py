import sys
import pip._vendor.requests.api as requests

r = requests.get("http://www.python.org")
print(r.status_code)
