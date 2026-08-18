"""
Feature Test Environment functions
"""

# general imports
import csv
import os
import logging

# logging config
logging.basicConfig(
    filename='./stats/stats.log',
    filemode='a',
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
    level=logging.DEBUG,
)
# suppress parse WARNING
logging.getLogger('parse').setLevel(logging.WARNING)

# create logger
logger = logging.getLogger(__name__)

# stats file
stats_file = os.path.abspath('./stats/stats.csv')


# after scenario
def after_scenario(context, scenario):
    if context.input_file and context.input_file == 'input.txt':
        data = [context.year, context.day, context.funcname, context.timer, context.feature.name]
        with open(stats_file, 'a') as f:
            writer = csv.writer(f)
            writer.writerow(data)
