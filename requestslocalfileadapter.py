import requests
from requests_file import FileAdapter

s = requests.Session()
s.mount('file://', FileAdapter())

resp = s.get('file:///path/to/file')