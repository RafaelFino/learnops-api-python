# APIs
## Desafios dos sistemas distrubuídos
### O que é um sistema distribuído?
Para entender o conceito de sistemas distribuídos, antes é importante entender o que é um sistema centralizado.

Um sistema centralizado pode ser definido como um processo onde apenas um ator controla todas as etapas para se chegar ao objetivo desse processo. Nesse caso o processo é totalmente gerenciado em um ponto comum de controle e acontece de forma sequêncial, com esse operador fazendo uma etapa de cada vez. Nesse modelo o operador precisa ter conhecimento e controle de todas as etapas do processo.

Em um sistema distribuído, cada etapa é dividida em pedaços menores e realizados por diferentes operadores, diminuindo a complexidade de cada etapa e aumentando a produtividade em escala. Porém com essa abordagem uma série de novas desafios aparecem:

 - Como cada parte se comunica? 
 - Como é feita a gestão dos processos?

Um exemplo prático para comparar as duas diferentes abordagens é uma produção de um artesão comparada a produção em uma linha de produção. 

Um artesão nesse exemplo, simboliza um sistema centralizado, onde ele possui todo o conhecimento de todas as etapas necessárias para produzir algo, realizando essas tarefas de forma sequêncial e com total controle sobre cada passo dado, não precisando se comunicar com mais ninguém para atingir seu objetivo.

Por outro lado, se pensarmos em uma linha de produção, com vários trabalhadores, cada um realizando sua função, uma parte pequena do processo, simplificando a responsabilidade de cado um deles, pode-se assim aumentar a vazão desse processo, melhorar a produtividade e diminuir a complexidade de cada etapa. 

Mas como se dá a comunicação e o controle sobre cada etapa? 

A esteira, que faz a união de cada etapa do processo faz esse papel, mas é preciso um processo muito claro e definido para garantir que a saída de uma etapa seja a entrada do próximo e assim por diante, nessa abordagem os contratos e a comunicação passam a ter papel fundamental para o sucesso do processo.

Quando olhamos para sistemas computacionais isso não é diferente, no princípio os sistemas eram centralizados, com grandes computadores realizando todas as tarefas, os dados e processos estavam no mesmo local, sob a mesma gestão e infra estrutura. Mas nesse caso é um limitante se prender a uma só célula de processamento.

Em sistemas computacionais distrbuídos, ganhamos em escala, independência, resiliência e eficiência, mas por outro lado, aumentamos drasticamente a complexidade desses sistemas devido a necessidade de gestão e sincronismo entre os diferentes atores desse paradigma.

### Características de um sistema distribuído

Compartilhamento de recursos — um sistema distribuído pode compartilhar hardware, software ou dados

Processamento simultâneo — várias máquinas podem processar dados ao mesmo tempo

Escalonamento — a capacidade de computação e processamento pode evoluir conforme necessário quando estendida para máquinas adicionais

Detecção de erros e resiliência — as falhas podem ser detectadas com mais facilidade, uma vez que cada parte do sistema faz uma etapa específica do processo

Transparência — um ponto central pode acessar os serviços se comunicar com outros pontos no sistema, abstraindo essa segregação do ponto de vista do usuário

### Exemplos de arquiteturas de sistemas distribuídos
#### Cliente Servidor
#### Pareado (HA)
#### Serviços (SOA)

## API: O que são?
API é um conjunto de rotinas e padrões de programação para acesso a um aplicativo de software ou plataforma baseado na Web. A sigla API refere-se ao termo em inglês "Application Programming Interface" que significa em tradução para o português "Interface de Programação de Aplicativos"

Uma API é criada quando uma empresa de software tem a intenção de que outros criadores de software desenvolvam produtos associados ao seu serviço. Existem vários deles que disponibilizam seus códigos e instruções para serem usados em outros sites da maneira mais conveniente para seus usuários. O Google Maps é um dos grandes exemplos na área de APIs. Por meio de seu código original, muitos outros sites e aplicações utilizam os dados do Google Maps adaptando-o da melhor forma a fim de utilizar esse serviço.

