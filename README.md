# Learnops API with Python
APIs with Python - Intro with KillerCoda

Content aggregated and developed for the study about APIs

## Quick Start
1. Create an Ubuntu instance in [KillerCoda](https://killercoda.com/playgrounds/scenario/ubuntu)

2. Run This command on VM Terminal:
``` bash 
curl https://raw.githubusercontent.com/RafaelFino/learnops-api-python/main/prepare.sh | bash && zsh
```

3. Run the command, for application path (~/learnops-api-python):
``` bash 
cd ~/learnops-api-python
source bin/activate
pip3 install -r requirements.txt
```
4. Run command, to upload the server:
```bash
./run-server.sh {api-name}
```

> If you run **./run-server.sh** and don't provide the endpoint, you'll get the following return:
``` bash 
API name are expected! Try one of available options:
#       ping
#       example
#       hello
#       body
#       sum
#       crud
#       currency
#       auth
#       auth-jwt
```
5. Open a second tab in the console, to run the client commands

6. Run command, for application path (~/learnops-api-python):
``` bash 
cd ~/learnops-api-python
source bin/activate
```

7. Run the command to make the requests
``` bash
./run-client.sh {api-name}
```

## Available APIs:
| Name | Description | HTTP return | Swagger | Args | Return type | Diagram |
|-|-|:-:|:-:|:-:|:-:|:-:|
| [ping](https://github.com/RafaelFino/learnops-api-python/tree/main/app/ping) | A ping pong example API | &#x10102; | &#x10102; | &#x10102; | text |[ping diagram](https://github.com/RafaelFino/learnops-api-python/raw/main/doc/images/ping.png)|
| [example](https://github.com/RafaelFino/learnops-api-python/tree/main/app/example) | Simple API, using swagger | &#x2713; | in code | &#x10102; | json body |[example diagram](https://github.com/RafaelFino/learnops-api-python/raw/main/doc/images/example.png)|
| [hello](https://github.com/RafaelFino/learnops-api-python/tree/main/app/hello) | API with one path GET method | &#x2713; | in file | in path | json body |[hello diagram](https://github.com/RafaelFino/learnops-api-python/raw/main/doc/images/hello.png)|
| [body](https://github.com/RafaelFino/learnops-api-python/tree/main/app/body) | API with one POST method, passing args in body | &#x2713; | in file | in body | json body |[body diagram](https://github.com/RafaelFino/learnops-api-python/raw/main/doc/images/body.png)|
| [sum](https://github.com/RafaelFino/learnops-api-python/tree/main/app/sum) | A sum calc API, to show a simple service | &#x2713; | in file | in body | json body |[sum diagram](https://github.com/RafaelFino/learnops-api-python/raw/main/doc/images/sum.png)|
| [crud](https://github.com/RafaelFino/learnops-api-python/tree/main/app/crud) | REST API with CRUD example, to show REST Methods | &#x2713; | indivual files | in body and path | json body |[crud diagram](https://github.com/RafaelFino/learnops-api-python/raw/main/doc/images/crud.png)|
| [currency](https://github.com/RafaelFino/learnops-api-python/tree/main/app/currency) | API to query and convert currency values, args on path and body | &#x2713; | indivual files | in body and path | json body |[currency diagram](https://github.com/RafaelFino/learnops-api-python/raw/main/doc/images/currency.png)|
| [auth](https://github.com/RafaelFino/learnops-api-python/tree/main/app/auth) | Simple API to show a how a login and token works | &#x2713; | indivual files | in body and header | json body |[auth diagram](https://github.com/RafaelFino/learnops-api-python/raw/main/doc/images/auth.png)|
| [auth-jwt](https://github.com/RafaelFino/learnops-api-python/tree/main/app/auth-jwt) | Login API example with JWT | &#x2713; | indivual files | in body, header and path | json body |[auth-jwt diagram](https://github.com/RafaelFino/learnops-api-python/raw/main/doc/images/auth-jwt.png)|

## More info
1. [Distributed Systems](https://github.com/RafaelFino/learnops-api-python/blob/main/doc/PT-BR/distributed-systems.md)
2. [What is an API?](https://github.com/RafaelFino/learnops-api-python/blob/main/doc/PT-BR/api.md)
3. [HTTP Pattern](https://github.com/RafaelFino/learnops-api-python/blob/main/doc/PT-BR/http.md)
4. [REST APIs](https://github.com/RafaelFino/learnops-api-python/blob/main/doc/PT-BR/rest.md)
5. [JSON Format](https://github.com/RafaelFino/learnops-api-python/blob/main/doc/PT-BR/json.md)
6. [Auth and Sec](https://github.com/RafaelFino/learnops-api-python/blob/main/doc/PT-BR/sec.md)
6. [JWT - Json Web Token](https://github.com/RafaelFino/learnops-api-python/blob/main/doc/PT-BR/jwt.md)
7. [Micro Services and APIs](https://github.com/RafaelFino/learnops-api-python/blob/main/doc/PT-BR/micro-services.md)
8. [Arch and best pratices](https://github.com/RafaelFino/learnops-api-python/blob/main/doc/PT-BR/best-pratices.md)

## Special Thanks!
- API managed with [Flask](https://flask.palletsprojects.com/en/2.2.x/)
- OpenAPI automated interface and Swagger with [flasgger](https://github.com/flasgger/flasgger)
- Sequence diagrams automated by [seqdiag](https://pypi.org/project/seqdiag/)
- Currency data from [economia.awesomeapi](https://economia.awesomeapi.com.br/all)
- Awesome texts about [JWT](https://tableless.com.br/entendendo-tokens-jwt/) and [how to handle it with Python](https://auth0.com/blog/how-to-handle-jwt-in-python/) by [Jessica Temporal](https://auth0.com/blog/authors/jessica-temporal/) and [Wellington Nascimento](https://tableless.com.br/authors/wellington-nascimento/)
- Table of contents made with [extracttoc](https://pypi.org/project/extracttoc/)
- Python JWT examples made with [pyjwt](https://pyjwt.readthedocs.io/en/stable/)
- Python Criptografy examples made with [cryptography](https://cryptography.io/en/latest/)
- An excelent and very complete [article](https://kinsta.com/pt/blog/microservicos-vs-api/) comparing APIs and Microservices from [Durga Prasad Acharya](https://kinsta.com/pt/blog/author/durga/)

**Thanks!**
