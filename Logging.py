import logging
"""5 levels of logging - DEBUG, INFO, WARNING, ERROR and CRITICAL. If level is WARNING, warning and above 
will be shown. For disabling, highest need to be disable to disable all. """

logging.basicConfig(filename='Files\\myProgramLog.txt',level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)
logging.debug('Start of program')
def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1,n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s)' %(n))
    return total
print(factorial(5))
logging.debug('End of program')

logging.debug('--------------------------------')

logging.debug('Some debugging details.')
logging.info('The logging module is working.')
logging.warning('An error message is about to be logged.')
logging.error('An error has occurred.')
logging.critical('The program is unable to recover!')