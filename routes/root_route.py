from flask import Blueprint, json
from modules.db import get_db_connection
import sqlite3


RootRoute = Blueprint('test', __name__,)

@RootRoute.route('/')
def test():
    result=[]
    conn = get_db_connection()
    query="SELECT t.id, scientific_name, height_max ,e.ecological_class, f.botanical_family,\
           ( SELECT popular_name FROM tb_popular_names WHERE tree = t.id) AS popular_name\
           FROM tb_trees t\
           LEFT JOIN tb_ecological_class e ON e.id = t.ecological_class\
           LEFT JOIN tb_botanical_family f ON f.id = t.botanical_family"

    trees = conn.execute( query ).fetchall()

    for tree in trees:
        tree_data={
            'scientific_name' : tree["scientific_name"],
            'height_max'      : tree["height_max"],
            'ecological_class': tree["ecological_class"],
            'botanical_family': tree["botanical_family"],
        }

        names = []
        query = "SELECT popular_name FROM tb_popular_names WHERE tree = %s" % tree["id"]
        for name in conn.execute( query ).fetchall():
            names.append( name['popular_name'] )
            
        tree_data['popular_name'] = names
        result.append(tree_data)

    conn.close()
    return json.dumps(result)