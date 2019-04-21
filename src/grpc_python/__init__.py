import logging
from grpc_python import config

logging.getLogger(__name__).addHandler(logging.NullHandler())

for var in config.__dict__:
    if isinstance(var, (float, int, str, list, dict)):
        logging.info("{} = {}".format(var, config.__dict__[var]))
