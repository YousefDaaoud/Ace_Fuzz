from core.requester import Requester
from core.utils import run_threads

def vhost_task(args):
    url, host = args
    req = Requester()

    headers = {"Host": host}
    r = req.get(url, headers=headers)

    if r and r.status_code not in [404]:
        print(f"[+] VHost Found: {host}")

def run_vhost(url, wordlist, threads=50):
    with open(wordlist) as f:
        hosts = [line.strip() for line in f]

    items = [(url, h) for h in hosts]
    run_threads(vhost_task, items, threads)
