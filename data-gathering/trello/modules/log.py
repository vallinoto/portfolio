import logging
from datetime import datetime as dt
from sys import argv


def get_log_file_name(job_name):
    timestamp = dt.now()
    timestamp = f'{timestamp.month}_{timestamp.day}'

    return f'logs/{job_name}_{timestamp}.log'


def get_script_file_name():
    return argv[0].split('/')[-1].replace('.py', '')


def setup_logging():
    file_name = get_script_file_name()
    logging.basicConfig(
        format='%(asctime)s:%(name)s:%(levelname)s:%(message)s',
        filename=get_log_file_name(file_name), level=logging.DEBUG
    )


def get_logging_mark(mark='start'):
    file_name = get_script_file_name()
    return f'[{">" * 20} {file_name}: '\
        f'{"Iniciando..." if mark == "start" else "Fim."}]'


def start_logging():
    setup_logging()
    logging.info(get_logging_mark('start'))


def end_logging():
    logging.info(get_logging_mark('end'))