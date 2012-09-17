from ConfigParser import ConfigParser, Error

class ToSentryConfigParser(ConfigParser):

    CONFIG_FILE = "/etc/to_sentry.conf"

    def __init__(self, *args, **kwargs):
        ConfigParser.__init__(self, *args, **kwargs)
        if not self.read(self.CONFIG_FILE):
            raise IOError("%r not readable." % (self.CONFIG_FILE,))
        
    def __getitem__(self, key):
        try:
            return self.get(key, "url")
        except Error:
            if key.startswith('http://') or key.startswith('https://'):
                return key
            else:
                raise Error(key)
    
