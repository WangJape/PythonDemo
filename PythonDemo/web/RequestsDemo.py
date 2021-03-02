import requests
import json

r = requests.get('http://www.baidu.com')
print(r)

jsonStr = """
{
    "a":4,
    "b":6
}
"""
print(json.dumps(jsonStr))

