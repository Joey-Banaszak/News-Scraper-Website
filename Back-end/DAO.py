from connection import Connection 
import time 
from flask import Flask, jsonify

app = Flask(__name__)
        
# define the class
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

    def save(self):
    conn = Connection(self.__config)
    
    # Insert the new search term into the database
    sql = "INSERT INTO Prev_search (search, time_searched) VALUES (%s, %s)"
    values = [self.get_search(), self.get_time()]
    
    conn.open_conn()
    cursor = conn.get_cursor()
    cursor.execute(sql, values)
    conn.commit_changes()
    conn.close_conn()

    @app.route('/get_last_search', methods=['GET'])
    def get_last_search():
        # Fetch the last search from the database
        conn = Connection(config_dic)
        sql = "SELECT search FROM Prev_search ORDER BY time_searched DESC LIMIT 1"
        result = conn.run_select(sql)
    
        if result:
            return jsonify({'last_search': result[0][0]})
        else:
            return jsonify({'last_search': None})
        
        
