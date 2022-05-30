from flask import Blueprint, jsonify, make_response

Greetings = Blueprint('greetings', __name__,)

@Greetings.route('/')
def greetings():
    return make_response( jsonify(  
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
    )) 