Quando uma pessoa acessa uma página de um hotel, por exemplo, é possível visualizar dentro do próprio site o mapa do Google Maps para saber a localização do estabelecimento e verificar qual o melhor caminho para chegar até lá. Esse procedimento é realizado por meio de uma API, onde os desenvolvedores do site do hotel utilizam do código do Google Maps para inseri-lo em um determinado local de sua página.

Através das APIs, os aplicativos podem se comunicar uns com os outros sem conhecimento ou intervenção dos usuários. Elas funcionam através da comunicação de diversos códigos, definindo comportamentos específicos de determinado objeto em uma interface. A API liga as diversas funções em um site de maneira que possam ser utilizadas em outras aplicações. Sistemas de pagamento online são um bom exemplo de funcionalidade das APIs que rodam de maneira automática. De modo geral, a API é composta de uma série de funções acessíveis somente por meio de programação.

Recentemente, a utilização das APIs tem se espalhado nos plugins, que complementam a funcionalidade de um determinado programa. Os desenvolvedores de um programa principal criam uma API específica e fornecem a outros criadores, que desenvolvem plugins para aumentar o potencial e as funcionalidades do programa.

Os sistemas operacionais também possuem suas APIs com as mesmas funções descritas acima. Por exemplo, o Windows possui APIs como a Telephony API, Win16 API e Win32 API. Quando um usuário executa um programa que envolva algum processo do sistema operacional, é bem provável que o Windows faça uma conexão entre o software e alguma de suas APIs.

##### Fontes e links uteis:
- https://canaltech.com.br/software/o-que-e-api/#:~:text=API%20%C3%A9%20um%20conjunto%20de,Interface%20de%20Programa%C3%A7%C3%A3o%20de%20Aplicativos%22.
- https://www.take.net/blog/tecnologia/api-conceito-e-exemplos/
- https://blog.idwall.co/o-que-e-uma-api-e-quais-seus-beneficios/?utm_term=&utm_campaign=%5BID1%5D+GoogleAds_PMax_Geral&utm_source=adwords&utm_medium=ppc&hsa_acc=4544575733&hsa_cam=16810657142&hsa_grp=&hsa_ad=&hsa_src=x&hsa_tgt=&hsa_kw=&hsa_mt=&hsa_net=adwords&hsa_ver=3&gclid=CjwKCAjw9NeXBhAMEiwAbaY4lqnJqVcubFbJmkL7bWGC506gw3UUAsu3I5jg-VPhwR80mCniNBIa5RoCRKQQAvD_BwE


### Como as APIs funcionam?
Muitas vezes, o cliente precisa ter acesso a determinados dados disponibilizados por um banco de informações, serviço ou dispositivo, por exemplo. É nesse momento que entram as APIs.

Para acessar essas informações específicas, o cliente faz uma solicitação — nomeada de requisição — à API. Assim, ela consegue fazer uma busca no servidor e devolver as respostas solicitadas em formato de dados, que são entregues em seu estado mais puro.

Ou seja, as informações não são organizadas em uma interface desenvolvida especialmente para o cliente. Não há também renderização feita por um navegador (como seria no caso de um website, por exemplo, que é mais amigável visualmente).

Existem várias APIs presentes em nosso dia a dia — uma das mais comuns, por exemplo, é a do Google Maps. Muitos sites a utilizam para ter acesso aos recursos dos mapas e, dessa forma, não precisam desenvolver seus próprios mapas, apenas realizam a integração com a interface oferecida pelo Google.

Assim como a multinacional de tecnologia, muitas empresas desenvolvem APIs para que outras companhias e usuários consigam fazer integração com seus produtos.

### Vantagens
#### Segurança
Por meio de uma API, é possível ter maior controle sobre as permissões de acesso ao software e hardware da sua empresa. Ela identifica quem são as pessoas que tentaram acessar seu sistema e a localização de onde partiu a requisição. Além disso, você decide quais informações ficarão disponíveis ao cliente no momento da integração.

