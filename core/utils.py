from concurrent.futures import ThreadPoolExecutor, as_completed

def run_threads(func, items, threads):
    results = []
    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(func, item) for item in items]

        for future in as_completed(futures):
            res = future.result()
            if res:
                results.append(res)

    return results
