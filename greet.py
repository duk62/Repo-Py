import sys
import pip._vendor.requests.api as requests


# print(sys.version)
# print(sys.executable)


def greet(whom_to_greet):
    greeting = "Hello, {}".format(whom_to_greet)
    return greeting


# print(greet('world'))
# print(greet('Learner'))
r = requests.get("http://www.python.org")
print(r.status_code)
