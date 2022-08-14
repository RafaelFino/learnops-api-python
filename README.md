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
| Name | Description | HTTP return | Swaggger | Args | Return type | Sequence Diagram | 
|-|-|:-:|:-:|:-:|:-:|:-:| 
| [ping](https://github.com/RafaelFino/learnops-api-python/tree/main/app/ping) | A ping pong example API | &#x10102; | &#x10102; | &#x10102; | text | ![ping](https://github.com/RafaelFino/learnops-api-python/raw/main/doc/images/ping.png)|
| [example](https://github.com/RafaelFino/learnops-api-python/tree/main/app/example) | Simple api, using swagger | &#x2713; | in code | &#x10102; | json body | ![ping](https://github.com/RafaelFino/learnops-api-python/raw/main/doc/images/example.png)|
| [hello](https://github.com/RafaelFino/learnops-api-python/tree/main/app/hello) | Api with one path GET method | &#x2713; | in file | in path | json body | ![ping](https://github.com/RafaelFino/learnops-api-python/raw/main/doc/images/hello.png)|
| [body](https://github.com/RafaelFino/learnops-api-python/tree/main/app/body) | Api with one POST method, passing args in body | &#x2713; | in file | in body | json body | ![ping](https://github.com/RafaelFino/learnops-api-python/raw/main/doc/images/body.png)|
| [sum](https://github.com/RafaelFino/learnops-api-python/tree/main/app/sum) | Api with methods, with args | &#x2713; | in file | in body | json body | ![ping](https://github.com/RafaelFino/learnops-api-python/raw/main/doc/images/sum.png)|
| [crud](https://github.com/RafaelFino/learnops-api-python/tree/main/app/crud) | Simple REST CRUD example, to show REST Methods | &#x2713; | on file per method | in body and path | json body | ![ping](https://github.com/RafaelFino/learnops-api-python/raw/main/doc/images/crud.png)|
| [currency](https://github.com/RafaelFino/learnops-api-python/tree/main/app/currency) | Api to query and convert currency values, args on path and body | &#x2713; | on file per method | in body and path | json body | ![ping](https://github.com/RafaelFino/learnops-api-python/raw/main/doc/images/currency.png) |
| [auth](https://github.com/RafaelFino/learnops-api-python/tree/main/app/auth) | Api to show a how a login works | &#x2713; | on file per method | in body and header | json body | ![ping](https://github.com/RafaelFino/learnops-api-python/raw/main/doc/images/auth.png)|
| [auth-jwt](https://github.com/RafaelFino/learnops-api-python/tree/main/app/auth-jwt) | Login Api example with JWT | &#x2713; | on file per method | in body and header | json body | ![ping](https://github.com/RafaelFino/learnops-api-python/raw/main/doc/images/auth-jwt.png)|

## More info
[PT-BR Documentation](https://github.com/RafaelFino/learnops-api-python/blob/main/doc/index-PT-BR.md)

## Sequence diagrams automated by [seqdiag](https://pypi.org/project/seqdiag/), thanks!
