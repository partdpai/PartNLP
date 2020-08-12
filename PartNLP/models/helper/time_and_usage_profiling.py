"""
        SEMANTIC SEARCH ENGINE
            AUTHORS:
                MOSTAFA & po_oya
"""
from time import perf_counter
import psutil as p
from terminaltables import AsciiTable
from PartNLP.models.helper.color import Color


def profile(func):
    """
          Wrapper Profiler
    """
    def wrap(*args, **kwargs):
        start_time = perf_counter()
        result = func(*args, **kwargs)
        func_time = perf_counter() - start_time
        usage = [[f'{Color.GREEN}MEMORY USAGE{Color.ENDC}',
                  f'{Color.BLUE}SWAP USAGE{Color.ENDC}',
                  f'{Color.HEADER}TIME{Color.ENDC}'],
                 [f'{Color.GREEN}{p.virtual_memory().percent}{Color.ENDC}',
                  f'{Color.BLUE}{p.swap_memory().percent}{Color.ENDC}',
                  f'{Color.HEADER}{float(func_time)}{Color.ENDC}']]
        usage_table = AsciiTable(usage)
        usage_table.title = f'{Color.FAIL}{func.__name__} profiling{Color.ENDC}'
        print('\n')
        print(usage_table.table)
        return result
    return wrap
