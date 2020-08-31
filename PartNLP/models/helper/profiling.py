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
        usage = [[f'{Color.green}MEMORY USAGE{Color.endc}',
                  f'{Color.blue}SWAP USAGE{Color.endc}',
                  f'{Color.header}TIME{Color.endc}'],
                 [f'{Color.green}{p.virtual_memory().percent}{Color.endc}',
                  f'{Color.blue}{p.swap_memory().percent}{Color.endc}',
                  f'{Color.header}{float(func_time)}{Color.endc}']]
        usage_table = AsciiTable(usage)
        usage_table.title = f'{Color.fail}{func.__name__} profiling{Color.endc}'
        print('\n')
        print(usage_table.table)
        return result
    return wrap
