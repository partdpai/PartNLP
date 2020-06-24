"""In configuration script get preferred preprocessing options.
"""
import argparse
import os


def get_config():
    """
    :return: all set values(config)
    """
    args = get_args()
    config = {
        'text': '',
        'Language': args.language,
        'DatasetType': args.input_type,
        'InputFilePath': args.input,
        'OutputFilePath': args.output,
        'package': args.package,
        'processors': []
    }
    return config


def get_args():
    """Set default values or get values from command line.
    """
    input_default_path = ' '
    output_default_path = os.getcwd() + '/output.txt'
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='path to input dataset',
                        default=input_default_path)
    parser.add_argument('-o', '--output', help='path to the output directory',
                        default=output_default_path)
    parser.add_argument('-lang', '--language', default='en', help='text language')
    parser.add_argument('-itype', '--input_type', help='input format', default='txt')
    parser.add_argument('-otype', '--output_type', help='output format', default='txt')
    parser.add_argument('-p', '--package', help='name of toolkit', default='HAZM')
    args = parser.parse_args()
    if args.input is None or args.output is None:
        parser.print_usage()
        exit()
    return args