#### Agilidade e compatibilidade na integração entre sistemas e aplicações
Ela também permite a realização de uma integração mais ágil de sistemas que sejam incompatíveis, sem que seja necessário alocar um time de desenvolvedores para o processo. Além de maior rapidez na troca de informações, há economia de tempo, quantidade de recursos financeiros e dados utilizados no trabalho.

#### Possibilidade de inovação em produtos e serviços
Cobrando um determinado custo, muitas empresas disponibilizam suas APIs para que outros usuários e negócios desenvolvam soluções inovadoras com elas. Tudo isso sem que o produto original seja despadronizado, já que somente a empresa proprietária poderá permitir o acesso ou qualquer tipo de alteração na API.

#### Redução de trabalho manual
Uma das infinitas possibilidades oferecidas pela API é a automatização da extração de determinados dados. Assim, diminuem a necessidade do trabalho manual no momento de exportar informações.

## Entendendo APIs
### O que é HTTP
O HTTP é um protocolo de comunicação. Através dele o cliente e o servidor conseguem se comunicar, seguindo um conjunto de regras bem definidas (por isso chamamos de protocolo). Por exemplo, se estivermos falando de uma aplicação web, o cliente é o navegador, ele envia um pedido para o servidor web usando o protocolo HTTP, com base nesse pedido, se tudo estiver correto, o servidor responde também usando o mesmo protocolo o conteúdo solicitado.

#### O que é Request
A Request ou requisição traduzindo diretamente para português, é o pedido que um cliente realiza a nosso servidor. Esse pedido contém uma série de dados que são usados para descrever exatamente o que o cliente precisa. Vamos pensar que um cliente precisa cadastrar um novo produto, ele deve passar todos os dados necessários para o cadastro acontecer de maneira correta, inclusive os dados que foram digitados pelo usuário em um formulário, no caso de uma aplicação web. No navegador toda vez que trocamos de página ou apertamos enter na barra de endereço uma nova request é feita. Independente se estamos apenas pedindo a exibição de uma página, cadastrando um novo recurso, atualizando ou excluindo.

##### Estrutura
###### Header
###### Body

#### REST
##### O que são os verbos? GET, POST e etc?
Tanto GET como POST na verdade são métodos HTTP. Eles indicam para o servidor qual a ação que o cliente deseja realizar. Quando realizamos uma requisição obrigatoriamente precisamos informar um método.

 - GET – é usado quando o cliente deseja obter recursos do servidor
 - POST – é usado quando o cliente deseja enviar dados para processamento ao servidor, como os dados de um formulário, por exemplo.
 - PUT –
 - DELETE –

Existem outros métodos HTTP. Os dois métodos citados acima são os mais usados, principalmente em aplicações web. Quando o usuário digita um endereço e aperta enter na barra de endereço do navegador, ele realiza uma requisição do tipo GET. Já quando preenchemos um formulário e clicamos em enviar geralmente o método usado é o POST.

#### O que é Response
Vimos que o cliente envia uma Request (requisição) ao servidor. Essa requisição possui todas as informações acerca do que o cliente espera receber de volta. O servidor web ao receber essas informações precisa enviar uma resposta ao cliente, nesse ponto entra a Response. A Response (resposta) nada mais é do que a resposta que o servidor envia ao cliente. Essa resposta pode conter os dados que realmente o cliente esperava receber ou uma resposta informando que alguma coisa deu errado.

#### O que é 200, 404, 301 e outros números? Esses são os HTTP Status Code?
Esses números são os chamados códigos HTTP. Quando o cliente faz uma requisição ele espera uma resposta. O servidor pode realmente responder o que o cliente esperava ou devolver outra informação, justamente nesse ponto entram os códigos HTTP. O servidor utiliza um código desse na resposta para indicar o que aconteceu.

