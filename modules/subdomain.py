import dns.resolver
from core.utils import run_threads

def sub_task(sub):
    try:
        dns.resolver.resolve(sub, "A")
        print(f"[+] Subdomain: {sub}")
    except:
        pass

def run_subdomain(domain, wordlist, threads=50):
    with open(wordlist) as f:
        subs = [f"{w.strip()}.{domain}" for w in f]

    run_threads(sub_task, subs, threads)
