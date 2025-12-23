from core.requester import Requester
from core.utils import run_threads
from core.baseline import Baseline
from core.output import OutputManager

req = None
baseline = None

def dir_task(args):
    url, word = args
    target = f"{url}/{word}"

    r = req.get(target)

    if not r:
        return

    if baseline.is_fake(r):
        return

    if r.status_code in [200, 301, 302, 403]:
        print(f"[+] {target} ({r.status_code}) | len={len(r.text)}")

def run_dirfuzz(url, wordlist, threads=50):
    global req, baseline
    req = Requester()
    baseline = Baseline(url)

    print(f"[*] Baseline → status={baseline.status} length={baseline.length}")

    with open(wordlist) as f:
        words = [line.strip() for line in f if line.strip()]

    items = [(url, word) for word in words]
    run_threads(dir_task, items, threads)
