from connection import Connection 
import time 

# define the class Pilot
class Prev_search:

    
    def __init__( self, config_dic, prev_search = "", time = 0 ):
        self.__time = time
        self.__search = prev_search
        self.__config = config_dic

# getters 
    def get_search( self ):
        return self.__search 
    
    def get_time( self ):
        return self.__time 

# setters 
    def set_search( self, search ):
        self.__search = search
        
    def set_time( self, time = time.time() ):
        self.__search = time

    def save( self ):

        # create a connection to the db 
        conn = Connection(self.__config)

        # select prev searches
        sql = "select * from Prev_search"

        result = list(conn.run_select(sql))

        for da_result in result: 

            # check if the result has already been searched 
            if da_result.__time == self.__time:

                # if so update the time
                da_result.set_time(self)

            # otherwise, 
            else: 

                # add it to the db 
                 sql = "insert into Prev_search(search, time_searched) values (%s, %s)"
                 values = [ str( self.get_search() ), str( self.get_time() ) ]

            result = conn.commit_changes(sql, values)
            if result == 1:
                return True
            else:
                return False
        
        