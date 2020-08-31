"""
        SEMANTIC SEARCH ENGINE
            AUTHORS:
                MOSTAFA & po_oya
"""
from terminaltables import AsciiTable
from PartNLP.models.helper.color import Color


def show_program_profile(package, batch_size, operations,
                         program_time, use_multiprocess, file_size):
    """
          program profiler
    """
    usage = [[f'{Color.green}PACKAGE{Color.endc}',
              f'{Color.blue}BATCH_SIZE{Color.endc}',
              f'{Color.yellow}TIME{Color.endc}',
              f'{Color.fail}USE MULTIPROCESS{Color.endc}',
              f'{Color.black}{Color.bold}GIVEN FILE SIZE{Color.endc}',
              f'{Color.header}OPERATIONS{Color.endc}'],
             [f'{Color.green}{package}{Color.endc}',
              f'{Color.blue}{batch_size}(bytes){Color.endc}',
              f'{Color.yellow}{round(program_time, 1)}(seconds){Color.endc}',
              f'{Color.fail}{use_multiprocess}{Color.endc}',
              f'{Color.black}{Color.bold}{file_size/1000000}(megaBytes){Color.endc}',
              f'{Color.header}{operations}{Color.endc}']]
    usage_table = AsciiTable(usage)
    usage_table.title = f'{Color.fail}PartNLP profile{Color.endc}'
    print('\n')
    print(usage_table.table)
