from to_sentry.config_parser import ToSentryConfigParser

import raven
import raven.events
import urllib2
import warnings

def usage():
    print "Usage: to_sentry <sentry feed> Subject line ... " 

def send(argv, stdin, client_factory=raven.Client):
    if len(argv) < 2:
        usage()
        return 1
    client = client_factory(dsn=ToSentryConfigParser()[argv[1]])
    data = stdin.read()
    if data:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            client.capture('Message', 
                           message=' '.join(argv[2:]),
                           data = None,
                           extra = {'stdin':data})
            
