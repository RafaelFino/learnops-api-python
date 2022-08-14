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

## Availables APIs:
| Name | Description | HTTP return | Swaggger | Args | Return type |
|-|-|:-:|:-:|:-:|:-:|
| [ping](https://github.com/RafaelFino/learnops-api-python/blob/main/doc/images/ping.png) | A ping pong example API | &#x10102; | &#x10102; | &#x10102; | text |
| [example](https://github.com/RafaelFino/learnops-api-python/blob/main/doc/images/example.png) | Simple api, using swagger | &#x2713; | in code | &#x10102; | json body |
| [hello](https://github.com/RafaelFino/learnops-api-python/blob/main/doc/images/hello.png) | Api with one path GET method | &#x2713; | in file | in path | json body |
| [body](https://github.com/RafaelFino/learnops-api-python/blob/main/doc/images/body.png) | Api with one POST method, passing args in body | &#x2713; | in file | in body | json body |
| [sum](https://github.com/RafaelFino/learnops-api-python/blob/main/doc/images/sum.png) | Api with methods, with args | &#x2713; | in file | in body | json body |
| [crud](https://github.com/RafaelFino/learnops-api-python/blob/main/doc/images/crud.png) | Simple REST CRUD example, to show REST Methods | &#x2713; | on file per method | in body and path | json body |
| [currency](https://github.com/RafaelFino/learnops-api-python/blob/main/doc/images/currency.png) | Api to query and convert currency values, args on path and body | &#x2713; | on file per method | in body and path | json body |
| [auth](https://github.com/RafaelFino/learnops-api-python/blob/main/doc/images/auth.png) | Api to show a how a login works | &#x2713; | on file per method | in body and header | json body |
| [auth-jwt](https://github.com/RafaelFino/learnops-api-python/blob/main/doc/images/auth-jwt.png) | Login Api example with JWT | &#x2713; | on file per method | in body and header | json body |

## More info
[PT-BR Documentation](https://github.com/RafaelFino/learnops-api-python/blob/main/doc/index-PT-BR.md)
