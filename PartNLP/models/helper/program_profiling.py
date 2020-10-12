"""
        SEMANTIC SEARCH ENGINE
            AUTHORS:
                MOSTAFA & po_oya
"""
from terminaltables import AsciiTable
from PartNLP.models.helper.color import Color


def show_program_profile(**kwargs):
    """
          program profiler
    """
    usage = [[f'{Color.green}PACKAGE{Color.endc}',
              f'{Color.blue}BATCH_SIZE{Color.endc}',
              f'{Color.yellow}TIME{Color.endc}',
              f'{Color.fail}MULTIPROCESS TYPE{Color.endc}',
              f'{Color.black}{Color.bold}GIVEN FILE SIZE{Color.endc}',
              f'{Color.header}OPERATIONS{Color.endc}'],
             [f'{Color.green}{kwargs["config"]["package"]}{Color.endc}',
              f'{Color.blue}{kwargs["config"]["batchSize"]}(bytes){Color.endc}',
              f'{Color.yellow}{round(kwargs["program_time"], 1)}(seconds){Color.endc}',
              f'{Color.fail}{kwargs["config"]["multiProcessType"]}{Color.endc}',
              f'{Color.black}{Color.bold}{kwargs["file_size"]/1000000}(megaBytes){Color.endc}',
              f'{Color.header}{kwargs["config"]["operations"]}{Color.endc}']]
    usage_table = AsciiTable(usage)
    usage_table.title = f'{Color.fail}PartNLP profile{Color.endc}'
    print('\n')
    print(usage_table.table)
