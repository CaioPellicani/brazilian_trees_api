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
                        "description":"Retorna essa mensagem",
                        "title": "Página Inicial"
                    },
                    {  
                        "Route":"/trees/id/<int>",
                        "methods":["GET", "PUT"],
                        "description":"Retorna/atualiza os dados da arvore com o <int> enviado",
                        "title": "Busca por código"
                    },
                    {  
                        "Route":"/trees/scientific_name/<string>",
                        "methods":["GET"],
                        "description":"Retorna os dados da arvore com o nome cientifico <string> enviado",
                        "title": "Busca por nome científico"
                    },
                    {  
                        "Route":"/trees/botanical_family/<string>",
                        "methods":["GET"],
                        "description":"Retorna os dados das arvores da familia <string> enviada",
                        "title": "Busca por família"
                    },
                    {  
                        "Route":"/trees/ecological_class/<string>",
                        "methods":["GET"],
                        "description":"Retorna os dados das arvores da classe ecologica <string> enviada",
                        "title": "Busca por classe ecológica"
                    }
                ]
            
            }
        }
    )) 