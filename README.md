# Learnops API with Python
APIs with Python - Intro with KillerCoda

# Quick Start
1. Create an Ubuntu instance in [KillerCoda](https://killercoda.com/playgrounds/scenario/ubuntu)

2. Run This command on VM Terminal:
```
curl https://raw.githubusercontent.com/RafaelFino/learnops-api-python/main/prepare.sh | bash && zsh
```

3. Install python dependencies
```
pip3 install -r requirements.txt
```

4. To execute, on application path (~/learnops-api-python):
```
./run.sh {api-name}
```

Availables APIs:
| Name | Description |
|-|-|
| ping | A ping pong example API | 
| example | Simple api, using swagger |
| hello | Api with methods, with args, using swagger and HTTP returns |