Os códigos estão entre 100 e 500, sendo que cada centena indica uma categoria:
| Grupos de Código | Descrição |
| :-: | :- |
| 1xx |  Informativos | 
| 2xx |  Indicativos de sucesso | 
| 3xx |  Redirecionamentos | 
| 4xx |  Erros do cliente na hora de fazer a solicitação | 
| 5xx |  Erros no lado do servidor | 

Dentro de cada centena temos os códigos específicos, por exemplo:

- 200 - Tudo ocorreu corretamente
- 301 – Indica redirecionamento permanente
- 401 – Não autorizado
- 404 – O recurso solicitado não foi encontrado no servidor

Existem vários sites que especificam todos os códigos HTTP. Esse usa cachorrinhos como exemplo , mas se você gosta mais dos gatinhos também existe.

O HTTP é o protocolo que define as regras para a comunicação entre o cliente o servidor. No fluxo básico o cliente realiza uma requisição para o servidor, nessa requisição é enviada além de várias outras informações um método que indica a ação que ele deseja. O servidor devolve uma resposta, nessa resposta, além de outras informações, existe um código que indica ao cliente o que aconteceu. Caso você queira se aprofundar no assunto também abordamos no blog sobre o protocolo HTTP/2, que é a evolução do HTTP.

##### Fontes e links uteis:
- https://www.w3.org/Protocols/rfc2616/rfc2616.html
- https://pt.wikipedia.org/wiki/Hypertext_Transfer_Protocol
- https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
- https://dev.to/_staticvoid/deixando-sua-api-rest-mais-expressiva-com-status-codes-http-1-entendendo-os-codigos-4eik
- https://dev.to/_staticvoid/deixando-sua-api-rest-mais-expressiva-com-status-codes-http-2-os-esquecidos-3eee
- https://dev.to/_staticvoid/status-http-fantasticos-e-onde-habitam-3-conclusao-7bg

#### Lista com os principais códigos de retorno
| Código | Description |
|:-:|:-|
| 100  | Continue |
| 101  | Switching Protocols |
| 200  | OK |
| 201  | Created |
| 202  | Accepted |
| 203  | Non-Authoritative Information |
| 204  | No Content |
| 205  | Reset Content |
| 206  | Partial Content |
| 300  | Multiple Choices |
| 301  | Moved Permanently |
| 302  | Found |
| 303  | See Other |
| 304  | Not Modified |
| 305  | Use Proxy |
| 307  | Temporary Redirect |
| 400  | Bad Request |
| 401  | Unauthorized |
| 402  | Payment Required |
| 403  | Forbidden |
| 404  | Not Found |
| 405  | Method Not Allowed |
| 406  | Not Acceptable |
| 407  | Proxy Authentication Required |
| 408  | Request Time-out |
| 409  | Conflict |
| 410  | Gone |
| 411  | Length Required |
| 412  | Precondition Failed |
| 413  | Request Entity Too Large |
| 414  | Request-URI Too Large |
| 415  | Unsupported Media Type |
| 416  | Requested range not satisfiable |
| 417  | Expectation Failed |
| 500  | Internal Server Error |
| 501  | Not Implemented |
| 502  | Bad Gateway |
| 503  | Service Unavailable |
| 504  | Gateway Time-out |
| 505  | HTTP Version not supported |

##### Fontes e links uteis:
- https://www.w3.org/Protocols/rfc2616/rfc2616-sec6.html
- https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1

### Fontes e links uteis:
- https://www.treinaweb.com.br/blog/o-que-e-http-request-get-post-response-200-404

## Quais as vantagens das APIs -> Orientação  serviços

## Qual a relação entre as APIs e os microserviços?

## Autenticações
### O que é um token
### Criptografias
#### Com chaves simétrica
#### Com chaves assimétrica (publica e privada)
### JWT
- https://www.rfc-editor.org/rfc/rfc7519

## Mitigação de riscos

## Modelos de autenticação e de segurança

## Swagger

## Outras ferramentas de desenvolvimento de APIs