import sys
import pip._vendor.requests.api as requests


def show():
    print(sys.version)
    print(sys.executable)
    r = requests.get("http://www.python.org")
    print(r.status_code)


show()
