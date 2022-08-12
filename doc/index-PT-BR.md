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

- Compartilhamento de recursos — um sistema distribuído pode compartilhar hardware, software ou dados

- Processamento simultâneo — várias máquinas podem processar dados ao mesmo tempo

- Escalonamento — a capacidade de computação e processamento pode evoluir conforme necessário quando estendida para máquinas adicionais

- Detecção de erros e resiliência — as falhas podem ser detectadas com mais facilidade, uma vez que cada parte do sistema faz uma etapa específica do processo

- Transparência — um ponto central pode acessar os serviços se comunicar com outros pontos no sistema, abstraindo essa segregação do ponto de vista do usuário

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

Veja a especificação completa da [RFC HTTP]( https://www.rfc-editor.org/rfc/rfc9110.html) para maiores detalhes

#### O que é Request
A Request ou requisição traduzindo diretamente para português, é o pedido que um cliente realiza a nosso servidor. Esse pedido contém uma série de dados que são usados para descrever exatamente o que o cliente precisa. Vamos pensar que um cliente precisa cadastrar um novo produto, ele deve passar todos os dados necessários para o cadastro acontecer de maneira correta, inclusive os dados que foram digitados pelo usuário em um formulário, no caso de uma aplicação web. No navegador toda vez que trocamos de página ou apertamos enter na barra de endereço uma nova request é feita. Independente se estamos apenas pedindo a exibição de uma página, cadastrando um novo recurso, atualizando ou excluindo.

##### Estrutura
###### Header
###### Body

##### Mas o que é  [Json](https://jsonapi.org/)
JSON é basicamente um formato leve de troca de informações/dados entre sistemas. Mas JSON significa JavaScript Object Notation, ou seja, só posso usar com JavaScript correto? Na verdade não e alguns ainda caem nesta armadilha.

O JSON além de ser um formato leve para troca de dados é também muito simples de ler. Mas quando dizemos que algo é simples, é interessante compará-lo com algo mais complexo para entendermos tal simplicidade não é? Neste caso podemos comparar o JSON com o formato XML.

Vamos visualizar esta diferença?

**XML**
``` XML
<note>
<to>Tove</to>
<from>Jani</from>
<heading>Reminder</heading>
<body>Don't forget me this weekend!</body>
</note>
```

**JSON**
``` JSON
{
   "id":1,
   "nome":"Alexandre Gama",
   "endereco":"R. Qualquer"
}
```

Bom, é notável a diferença. Visualmente o segundo trecho (em JSON) é mais fácil de ler. Mas só existe essa diferença entre os dois? Na verdade não. Podemos listar algumas outras 
vantagens

###### Quais as principais características desse formato?
Os arquivos no formato .json contêm algumas características específicas que tornam essa especificação mais atraente para a utilização em aplicações que consomem dados de outros sistemas. Confira as principais, a seguir.

###### Linguagem independente
A simplicidade com que os dados são estruturados no formato JSON permite que ele seja utilizado em qualquer tipo de linguagem de programação. Além disso, ele pode ser manipulado em diferentes plataformas, como Windows, macOS, Linux, e em vários tipos de sistemas, como em aplicações web e aplicativos móveis.

###### Formatação do arquivo
Além da terminação .json em todos os arquivos que utilizam esse formato, os dados armazenados devem seguir uma notação específica, ou seja, precisam ser organizados com os seguintes elementos básicos:

- chaves { } para delimitar os objetos e obrigatórias para iniciar e encerrar o conteúdo;
- colchetes [ ] para indicar um array;
- dois pontos : para separar a chave e seu valor correspondente;
- vírgula , para indicar a separação entre os elementos.

Veja, a seguir, alguns exemplos de como os dados devem ser relacionados em um arquivo .json.

**String**
``` JSON 
{ "estado": "São Paulo"}
``` 

**Array**
``` JSON 
{
    "estados": ["São Paulo", "Minas Gerais", "Rio de Janeiro"]
}
``` 

**Objeto**
``` JSON 
{ "estado": {
       "estado": "São Paulo",
       "sigla": "SP"
  }
}
``` 
Lista de objetos
Confira como fazer a notação para indicar uma lista de objetos:

{   "estados":[
    {"estado": "São Paulo", "sigla": "SP"},
    {"estado": "Minas Gerais", "sigla": "MG"},
    {"estado": "Rio de Janeiro", "sigla": "RJ"}
    ]
}

###### Quais as diferenças entre .json e .xml?
Outro formato utilizado para a troca de dados entre aplicações é o XML — eXtensible Markup Language. Apesar de também ser um arquivo de texto, existem algumas diferenças entre os dois modelos. Confira as principais.

###### Notação
A primeira diferença entre os dois modelos é a forma de fazer a notação dos dados. Conforme mencionamos, o JSON utiliza uma notação simples, enquanto o XML utiliza uma estrutura de tags personalizadas para representar os objetos. Além disso, elas devem conter o par, ou seja, a tag de abertura e a de fechamento.

Outra característica da notação XML é que o seu conteúdo não precisa ser delimitado com aspas, como acontece com os textos no formato JSON. Nele, o que indica o início e o fim das informações são as tags de abertura e fechamento. Confira o exemplo, a seguir.

<?xml version="1.0" encoding="UTF-8" ?>
<estados>
    <estado>
        <nomeEstado>São Paulo</nomeEstado>
        <sigla>SP</sigla>
    </estado>
    <estado>
        <nomeEstado>Minas Gerais</nomeEstado>
        <sigla>MG</sigla>
    </estado>
    <estado>
        <nomeEstado>Rio de Janeiro</nomeEstado>
        <sigla>RJ</sigla>
    </estado>
</estados>

###### Tipos de dados
O formato XML suporta diferentes tipos de dados, entre eles: imagens e gráficos, o que não é possível transmitir no formato JSON, pois ele só oferece suporte a números e textos. Em contrapartida, o XML não oferece suporte a arrays.

###### Codificação
A codificação representa as formas de conversão para o formato binário suportadas pelo modelo. O JSON utiliza o formato UTF-8, enquanto o XML oferece essa e outras opções. É importante dizer que o UTF-8 é o formato mais utilizado em sites na internet, como o WordPress e muitos outros.

###### Facilidade de leitura e comentários
Os arquivos JSON são fáceis de entender, pois sua estrutura e notação são bem simples. Já o XML é mais estruturado e, portanto, com a interpretação mais complexa. Outra diferença é com relação aos comentários no arquivo, que são permitidos apenas no modelo XML.

###### Por que o .json tem sido cada vez mais utilizado?
A simplicidade do formato JSON é uma das principais razões pelas quais ele é bastante utilizado. Isso porque as requisições AJAX, que permitem a atualização da página sem a necessidade de recarregá-la completamente, precisam ser executadas com muita rapidez para que essas atualizações sejam transparentes para o usuário.

Por ser leve e compacto, o formato JSON atende a essa necessidade. Portanto, os dados podem ser trafegados de forma rápida e interpretados com facilidade pela aplicação.

Vale dizer que o formato XML também pode ser utilizado em requisições AJAX. Entretanto, é um arquivo maior, por conter mais informações em razão do grande número de tags de abertura e fechamento, o que torna a sua transferência e processamento mais lentos que o modelo JSON.

Outra razão importante para utilizar esse formato é para resolver o problema de domínio cruzado, que é a impossibilidade de executar requisições AJAX em domínios que não estejam hospedados no mesmo servidor. Existe um recurso chamado JSONP que elimina essa situação com facilidade e permitir a recuperação de informações com essa característica.

###### Onde posso utilizar .json?
O arquivo .json pode ser utilizado em diferentes finalidades. Uma delas é para serializar e transmitir dados estruturados. Ele também é indicado para a utilização em aplicativos móveis, em que é preciso requisitar dados em um servidor e utilizá-los rapidamente na aplicação.

Conforme mencionamos, o JSON é muito utilizado em requisições AJAX para aplicações web e para resolver o problema de domínio cruzado. Além disso, ele também é utilizado como arquivo de configuração para armazenar dados que são verificados em tempo de utilização da aplicação.

###### Quais os benefícios do formato JSON?
Existem diversas vantagens em optar pela utilização do formato JSON para diversos tipos de aplicações. Confira as principais delas.

###### Leitura mais simples
O formato JSON é fácil de utilizar, pois sua notação permite, inclusive, o entendimento visual da organização dos dados. Isso significa que se alguém abrir um arquivo .json, provavelmente, conseguirá compreender as suas informações. A mesma facilidade é com relação ao processamento desse arquivo, especialmente, por ser em formato texto.

###### Mais agilidade na execução e transporte de dados
Armazenar os dados em formato texto, aliás, permite que o arquivo .json ocupe pouco espaço em memória. Essa característica oferece ótima performance, pois como ele é pequeno, ocupa poucos bytes, o que oferece mais agilidade para a transferência e carregamento durante o processamento.

###### Arquivos mais leves
A forma com que os dados são estruturados no modelo JSON é extremamente compacta. Isso permite armazenar muitas informações com menos delimitadores que o modelo XML. Conforme mencionamos, os arquivos gerados são leves e mais rápidos para transmitir e fazer o processamento pela aplicação.

###### Parsing mais fácil
Como os dados armazenados em um arquivo JSON são em formato de texto, é preciso realizar a interpretação de seu conteúdo para que ele seja consumido pela aplicação. Isso pode ser feito facilmente por diferentes tipos de linguagens, como JavaScript, jQuery e muitas outras.

**Resumindo:**
- Leitura mais simples
- Analisador(parsing) mais fácil
- JSON suporta objetos! Sim, ele é tipado!
- Velocidade maior na execução e transporte de dados
- Arquivo com tamanho reduzido
- Quem utiliza? Google, Facebook, Yahoo!, Twitter...




#### [REST](https://standards.rest/)
##### O que são os [verbos](https://www.rfc-editor.org/rfc/rfc9110.html#name-methods)? GET, POST e etc?
Tanto GET como POST na verdade são métodos HTTP. Eles indicam para o servidor qual a ação que o cliente deseja realizar. Quando realizamos uma requisição obrigatoriamente precisamos informar um método.

 - [GET](https://www.rfc-editor.org/rfc/rfc9110.html#name-get) – é usado quando o cliente deseja obter recursos do servidor
 - [POST](https://www.rfc-editor.org/rfc/rfc9110.html#name-post) – é usado quando o cliente deseja enviar dados para processamento ao servidor, como os dados de um formulário, por exemplo.
 - [PUT](https://www.rfc-editor.org/rfc/rfc9110.html#name-put) – é usado quando o cliente deseja atualizar um dado de um recurso que está no servidor
 - [DELETE](https://www.rfc-editor.org/rfc/rfc9110.html#name-delete) – é usado quando uo cliente deseja apagar um dado dew um recurso que está no servidor

Existem outros métodos HTTP. Os dois métodos citados acima são os mais usados, principalmente em aplicações web. Quando o usuário digita um endereço e aperta enter na barra de endereço do navegador, ele realiza uma requisição do tipo GET. Já quando preenchemos um formulário e clicamos em enviar geralmente o método usado é o POST.

#### O que é [Response](https://datatracker.ietf.org/doc/html/rfc8246)
Vimos que o cliente envia uma Request (requisição) ao servidor. Essa requisição possui todas as informações acerca do que o cliente espera receber de volta. O servidor web ao receber essas informações precisa enviar uma resposta ao cliente, nesse ponto entra a Response. A Response (resposta) nada mais é do que a resposta que o servidor envia ao cliente. Essa resposta pode conter os dados que realmente o cliente esperava receber ou uma resposta informando que alguma coisa deu errado.

#### O que é 200, 404, 301 e outros números? Esses são os [HTTP Status Code](https://datatracker.ietf.org/doc/html/rfc6585)?
Esses números são os chamados códigos HTTP. Quando o cliente faz uma requisição ele espera uma resposta. O servidor pode realmente responder o que o cliente esperava ou devolver outra informação, justamente nesse ponto entram os códigos HTTP. O servidor utiliza um código desse na resposta para indicar o que aconteceu.

Os códigos estão entre 100 e 500, sendo que cada centena indica uma categoria:
| Grupos de Código | Descrição |
| :-: | :- |
| **1xx** |  Informativos | 
| **2xx** |  Indicativos de sucesso | 
| **3xx** |  Redirecionamentos | 
| **4xx** |  Erros do cliente na hora de fazer a solicitação | 
| **5xx** |  Erros no lado do servidor | 

Dentro de cada centena temos os códigos específicos, por exemplo:

- **200** – Tudo ocorreu corretamente
- **301** – Indica redirecionamento permanente
- **401** – Não autorizado
- **404** – O recurso solicitado não foi encontrado no servidor

Existem vários sites que especificam todos os códigos HTTP. Esse usa cachorrinhos como exemplo , mas se você gosta mais dos gatinhos também existe.

O HTTP é o protocolo que define as regras para a comunicação entre o cliente o servidor. No fluxo básico o cliente realiza uma requisição para o servidor, nessa requisição é enviada além de várias outras informações um método que indica a ação que ele deseja. O servidor devolve uma resposta, nessa resposta, além de outras informações, existe um código que indica ao cliente o que aconteceu. Caso você queira se aprofundar no assunto também abordamos no blog sobre o protocolo HTTP/2, que é a evolução do HTTP.

##### Fontes e links uteis:
- https://www.w3.org/Protocols/rfc2616/rfc2616.html
- https://datatracker.ietf.org/doc/html/rfc6585
- https://pt.wikipedia.org/wiki/Hypertext_Transfer_Protocol
- https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
- https://datatracker.ietf.org/doc/html/rfc8246
- https://dev.to/_staticvoid/deixando-sua-api-rest-mais-expressiva-com-status-codes-http-1-entendendo-os-codigos-4eik
- https://dev.to/_staticvoid/deixando-sua-api-rest-mais-expressiva-com-status-codes-http-2-os-esquecidos-3eee
- https://dev.to/_staticvoid/status-http-fantasticos-e-onde-habitam-3-conclusao-7bg

#### Lista com os principais códigos de retorno
| Código | Description |
|:-:|:-|
| **100**  | Continue |
| **101**  | Switching Protocols |
| **200**  | OK |
| **201**  | Created |
| **202**  | Accepted |
| **203**  | Non-Authoritative Information |
| **204**  | No Content |
| **205**  | Reset Content |
| **206**  | Partial Content |
| **300**  | Multiple Choices |
| **301**  | Moved Permanently |
| **302**  | Found |
| **303**  | See Other |
| **304**  | Not Modified |
| **305**  | Use Proxy |
| **307**  | Temporary Redirect |
| **400**  | Bad Request |
| **401**  | Unauthorized |
| **402**  | Payment Required |
| **403**  | Forbidden |
| **404**  | Not Found |
| **405**  | Method Not Allowed |
| **406**  | Not Acceptable |
| **407**  | Proxy Authentication Required |
| **408**  | Request Time-out |
| **409**  | Conflict |
| **410**  | Gone |
| **411**  | Length Required |
| **412**  | Precondition Failed |
| **413**  | Request Entity Too Large |
| **414**  | Request-URI Too Large |
| **415**  | Unsupported Media Type |
| **416**  | Requested range not satisfiable |
| **417**  | Expectation Failed |
| **500**  | Internal Server Error |
| **501**  | Not Implemented |
| **502**  | Bad Gateway |
| **503**  | Service Unavailable |
| **504**  | Gateway Time-out |
| **505**  | HTTP Version not supported |

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