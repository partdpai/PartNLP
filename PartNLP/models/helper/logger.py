"""
        PartNLP
            AUTHORS:
                MOSTAFA & SAMAN
"""
import sys
import time
import threading
from .color import Color as clr
from terminaltables import AsciiTable

LOG_ENABLED = True


class Logger:

    def __init__(self, out_stream, log_profiling=False):
        self.out, self.log_profiling = out_stream, log_profiling
        self.profile = {}

    def reset(self):
        self.profile = {}

    def start(self, fname):
        if self.log_profiling:
            self.info(f"{fname} is statrted")

        if fname not in self.profile:
            self.profile[fname] = {
                'current': None, 'total': 0, 'calls': 0
            }
        self.profile[fname]['current'] = time.clock()
        self.profile[fname]['calls'] += 1

    def finish(self, fname):
        if self.log_profiling:
            self.info(f"{fname} is Finished.")
        self.profile[fname]['total'] += time.clock() - \
                                        self.profile[fname]['current']

    def condense_profile(self):
        """combines functions of the same name running on different threads."""
        new_profile = {}
        for k in self.profile:
            func_name = k.split(",")[0]
            if func_name in new_profile:
                new_profile[func_name]['calls'] += self.profile[k]['calls']
                new_profile[func_name]['total'] += self.profile[k]['total']
            else:
                new_profile[func_name] = {'calls': self.profile[k]['calls'],
                                          'total': self.profile[k]['total']}
        self.profile = new_profile
        return self.profile

    def print_profile(self):
        self.condense_profile()
        table_data = [[f'{clr.header} function name {clr.endc}',
                       f'{clr.header}# of calls{clr.endc}',
                       f'{clr.header}time per call{clr.endc}',
                       f'{clr.header}total time{clr.endc}']]
        for k in self.profile:
            calls = self.profile[k]['calls']
            total = self.profile[k]['total']
            time_pre_call = total / calls
            table_data.append([f'{clr.blue}{k}{clr.endc}',
                               f'{clr.blue}{calls}{clr.endc}',
                               f'{clr.blue}{time_pre_call}{clr.endc}',
                               f'{clr.blue}{total}{clr.endc}'])
        table = AsciiTable(table_data)
        self.out.write(table.table)

    def __call__(self, *args, **kwargs):
        self.info(*args)

    def info(self, msg):
        self.out.write(clr.green)
        self.out.write(time.asctime().split()[3] + ' - ')
        self.out.write(clr.Yellow)
        self.out.write(clr.Yellow + msg + '\n')
        self.out.write(clr.header)

    def writeln(self, msg):
        self.out.write(clr.blue)
        self.out.write(msg + '\n')
        self.out.write(clr.header)


global_logger = Logger(sys.stdout)


def wrap_with_log(func, logger=global_logger):
    """Wraps specified functions of an object with logger.start and logger.finish"""
    def wrap(*args, **kwargs):
        logger.start(func.__name__ + "," + str(threading.get_ident()))
        result = func(*args, **kwargs)
        logger.finish(func.__name__ + "," + str(threading.get_ident()))
        return result

    wrap.__name__ = func.__name__
    return wrap
