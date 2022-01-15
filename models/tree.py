from markupsafe import string
from modules.db import get_db_connection

class Tree:
    def __init__( self, data ):
        self.id = data[ 'id' ]
        self.scientific_name = data[ 'scientific_name' ]
        self.height_max = data[ 'height_max' ]
        self.ecological_class = data[ 'ecological_class' ]
        self.botanical_family = data[ 'botanical_family' ]       

    def get( self ):
        result={
            'id' : self.id,
            'scientific_name' : self.scientific_name,
            'height_max'      : self.height_max,
            'ecological_class': self.ecological_class,
            'botanical_family': self.botanical_family,
            'popular_name': []        
        }
        
        conn = get_db_connection()
        query = "SELECT popular_name FROM tb_popular_names WHERE tree = %s" % self.id

        for name in conn.execute( query ).fetchall():
            result['popular_name'].append( name['popular_name'] )

        conn.close()   
        return result