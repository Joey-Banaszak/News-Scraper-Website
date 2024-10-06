class Config(object):
    HOST = '142.11.219.155'      
    DATABASE = '440 Prog'  # fill with database name
    USER = 'dbguy'      
    PASSWORD = 'P@ssword69'  
    PORT = 3306

    CHARSET = 'utf8'
    UNICODE = True
    WARNINGS = True

    @classmethod
    def dbinfo(cls):
        return {
            'host': cls.HOST,
            'database': cls.DATABASE,
            'user': cls.USER,
            'password': cls.PASSWORD,
            'charset': cls.CHARSET,
            'use_unicode': cls.UNICODE,
            'get_warnings': cls.WARNINGS,
            'port': cls.PORT,
        }
