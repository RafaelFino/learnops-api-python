# Learnops API with Python
APIs with Python - Intro with KillerCoda

# Quick Start
1. Create an Ubuntu instance in [KillerCoda](https://killercoda.com/playgrounds/scenario/ubuntu)

2. Run This command on VM Terminal:
```
curl https://raw.githubusercontent.com/RafaelFino/learnops-api-python/main/prepare.sh | bash && zsh
```

3. To execute server, on application path (~/learnops-api-python):
```
./run-server.sh {api-name}
```

4. To execute clients, on application path (~/learnops-api-python):
```
./run-client.sh {api-name}
```

Availables APIs:
| Name | Description | Using swagger | HTTP Return |
|-|-|:-:|:-:|
| ping | A ping pong example API | &#x10102; | &#x10102; |
| example | Simple api, using swagger | &#x2713; | 	&#x10102; |
| hello | Api with one path GET method | &#x2713; | &#x2713; |
| body | Api with one POST method, passing args in body | &#x2713; | &#x2713; |
| sum | Api with methods, with args | &#x2713; | &#x2713; |
