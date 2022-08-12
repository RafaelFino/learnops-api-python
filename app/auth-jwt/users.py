# fake struct for users - simulates a database
class UserStorage:
    Users = { 'usuario1': 'senha1', 'usuario2': 'senha2' }

    ServerInfoUsers = { 
        'usuario1': {
            'claims': {
                'routes' : [
                    "query", "admin"
                ],
                'nick': 'Fulano'
            }
        }, 
        'usuario2': {
            'claims': {
                'routes' : [
                    "query"
                ],
                'nick': 'Beltrano'		 
            }
        }
    }