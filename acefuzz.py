from modules.dirfuzz import run_dirfuzz
from modules.subdomain import run_subdomain
from modules.vhost import run_vhost
import argparse
import time
from datetime import timedelta

def main():
    parser = argparse.ArgumentParser("AceFuzz")
    sub = parser.add_subparsers(dest="mode")

    d = sub.add_parser("dir")
    d.add_argument("-u", required=True)
    d.add_argument("-w", required=True)
    d.add_argument("-t", type=int, default=50)

    s = sub.add_parser("subdomain")
    s.add_argument("-d", required=True)
    s.add_argument("-w", required=True)
    s.add_argument("-t", type=int, default=50)

    v = sub.add_parser("vhost")
    v.add_argument("-u", required=True)
    v.add_argument("-w", required=True)
    v.add_argument("-t", type=int, default=50)

    args = parser.parse_args()

    if args.mode == "dir":
        run_dirfuzz(args.u, args.w, args.t)

    elif args.mode == "subdomain":
        run_subdomain(args.d, args.w, args.t)

    elif args.mode == "vhost":
        run_vhost(args.u, args.w, args.t)

if __name__ == "__main__":
    main()
