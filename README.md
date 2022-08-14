# Learnops API with Python
APIs with Python - Intro with KillerCoda

## Quick Start
1. Create an Ubuntu instance in [KillerCoda](https://killercoda.com/playgrounds/scenario/ubuntu)

2. Run This command on VM Terminal:
```
curl https://raw.githubusercontent.com/RafaelFino/learnops-api-python/main/prepare.sh | bash && zsh
```

3. To execute server, on application path (~/learnops-api-python):
```
cd ~/learnops-api-python
source bin/activate
pip3 install -r requirements.txt

./run-server.sh {api-name}
```

4. To execute clients, on application path (~/learnops-api-python):
```
cd ~/learnops-api-python
source bin/activate

./run-client.sh {api-name}
```

## Available APIs:
| Name | Description | HTTP return | Swaggger | Args | Return type |
|-|-|:-:|:-:|:-:|:-:|
| [ping](https://github.com/RafaelFino/learnops-api-python/tree/main/app/ping) | A ping pong example API | &#x10102; | &#x10102; | &#x10102; | text |
| [example](https://github.com/RafaelFino/learnops-api-python/tree/main/app/example) | Simple api, using swagger | &#x2713; | in code | &#x10102; | json body |
| [hello](https://github.com/RafaelFino/learnops-api-python/tree/main/app/hello) | Api with one path GET method | &#x2713; | in file | in path | json body |
| [body](https://github.com/RafaelFino/learnops-api-python/tree/main/app/body) | Api with one POST method, passing args in body | &#x2713; | in file | in body | json body |
| [sum](https://github.com/RafaelFino/learnops-api-python/tree/main/app/sum) | Api with methods, with args | &#x2713; | in file | in body | json body |
| [crud](https://github.com/RafaelFino/learnops-api-python/tree/main/app/crud) | Simple REST CRUD example, to show REST Methods | &#x2713; | on file per method | in body and path | json body |
| [currency](https://github.com/RafaelFino/learnops-api-python/tree/main/app/currency) | Api to query and convert currency values, args on path and body | &#x2713; | on file per method | in body and path | json body |
| [auth](https://github.com/RafaelFino/learnops-api-python/tree/main/app/auth) | Api to show a how a login works | &#x2713; | on file per method | in body and header | json body |
| [auth-jwt](https://github.com/RafaelFino/learnops-api-python/tree/main/app/auth-jwt) | Login Api example with JWT | &#x2713; | on file per method | in body and header | json body |

### Diagrams
#### Ping
![ping](https://github.com/RafaelFino/learnops-api-python/raw/main/doc/images/ping.png)
#### Example
![example](https://github.com/RafaelFino/learnops-api-python/raw/main/doc/images/example.png)
#### Hello
![hello](https://github.com/RafaelFino/learnops-api-python/raw/main/doc/images/hello.png)
#### Body
![body](https://github.com/RafaelFino/learnops-api-python/raw/main/doc/images/body.png)
#### Sum 
![sum](https://github.com/RafaelFino/learnops-api-python/raw/main/doc/images/sum.png)
#### CRUD
![crud](https://github.com/RafaelFino/learnops-api-python/raw/main/doc/images/crud.png)
#### Currency
![currency](https://github.com/RafaelFino/learnops-api-python/raw/main/doc/images/currency.png)
#### Auth 
![auth](https://github.com/RafaelFino/learnops-api-python/raw/main/doc/images/auth.png)
#### Auth-JWT
![auth-jwt](https://github.com/RafaelFino/learnops-api-python/raw/main/doc/images/auth-jwt.png)


## More info
[Full documentation about APIs (PT-BR)](https://github.com/RafaelFino/learnops-api-python/blob/main/doc/index-PT-BR.md)

## Special Thanks!
- API managed with [Flask](https://flask.palletsprojects.com/en/2.2.x/)
- Sequence diagrams automated by [seqdiag](https://pypi.org/project/seqdiag/)
- Currency data from [economia.awesomeapi](https://economia.awesomeapi.com.br/all)
- Awesome texts about [JWT](https://tableless.com.br/entendendo-tokens-jwt/) and [how to handle it with Python](https://auth0.com/blog/how-to-handle-jwt-in-python/) by [Jessica Temporal](https://auth0.com/blog/authors/jessica-temporal/) and [Wellington Nascimento](https://tableless.com.br/authors/wellington-nascimento/)

**Thanks!**