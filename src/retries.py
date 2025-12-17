import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def get_custom_session():
    session = requests.Session()
    retries = Retry(
        total=3,
        backoff_factor=1, 
        status_forcelist=[500, 502, 503, 504],
        allowed_methods=["GET", "POST"]
    )
    
    adapter = HTTPAdapter(max_retries=retries)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session


