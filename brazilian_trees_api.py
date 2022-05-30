from genericpath import exists
from flask import Flask, make_response, jsonify, render_template
from routes.root_route import RootRoute
from routes.trees_routes import routeTrees
from modules.db import create_db

if( not exists( "database.db" ) ):
    create_db()

app = Flask(__name__)

app.register_blueprint(RootRoute, url_prefix='/root')
app.register_blueprint(routeTrees, url_prefix='/trees')

@app.route('/' )
def greetings():
    return render_template("menu.html", data=  
        {   
            "Authors":{
                "institution":"Fatec Ribeirão Preto",
                "name":["Aline Mizumukai", "Caio Damasceno Pellicani"],
                "about":"Trabalho avaliativo desenvolvido em Python com uso do framework Flask",
            },
            "apiDescription":{
                "name":"Brazilian Trees Api",
                "about":"Api desenvolvida com o objetivo de armazenar e acessar dados de especies arboreas nativas dos diferentes biomas do Brasil",
                "endpoints":[
                    {  
                        "Route":"/",
                        "methods":["GET"],
                        "description":"retorna essa mensagem"
                    },
                    {  
                        "Route":"/trees/id/<int>",
                        "methods":["GET", "PUT"],
                        "description":"retorna/atualiza os dados da arvore com o <int> enviado"
                    },
                    {  
                        "Route":"/trees/scientific_name/<string>",
                        "methods":["GET"],
                        "description":"retorna os dados da arvore com o nome cientifico <string> enviado"
                    },
                    {  
                        "Route":"/trees/botanical_family/<string>",
                        "methods":["GET"],
                        "description":"retorna os dados das arvores da familia <string> enviada"
                    },
                    {  
                        "Route":"/trees/ecological_class/<string>",
                        "methods":["GET"],
                        "description":"retorna os dados das arvores da classe ecologica <string> enviada"
                    }
                ]
            
            }
        }
    )
     