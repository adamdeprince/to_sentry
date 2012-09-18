from to_sentry.config_parser import ToSentryConfigParser

import raven
import raven.events
import urllib2
import warnings
import logging 



def usage():
    print "Usage: to_sentry <sentry feed> Subject line ... " 

def send(argv, stdin, client_factory=raven.Client):
    if len(argv) < 2:
        usage()
        return 1

    data = stdin.read()
    logger = logging.getLogger("sentry.errors")
    handler = logging.StreamHandler()
    formatter = logging.Formatter("[%(levelname)s] %(name)s: %(message)s\n\nOriginal application error follows:\n" + data)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        client = client_factory(dsn=ToSentryConfigParser()[argv[1]])
        if data:
            client.capture('Message', 
                           message=' '.join(argv[2:]),
                           data = None,
                           extra = {'stdin':data})
