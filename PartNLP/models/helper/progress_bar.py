"""
        SEMANTIC SEARCH ENGINE
            AUTHORS:
                MOSTAFA & SAMAN
"""
import time
import concurrent.futures
import functools
from tqdm import tqdm


def progress_bar(expected_time, increments=10):
    def _progress_bar(func):
        def timed_progress_bar(future, expected_time, increments=10):
            """
            Display progress bar for expected_time seconds.
            Complete early if future completes.
            Wait for future if it doesn't complete in expected_time.
            """
            interval = expected_time / increments
            with tqdm(total=increments) as pbar:
                for i in range(increments - 1):
                    if future.done():
                        # finish the progress bar
                        # not sure if there's a cleaner way to do this?
                        pbar.update(increments - i)
                        return
                    else:
                        time.sleep(interval)
                # if the future still hasn't completed, wait for it.
                future.result()
                pbar.update()

        @functools.wraps(func)
        def _func(*args, **kwargs):
            with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
                future = pool.submit(func, *args, **kwargs)
                timed_progress_bar(future, expected_time, increments)
            return future.result()
        return _func
    return _progress_bar
