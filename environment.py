"""
Feature Test Environment functions
"""
# general imports
import csv
import logging

logging.basicConfig(
    filename='./stats/stats.log',
    filemode='a',
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
    level=logging.DEBUG,
)

logger = logging.getLogger(__name__)

stats_file = './stats/stats.csv'


def after_scenario(context, scenario):
    if context.input_file and context.input_file == 'input.txt':
        data = [context.year, context.day, context.funcname, context.timer, context.feature.name]
        with open(stats_file, 'a') as f:
            writer = csv.writer(f)
            writer.writerow(data)
