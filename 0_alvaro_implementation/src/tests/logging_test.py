from loguru import logger

# DEBUG -  to provide a view on the internal workings of your application - parameters, variables, other relevant data.
# INFO - information about function activities, used to track the flow of your application
# WARNING - to indicate potential issues or anomalies that while not error, deserve attention
# ERROR
# CRITICAL

logger.add('app.log', rotation='1 MB') # rotation='10:00', rotation='1 week', retention='10 days'
logger.add('error.log', rotation='1 MB', level='ERROR')

@logger.catch
def divide_by(a, b):
    logger.warning("Divide by zero can cause trouble")
    logger.info("Executing divide_by")
    logger.debug(f"Dividing {a} by {b}")
    return a/b    

try:
    res = divide_by(2,0)
except:
    logger.error("Division by zero")