# Mitigação de riscos e boas práticas
Existem muitas [boas práticas](https://www.crummy.com/writing/speaking/2008-QCon/act3.html) envolvidas ao se construir sistemas que irão expor APIs, algumas relacionadas a arquitetura e outras a segurança

## Fontes e links uteis:
- https://renatogroffe.medium.com/asp-net-core-boas-pr%C3%A1ticas-na-implementa%C3%A7%C3%A3o-de-apis-rest-setembro-2019-1d4f6b6e8352
- https://imasters.com.br/back-end/6-melhores-praticas-para-arquiteturas-baseadas-em-microservices

## APIs de Healthcheck
É um tipo de serviço nos sistemas que expõem APIs capaz de informar se esse serviço está funcionando adequadamente, ou seja, se está capacitado a responder requisições a ele feitas

O Health Checks nada mais é que um middleware que nos fornecem um endpoint configurável que nos retorna o estado atual da aplicação.

### Fontes e links uteis:
- https://balta.io/blog/aspnet-health-check

## Arquitetura de CircuitBraker
É um desenho de arquitetura que, ao identificar que um serviço/API não está saudável para receber requisições, entra em um modo de recuperação (falha rapidamente) e evita que o acumulo de requisições piore o seu estado já degradado.

Atualmente são bem conhecidas as vantagens que uma arquitetura microservices possui. Dentre muitas, podemos citar como exemplo: aplicações distribuídas na nuvem, baixo acoplamento, reusabilidade e agilidade para o negócio. Mas, ao mesmo tempo, esta é uma arquitetura frágil porque quando falamos de um sistema distribuído sabemos que cada ação do usuário invocará diversos serviços separados. O que antes — na arquitetura monolítica — eram chamadas in-memory, agora são remotas através da rede, o que funciona muito bem quando os serviços estão online e rodando.

Mas o que acontece quando um ou mais serviços ficam indisponíveis ou respondem com alta latência (o infame time out)? Estes casos quando não tratados podem levar a falhas em cascata afetando diversos serviços da empresa.

O padrão de projeto (Design Pattern) [Circuit Breaker](https://en.wikipedia.org/wiki/Microservices) ajuda a evitar a ocorrência dessas falhas em cascata. Ele permite que você construa um serviço tolerante a falhas e resiliente que consiga sobreviver quando os principais serviços que ele consome estiverem indisponíveis ou com alta latência.

### Problemas ocorrem
> “A sabedoria consiste na antecipação das consequências”. Norman Cousins

Vamos combinar, todos os serviços falharão em algum momento, é tudo uma questão de tempo. Os Circuit Breakers permitem que o sistema lide com essas falhas normalmente. Ao aplicar este padrão, estamos antecipando possíveis problemas (ou consequências 😃) da aplicação. A tradução literal de Circuit Breaker é “disjuntor”, e a finalidade desse padrão de projeto é a mesma deste aparelho. O conceito é simples e direto. Ele envolve uma função com uma regra que monitora e rastreia possíveis falhas. Quando uma falha ocorre determinado número de vezes, o “disjuntor cai” e protege o sistema para evitar as falhas catastróficas. Para entender melhor, vamos analisar os seus três estados: Closed, Open e Half-Open:
|[Diagrama](https://martinfowler.com/bliki/CircuitBreaker.html)|
|-|
|![circuit-breker-diagram](https://martinfowler.com/bliki/images/circuitBreaker/state.png) |
|  |

- **Closed**: Quando tudo está normal, o Circuit Breaker permanece Closed e todas as chamadas para os serviços ocorrem normalmente. Se o número de falhas excede um limite predeterminado, o estado muda para Open.

- **Open**: Neste estado, o Circuit Breaker não executará a chamada do serviço e retornará um erro tratado (existem casos que, ao invés disso, pode retornar uma informação do cache).

- **Half-Open**: Após um período, o estado é alternado para Half-Open para testar se o problema original ainda ocorre. Se uma única falha ocorrer, o estado será alternado para Open novamente. Se for bem-sucedido, ele volta ao normal (Closed).

### Implementações
Existem várias maneiras de implementar este Design Pattern no seu projeto. Você pode implementar seu próprio algoritmo utilizando o paradigma preferido (orientação a objetos, funcional, etc). Outra opção é utilizar alguma biblioteca já pronta. Na minha opinião, não existe certo ou errado, mas prefiro sempre aproveitar a experiê ncia e maturidade dessas ferramentas já utilizadas por outros desenvolvedores. Durante a elaboração deste post conheci diversas opções, vou listar algumas:

- **Hystrix**: Este é de longe o mais famoso de todos. É uma biblioteca Java criada pelo Netflix. O Hystrix também possui um dashboard próprio para monitorar os serviços.
- **PyBreaker**: Como o nome já entrega, esta é uma biblioteca do Python. É uma das mais famosas — de acordo com o git stars ⭐️— da linguagem.
- **Polly**: O Polly é uma biblioteca que garante a resiliência de aplicações .NET. Ela implementa diversos algoritmos para garantir isso, um deles é o Circuit Breaker.
- **Opossum**: Uma das bibliotecas Circuit Breakers para Node. (Existem muitas opções)


### Fontes e links uteis:
- https://martinfowler.com/bliki/CircuitBreaker.html
- https://medium.com/trainingcenter/design-pattern-para-microservices-circuit-breaker-f4a5b68f73d1
- https://en.wikipedia.org/wiki/Microservices

## Cache
Uma cache é um bloco de memória para o armazenamento temporário de dados que possuem uma grande probabilidade de serem utilizados novamente. Uma definição mais simples de cache poderia ser: uma área de armazenamento temporária onde os dados frequentemente acedidos são armazenados para acesso rápido.

O propósito do cache é acelerar a busca de dados que são muito utilizados e poupar a utilização de recursos de um servidor. Com o cache, você tem os seguintes benefícios na sua API: Redução da latência de rede. Redução de carga de processamento dos servidores.

|[Diagrama](https://womakerscode.gitbook.io/pwa-workshop/4.-estrategia-de-cache-para-rest-api)|
|:-:|
|![cache_diagram](https://149276298-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-Lm0i7_LcOK6f63R9uAb%2F-Lm2KHIe2YW1uL0db7oY%2F-Lm2K_uRqreSUQmUkQRm%2Fimage.png?alt=media&token=e08f012e-e25e-4b7f-891f-51b449933cfa)|
### Fontes e links uteis:
- https://en.wikipedia.org/wiki/Cache_(computing)
- https://developer.mozilla.org/pt-BR/docs/Web/API/Cache
- https://womakerscode.gitbook.io/pwa-workshop/4.-estrategia-de-cache-para-rest-api

## Swagger e OpenAPI
#### Fontes e links uteis:
- https://swagger.io/docs/specification/about/
- https://gr1d.io/2022/04/15/swagger/
- https://medium.com/@ronilsonribeiro/como-interpretar-um-swagger-cdc331b68804
