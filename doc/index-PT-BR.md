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

### Conceitos importantes ao se falar de sistemas computacionais distribuídos
- Cliente Servidor: É um tipo de arquitetura muito comum, onde existe um servidor provendo serviços para vários clientes
- Modelos de alta disponibilidade (HA): São desenhos de arquitetura para entregar um alto nível de resiliência, para que mesmo em situações de falha o serviço continue sendo provido ou que seja capaz de distribuir sua capacidade de processamento em mais do que um único ponto

### SOA - Orientação a serviços: 
Service Oriented Architectures (SOA) é, em tradução livre, Arquitetura Orientada a Serviços. Esse conceito de arquitetura busca disponibilizar as funcionalidades de um sistema como um serviço.

Desta forma, essas funcionalidades podem ser compartilhadas e reutilizadas entre aplicações. Seu principal objetivo é ser mais flexível em atender às necessidades do mercado.

Em 1996, os pesquisadores do Gartner Roy Schulte e Yefim Natis mencionaram pela primeira vez o conceito do SOA em um artigo. Os usuários dessa abordagem ganham em flexibilidade, agilidade e redução de custos na reutilização de serviços.

Um dos componentes mais importantes do SOA é o Enterprise Service Bus (ESB), um barramento de serviços corporativos.

Esse barramento disponibiliza com maior facilidade os serviços do sistema para os usuários e outras aplicações, acelerando processos de integração.

#### Principais vantagens do SOA
O alinhamento com as regras de negócio é um dos maiores benefícios desse tipo de arquitetura. Podemos elencar outras vantagens como:

- A diminuição do tempo de desenvolvimento;
- O baixo acoplamento entre as partes do sistema facilita a manutenção;
- O isolamento da estrutura de um serviço traz flexibilidade durante mudanças;
- Facilidade de agregar novas tecnologias a plataformas;
- A possibilidade de reutilização de componentes.

#### Funções da SOA
Em resumo, podemos dizer que uma arquitetura orientada a serviço é constituída de três funções:
- Provedor de serviços: Um provedor de serviços cria serviços web e os oferece para um registro de serviços. Ele é responsável pelos termos de uso desse serviço.
- Broker ou registro de serviços: Um broker de serviços ou registro de serviços é responsável por oferecer informações solicitadas sobre o serviço. O broker pode ser público ou privado.
- Solicitante ou cliente de serviços: Um solicitante de serviços encontra um serviço no broker ou no registro de serviços. Então, conecta-se ao provedor de serviços para recebê-lo.

#### Serviços SOA
Um serviço é uma atividade ou conjunto de atividades de natureza intangível que é o relacionamento entre um provedor e um consumidor. A interação acontece em respostas síncronas ou assíncronas (GRONROOS, 2006). Na prestação de serviços, existe um fornecedor que fornece algum tipo de serviço e o consumidor que consome o serviço fornecido. Abaixo se vê a figura de um ambiente de prestação de serviço.

Um exemplo de serviço é a energia elétrica que chega à sua casa. Há a geração, depois tem transmissão e por último tem distribuição. Para o usuário não importa todas essas etapas, o que importa são os benefícios que geram esse serviço. A seguir estão os princípios de design de serviços listador por Thomas ERL(2009):

- Serviços são reutilizáveis.
- Serviços compartilham um contrato formal.
- Serviços possuem um baixo acoplamento.
- Serviços abstraem a lógica.
- Serviços são capazes de se comporem.
- Serviços são autônomos.
- Serviços evitam alocação de recursos por longos períodos.
- Serviços são capazes de serem descobertos.

Serviços expõem seus membros através de um contrato de serviço. No contrato são definidas quais operações serão disponibilizadas e nele está presente a interface técnica. Essas interfaces são as ligações entre um serviço e as aplicações que irão consumi-lo, expondo somente as operações desejadas.

#### Arquitetura de Software SOA
A arquitetura de software consiste em documentar o que um sistema precisa ter em termos de componentes computacionais e os relacionamentos entre eles, os padrões que serão usados e suas restrições (SHAW e GARLAN, 1996).

Para construir um software, precisamos ter uma fundação sólida. A arquitetura de software estuda como deve ser feito o software, definindo todos os componentes que devem ser utilizados, estudando os requisitos funcionais e não funcionais do sistema.

A arquitetura de software procura construir uma relação entre os requisitos de negócio e os requisitos técnicos, entendo o funcionamento e então encontrando maneiras de implementar as funcionalidades do sistema. Uma arquitetura bem planejada reduz os riscos de negócio. Alguns benefícios são listados por MARZULLO (2009):

- Facilidade na gerência da complexidade.
- Padronização da linguagem e da comunicação entre desenvolvedores, clientes e gerentes.
- Possibilidades de reuso e consequente evolução do sistema.
- Fator determinante de uma boa análise (como consistência, atributos de qualidade, atendimento a estilos arquiteturais).

No desenvolvimento de software é muito importe o papel do arquiteto, podemos dividir em três papeis:

- **Arquiteto de Negócio**: Deve conhecer muito bem o negócio da empresa.
- **Arquiteto de Soluções**: Deve conhecer o negócio da empresa e conhecer soluções técnicas.
- **Arquiteto Técnico**: É o profissional que tem o conhecimento técnico, como Arquiteto de Software, Arquiteto de Rede, Arquiteto de Banco de Dados , etc.

Eis algumas funções do arquiteto de software:
- Priorizar casos de uso.
- Análise arquitetural.
- Construir prova de conceito arquitetural.
- Estruturar o modelo de implementação.
- Incorporar elementos de design.
- Descrever a distribuição.
- Avaliar viabilidade de prova de conceito.
- Identificar mecanismos de design.
- Desenvolver guia de programação.
- Identificar elementos de design.
- Descrever a arquitetura em tempo de execução.
- Desenvolver guia de design.

#### História
Algumas pessoas dizem que o termo arquitetura orientada a serviços (SOA) foi criado por um analista do Grupo Gartner chamado Alenxander Pasik, em 1994. Outras dizem que os primeiros indícios e discussões foram por volta do ano 2000, de estudos da Microsoft e IBM sobre a tecnologia de Web Service. O que pode ser afirmado é que, atualmente, é visto como uma técnica que cobri melhor as necessidades do mercado. (MARZULLO, 2009).

É uma arquitetura que promove a integração do negócio com a tecnologia da informação com componentes de serviços, esse componente é o principal item dessa arquitetura. Os resultados que SOA traz são: agilidade para atender as novas demandas, flexibilidade nas mudanças, redução de custo e reuso de serviços. (SILVA, 2012).

O foco em SOA é a construção e disponibilização de serviços de negócio, evitar replicação de dados, reuso e facilidade de manutenção de sistemas, integração entre os sistemas, visão e controle do processo de negócio, agilidade nas mudanças.

Podemos dizer que SOA é assunto novo, e algumas pessoas confundem o que realmente é essa arquitetura. Abaixo se vê algumas informações erradas sobre ela:
- Não é uma tecnologia.
- Não é um produto.
- Não é um Web Service.
- Não é um projeto de TI.
- Não é um software.
- Não é um “framework”.
- Não é uma metodologia.
- Não é uma solução de negócio.
- Não é um middleware.
- Não pode ser comprada.
- Não é um serviço.
- Não é uma ferramenta de produtividade.

SOA é um conceito de arquitetura que traz maiores prioridades de inovação, aumentando a capacidade de colaboração entres aplicativos e inovando os modelos de negócio e processos. Dizer que uma empresa precisa inovar seu negócio, é a mesma coisa em dizer que é preciso mudar, não existe uma inovação sem mudança, é essa arquitetura facilita as mudanças.

#### Web Service
Web Service é disponibilização de um serviço pela Internet que pode ser acessado em qualquer lugar. Os clientes enviam requisições com informações bem definidas e recebem respostas que podem ser síncronas ou assíncronas (MARZULLO, 2009).

A disponibilização de um serviço é através de um contrato, que é uma interface que disponibiliza as suas funcionalidades, com uma infraestrutura leve e desacoplada de plataforma que facilita a integração em diferentes tecnologias.

Web Service tem que ser visto por um conjunto de tecnologias, que são citadas por MARZULLO (2009), como por exemplo:
- Protocolo HTTP: Transmissão de dados pela Internet.
- Json/XML: Formatos para troca de informações, os dados são separados por tags.
- SOAP: Fornece uma estrutura padrão de empacotamento para transporte de documentos XML pela internet.
- WSDL: Tecnologia XML que descreve de forma padronizada a interface de um Web Service.
- UDDI: Descreve um registro mundial de serviços e serve com integração, propaganda e descoberta de serviços.


##### Links uteis:
- https://www.ibm.com/br-pt/cloud/learn/soa
- https://www.opus-software.com.br/o-que-e-soa-e-quais-os-beneficios/
- https://www.redhat.com/pt-br/topics/cloud-native-apps/what-is-service-oriented-architecture
- https://www.treinaweb.com.br/blog/voce-sabe-o-que-e-arquitetura-orientada-a-servicos-soa
- https://www.devmedia.com.br/vantagens-e-desvantagens-de-soa/27437

## APIs: O que são?
API é um conjunto de rotinas e padrões de programação para acesso a um aplicativo de software ou plataforma baseado na Web. A sigla API refere-se ao termo em inglês "Application Programming Interface" que significa em tradução para o português "Interface de Programação de Aplicativos"

Uma API é criada quando uma empresa de software tem a intenção de que outros criadores de software desenvolvam produtos associados ao seu serviço. Existem vários deles que disponibilizam seus códigos e instruções para serem usados em outros sites da maneira mais conveniente para seus usuários. O Google Maps é um dos grandes exemplos na área de APIs. Por meio de seu código original, muitos outros sites e aplicações utilizam os dados do Google Maps adaptando-o da melhor forma a fim de utilizar esse serviço.

Quando uma pessoa acessa uma página de um hotel, por exemplo, é possível visualizar dentro do próprio site o mapa do Google Maps para saber a localização do estabelecimento e verificar qual o melhor caminho para chegar até lá. Esse procedimento é realizado por meio de uma API, onde os desenvolvedores do site do hotel utilizam do código do Google Maps para inseri-lo em um determinado local de sua página.

Através das APIs, os aplicativos podem se comunicar uns com os outros sem conhecimento ou intervenção dos usuários. Elas funcionam através da comunicação de diversos códigos, definindo comportamentos específicos de determinado objeto em uma interface. A API liga as diversas funções em um site de maneira que possam ser utilizadas em outras aplicações. Sistemas de pagamento online são um bom exemplo de funcionalidade das APIs que rodam de maneira automática. De modo geral, a API é composta de uma série de funções acessíveis somente por meio de programação.

Recentemente, a utilização das APIs tem se espalhado nos plugins, que complementam a funcionalidade de um determinado programa. Os desenvolvedores de um programa principal criam uma API específica e fornecem a outros criadores, que desenvolvem plugins para aumentar o potencial e as funcionalidades do programa.

Os sistemas operacionais também possuem suas APIs com as mesmas funções descritas acima. Por exemplo, o Windows possui APIs como a Telephony API, Win16 API e Win32 API. Quando um usuário executa um programa que envolva algum processo do sistema operacional, é bem provável que o Windows faça uma conexão entre o software e alguma de suas APIs.

##### Fontes e links uteis:
- https://canaltech.com.br/software/o-que-e-api
- https://www.take.net/blog/tecnologia/api-conceito-e-exemplos/
- https://blog.idwall.co/o-que-e-uma-api-e-quais-seus-beneficios


## Como as APIs funcionam?
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
### O que é [HTTP]( https://www.rfc-editor.org/rfc/rfc9110.html)?
O HTTP é um protocolo de comunicação. Através dele o cliente e o servidor conseguem se comunicar, seguindo um conjunto de regras bem definidas (por isso chamamos de protocolo). Por exemplo, se estivermos falando de uma aplicação web, o cliente é o navegador, ele envia um pedido para o servidor web usando o protocolo HTTP, com base nesse pedido, se tudo estiver correto, o servidor responde também usando o mesmo protocolo o conteúdo solicitado.

Veja a especificação completa da [RFC HTTP]( https://www.rfc-editor.org/rfc/rfc9110.html) para maiores detalhes

### O que é [Request](https://www.rfc-editor.org/rfc/rfc2616.html#section-5)?
A Request ou requisição traduzindo diretamente para português, é o pedido que um cliente realiza a nosso servidor. Esse pedido contém uma série de dados que são usados para descrever exatamente o que o cliente precisa. Vamos pensar que um cliente precisa cadastrar um novo produto, ele deve passar todos os dados necessários para o cadastro acontecer de maneira correta, inclusive os dados que foram digitados pelo usuário em um formulário, no caso de uma aplicação web. No navegador toda vez que trocamos de página ou apertamos enter na barra de endereço uma nova request é feita. Independente se estamos apenas pedindo a exibição de uma página, cadastrando um novo recurso, atualizando ou excluindo.

### O que é [Response](https://datatracker.ietf.org/doc/html/rfc8246)?
Vimos que o cliente envia uma Request (requisição) ao servidor. Essa requisição possui todas as informações acerca do que o cliente espera receber de volta. O servidor web ao receber essas informações precisa enviar uma resposta ao cliente, nesse ponto entra a Response. A Response (resposta) nada mais é do que a resposta que o servidor envia ao cliente. Essa resposta pode conter os dados que realmente o cliente esperava receber ou uma resposta informando que alguma coisa deu errado.

### O que é 200, 404, 301 e outros números? Esses são os [HTTP Status Code](https://datatracker.ietf.org/doc/html/rfc6585)?
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

#### Fontes e links uteis:
- https://www.w3.org/Protocols/rfc2616/rfc2616.html
- https://datatracker.ietf.org/doc/html/rfc6585
- https://pt.wikipedia.org/wiki/Hypertext_Transfer_Protocol
- https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
- https://datatracker.ietf.org/doc/html/rfc8246
- https://dev.to/_staticvoid/deixando-sua-api-rest-mais-expressiva-com-status-codes-http-1-entendendo-os-codigos-4eik
- https://dev.to/_staticvoid/deixando-sua-api-rest-mais-expressiva-com-status-codes-http-2-os-esquecidos-3eee
- https://dev.to/_staticvoid/status-http-fantasticos-e-onde-habitam-3-conclusao-7bg

### Lista com os principais códigos de retorno
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

#### Fontes e links uteis:
- https://www.w3.org/Protocols/rfc2616/rfc2616-sec6.html
- https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1

### Estrutura
#### [Header](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Headers)
É um conjunto de informações que cada requisição HTTP contém e podem ser lidas antes mesmo do conteúdo da mensagem ser processado, esse cabeçalho é uma coleção de dados que chamamos de dicionários, ou seja, uma lista de chave e valor.

Na [RFC que define o modelo HTTP](https://www.rfc-editor.org/rfc/rfc7231.txt), esses campos são descritos e tem grande importância para a integração via APIs ou até mesmo para um browser ser capaz de abrir uma página web.

#### Body
Chamamos de Body o corpo de dados de uma transação HTTP, é a mensagem própriamente dita e ela pode variar totalmente no formato de conteúdo, de acordo com o especificado em alguns campos do Header.

Os campos [Content-Type](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Headers/Content-Type), [Content-Length](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Headers/Content-Length) e [Content-Encoding](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Headers/Content-Encoding) se referem diretamente o formato e tamanho do conteúdo do Body.

#### Fontes e links uteis:
- https://www.w3.org/Protocols/rfc2616/rfc2616-sec5.html
- https://datatracker.ietf.org/doc/html/rfc7231#section-3.1.1.5
- https://datatracker.ietf.org/doc/html/rfc7233#section-4.1
- https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Headers/Content-Type
- https://medium.com/clebertech/como-funciona-uma-requisi%C3%A7%C3%A3o-http-cf76f66fe36e
- https://www.tutorialspoint.com/http/http_requests.htm

## Mas o que é [Json](https://jsonapi.org/)?
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

### Quais as principais características desse formato?
Os arquivos no formato .json contêm algumas características específicas que tornam essa especificação mais atraente para a utilização em aplicações que consomem dados de outros sistemas. Confira as principais, a seguir.

### Linguagem independente
A simplicidade com que os dados são estruturados no formato JSON permite que ele seja utilizado em qualquer tipo de linguagem de programação. Além disso, ele pode ser manipulado em diferentes plataformas, como Windows, macOS, Linux, e em vários tipos de sistemas, como em aplicações web e aplicativos móveis.

### Formatação do arquivo
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
**Lista de objetos**
Confira como fazer a notação para indicar uma lista de objetos:

``` JSON 
{   "estados":[
    {"estado": "São Paulo", "sigla": "SP"},
    {"estado": "Minas Gerais", "sigla": "MG"},
    {"estado": "Rio de Janeiro", "sigla": "RJ"}
    ]
}
``` 

### Quais as diferenças entre .json e .xml?
Outro formato utilizado para a troca de dados entre aplicações é o XML — eXtensible Markup Language. Apesar de também ser um arquivo de texto, existem algumas diferenças entre os dois modelos. Confira as principais.

### Notação
A primeira diferença entre os dois modelos é a forma de fazer a notação dos dados. Conforme mencionamos, o JSON utiliza uma notação simples, enquanto o XML utiliza uma estrutura de tags personalizadas para representar os objetos. Além disso, elas devem conter o par, ou seja, a tag de abertura e a de fechamento.

Outra característica da notação XML é que o seu conteúdo não precisa ser delimitado com aspas, como acontece com os textos no formato JSON. Nele, o que indica o início e o fim das informações são as tags de abertura e fechamento. Confira o exemplo, a seguir.

``` XML
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
```

### Tipos de dados
O formato XML suporta diferentes tipos de dados, entre eles: imagens e gráficos, o que não é possível transmitir no formato JSON, pois ele só oferece suporte a números e textos. Em contrapartida, o XML não oferece suporte a arrays.

### Codificação
A codificação representa as formas de conversão para o formato binário suportadas pelo modelo. O JSON utiliza o formato UTF-8, enquanto o XML oferece essa e outras opções. É importante dizer que o UTF-8 é o formato mais utilizado em sites na internet, como o WordPress e muitos outros.

## Quais os benefícios do formato JSON?
Existem diversas vantagens em optar pela utilização do formato JSON para diversos tipos de aplicações. Confira as principais delas.

### Leitura mais simples
O formato JSON é fácil de utilizar, pois sua notação permite, inclusive, o entendimento visual da organização dos dados. Isso significa que se alguém abrir um arquivo .json, provavelmente, conseguirá compreender as suas informações. A mesma facilidade é com relação ao processamento desse arquivo, especialmente, por ser em formato texto.

### Mais agilidade na execução e transporte de dados
Armazenar os dados em formato texto, aliás, permite que o arquivo .json ocupe pouco espaço em memória. Essa característica oferece ótima performance, pois como ele é pequeno, ocupa poucos bytes, o que oferece mais agilidade para a transferência e carregamento durante o processamento.

### Arquivos mais leves
A forma com que os dados são estruturados no modelo JSON é extremamente compacta. Isso permite armazenar muitas informações com menos delimitadores que o modelo XML. Conforme mencionamos, os arquivos gerados são leves e mais rápidos para transmitir e fazer o processamento pela aplicação.

### Parsing mais fácil
Como os dados armazenados em um arquivo JSON são em formato de texto, é preciso realizar a interpretação de seu conteúdo para que ele seja consumido pela aplicação. Isso pode ser feito facilmente por diferentes tipos de linguagens, como JavaScript, jQuery e muitas outras.

**Resumindo:**
- Leitura mais simples
- Analisador(parsing) mais fácil
- JSON suporta objetos! Sim, ele é tipado!
- Velocidade maior na execução e transporte de dados
- Arquivo com tamanho reduzido
- Quem utiliza? Google, Facebook, Yahoo!, Twitter...

### Fontes e links uteis:
- https://dicasdeprogramacao.com.br/o-que-e-json/


## [REST](https://standards.rest/)
O protocolo HTTP define um conjunto de métodos de requisição responsáveis por indicar a ação a ser executada para um dado recurso. Embora esses métodos possam ser descritos como substantivos, eles também são comumente referenciados como HTTP Verbs (Verbos HTTP). Cada um deles implementa uma semântica diferente, mas alguns recursos são compartilhados por um grupo deles, como por exemplo, qualquer método de requisição pode ser do tipo safe, idempotent ou cacheable.

### O que são os [verbos](https://www.rfc-editor.org/rfc/rfc9110.html#name-methods)? GET, POST e etc?
Tanto GET como POST na verdade são [métodos HTTP](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Methods). Eles indicam para o servidor qual a ação que o cliente deseja realizar. Quando realizamos uma requisição obrigatoriamente precisamos informar um método.

 - **[GET](https://www.rfc-editor.org/rfc/rfc9110.html#name-get)** – é usado quando o cliente deseja obter recursos do servidor
 - **[POST](https://www.rfc-editor.org/rfc/rfc9110.html#name-post)** – é usado quando o cliente deseja enviar dados para processamento ao servidor, como os dados de um formulário, por exemplo.
 - **[PUT](https://www.rfc-editor.org/rfc/rfc9110.html#name-put)** – é usado quando o cliente deseja atualizar um dado de um recurso que está no servidor
 - **[DELETE](https://www.rfc-editor.org/rfc/rfc9110.html#name-delete)** – é usado quando uo cliente deseja apagar um dado dew um recurso que está no servidor

Existem outros métodos HTTP. Os dois métodos citados acima são os mais usados, principalmente em aplicações web. Quando o usuário digita um endereço e aperta enter na barra de endereço do navegador, ele realiza uma requisição do tipo GET. Já quando preenchemos um formulário e clicamos em enviar geralmente o método usado é o POST.

### Fontes e links uteis:
- https://standards.rest/
- https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Methods
- https://www.rfc-editor.org/rfc/rfc9110.html#name-methods
- https://www.treinaweb.com.br/blog/o-que-e-http-request-get-post-response-200-404

## Qual a relação entre as APIs e os microserviços?

## Autenticações e Segurança
### O que é um [token](https://pt.wikipedia.org/wiki/Token_(inform%C3%A1tica)) de autenticação
Chamamos de [token de autenticação](https://pt.wikipedia.org/wiki/Token_(chave_eletr%C3%B4nica)#:~:text=Token%20%C3%A9%20um%20dispositivo%20eletr%C3%B4nico,conectado%20a%20uma%20porta%20USB.) um conjunto de caracteres, chave que indentifica uma operação. Por exemplo:

Imagine uma API que tem um nível de proteção que precisa de usuário e senha (chamamos também de credênciais) para liberar acesso aos seus serviços, a cada requisição o cliente iria precisar enviar esses dados e a API validar se essas credênciais possuem acesso a esses serviços. 

Parece custoso e pouco seguro, certo? Nesses casos podemos ter um serviço responsável por validar se um usuário e senha são válidos e gerar um **token**, que pode identificar esse usuário nas próximas requisições.

Nesse caso, na autenticação por token, o usuário insere login e senha na plataforma, o que gera um token (que podemos também chamar de certificado digital) que o permite navegar pelos recursos do seu interesse, dentro de um prazo determinado, sem a necessidade de utilizar os dados do login novamente.

#### Fontes e links uteis:
- https://blog.engdb.com.br/autenticacao-por-token/
- https://www.linkedin.com/pulse/autentica%C3%A7%C3%A3o-baseada-em-token-uma-aplica%C3%A7%C3%A3o-rest-tarcisio-carvalho/?originalSubdomain=pt

### [Criptografias](https://en.wikipedia.org/wiki/Cryptography)
Através da criptografia obtemos diversas propriedades importantes como a confidencialidade (sigilo da informação), integridade (garantia que a mensagem não foi alterada), autenticidade (quem foi a autor da mensagem) e irretratabilidade ou não repúdio (capacidade de não negar a construção da mensagem). Temos ainda que a criptografia Simétrica garante a confidencialidade e a integridade, enquanto que a criptografia Assimétrica garante a confidencialidade, integridade, autenticidade e a irretratabilidade ou não repúdio.

Assim sendo, podemos classificar os algoritmos através do número de chaves (simétrico ou assimétrico). Nos algoritmos simétricos uma chave é usada tanto para criptografar quanto para descriptografar (podemos ter mais que uma se a segunda for facilmente derivada da primeira), enquanto que nos algoritmos assimétricos temos mais que uma chave e ambas são completamente independentes uma das outras.

Outra classificação para os algoritmos é em relação aos métodos de operação que podem ser dois: de substituição e de transposição. Mais uma importante classificação é em relação ao modo de processamento que pode ser: os cifradores de bloco e cifradores de fluxo. Cifradores de Bloco operam sobre 8 bits ou 16 bits e funcionam com complementos para que todos blocos tenham o mesmo tamanho. Cifradores de Fluxo é onde a cifragem ocorre bit a bit continuo. Essas classificações são importantes e nos permitem melhor organizar cada algoritmo criptográfico.

Nessa importante área de segurança da informação ainda temos duas ciências muito estudas: a Criptologia que se divide em Criptografia e que tem como foco o estudo de como tornar algo legível em ilegível e a Criptoanálise que estuda a arte de quebrar textos cifrados. Por fim, temos a Estagonologia que se divide em Esteganografia que estuda a ocultação da informação e Esteganoanálise que é a arte de revelar informações ocultas.

A criptografia através de cifras ocorre com a cifração da mensagem original através de operações de transposição e substituição de seus caracteres, resultando numa mensagem cifrada. Para decifração basta aplicar o processo inverso. Temos dois tipos de cifras, as cifras mono alfabéticas e as cifras poli alfabéticas. As cifras mono alfabéticas são compostas pela mais famosa de todas que é conhecida como Cifra de César onde basicamente cada letra do alfabeto é deslocada da sua posição um número fixo de lugares k, tal que 1<=k<=25 (número de letras que compõem o alfabeto). Originalmente a cifra anda três posições. Portanto, por exemplo, a palavra "senha" seria cifrada como "vhqkd", assim "s" andou três posições e foi para o "v", “e” andou mais três posições e foi para o “h” e assim por diante. A Cifra de César ainda é utilizada em algumas aplicações mais simples que necessitam de alguma criptografia. Por sua vez, as cifras poli alfabéticas são compostas pela cifra de Vigenère que consiste no uso de várias cifras de César em sequencia, com diferentes valores de deslocamento ditados por uma palavra-chave.

Os sistemas criptográficos são compostos por dois tipos: Simétricos e Assimétricos. Na próxima seção veremos mais sobre a criptografia Assimétrica estudando seus conceitos, funcionamento, algoritmos e como podemos aplica-los na prática utilizando a linguagem de programação Java que suporta amplamente a criptografia Assimétrica.

#### [Chaves simétricas](https://academy.bit2me.com/pt/que-es-criptografia-simetrica/)
O ciframento de uma mensagem (processo em que um conteúdo é criptografado) é baseado em 2 componentes:

- um algoritmo;
- uma chave de segurança.

##### Algoritmo
O algoritmo trabalha junto com a chave, de forma que eles tornam um conteúdo sigiloso com um conjunto único de regras.

##### A Chave (senha)
A criptografia simétrica faz uso de uma única chave, que é compartilhada entre o emissor e o destinatário de um conteúdo. Essa chave é uma cadeia própria de bits, que vai definir a forma como o algoritmo vai cifrar um conteúdo.

Como vantagem, a criptografia tem uma boa performance e a possibilidade de manter uma comunicação contínua entre várias pessoas simultaneamente. Caso a chave seja comprometida, basta efetuar a troca por uma nova, mantendo o algoritmo inicial.

A segurança de um sistema de criptografia vai variar conforme o tamanho da chave utilizada. Um algoritmo baseado no data encryption standart (DES ou padrão de criptografia de dados, em tradução livre) tem 56 bits, o que permite a criação de 72 quadrilhões de chaves diferentes. Pode parecer muito, mas esse padrão já é considerado inseguro diante da capacidade de processamento dos dispositivos atuais.

Por outro lado, sistemas como o RC2, que utiliza o protocolo S/MIME, tem uma chave de tamanho variável. Ela pode ter entre 8 e 1.024 bits. Assim, as chances de alguém conseguir decifrar um conteúdo criptografado por meio de algoritmos de força bruta diminui consideravelmente.

Apesar do seu alto desempenho, a criptografia simétrica possui falhas graves de segurança. A gestão de chaves, por exemplo, torna-se mais complexa conforme o número de pessoas que se comunica aumenta. Para cada N usuários, são necessárias N2 chaves.

A criptografia simétrica também não possui meios que permitem a verificação da identidade de quem envia ou recebe um conteúdo. Além disso, não há como garantir o armazenamento em ambientes confiáveis das chaves de segurança.

Na criptografia simétrica, toda a segurança é centrada na chave. Portanto, deve ser secreto e não fácil para uma terceira pessoa adivinhar. No entanto, com a tecnologia que temos hoje, o principal processo de comunicação ou distribuição se tornou o ponto fraco desse método. Como ao se comunicar (remetente e destinatário) para definir e concordar com a senha, um terceiro pode interceptar a referida comunicação, obter a senha e acessar as informações contidas na mensagem.

##### Padrão de Criptografia de Dados (DES)
Foi o primeiro método de criptografia de computador desenvolvido pela empresa IBM em 1975. Esse algoritmo funciona em blocos e emprega uma chave simétrica de 64 bits que passa por 16 interações. Dos 64 bits, 56 bits são usados ​​para criptografia. E os 8 bits restantes são usados ​​para paridade e detecção de erros e são descartados. Portanto, o comprimento real da chave é 56 bits.

Para executar criptografia, esse algoritmo aplica uma série de permutações e substituições. Com o qual modifica inicialmente a sequência dos bits e grava o resultado em diferentes blocos de um determinado tamanho. Que são então criptografados independentemente. O processo consiste em 16 rodadas de criptografia e, uma vez concluídos, os resultados são agrupados em um bloco de tamanho de 64 bits que também está sujeito a outra permutação. O texto final que resulta de todo esse processo é a mensagem criptografada.

O DES possui 4 modos de operação: o Modo de livro de códigos eletrônico (BCE) que é usado para mensagens curtas de comprimento menor que 64 bits. O Modo de encadeamento de blocos de criptografia (CBC) usado para mensagens longas. O Feedback do bloco de criptografia (CFB)) usado para criptografar bit por bit ou byte a byte. E finalmente o Modo de Feedback de Saída (OFB) que tem o mesmo uso, mas também impede a propagação de erros.

No entanto, embora esse algoritmo no momento de sua criação tenha sido um avanço e estabeleceu as bases para a criptografia moderna que conhecemos hoje. Hoje, ele não é mais usado porque sua senha é muito curta e não é mais segura contra ataques de força bruta. Como demonstrado em 1999, quando foi quebrado.

##### Padrão de criptografia de dados triplo (3DES)
O algoritmo 3DES é o mesmo que o algoritmo DES, apenas como o nome indica, é aplicado 3 vezes. Dependendo das chaves utilizadas, um sistema mais robusto pode ser gerado. Por exemplo, se três chaves forem usadas, uma chave de 3 bits poderá ser gerada; se apenas duas chaves forem usadas, uma chave de 168 bits poderá ser gerada.

##### Padrão avançado de criptografia (AES)
Esse novo algoritmo foi o substituto do DES e é o atualmente usado porque seu método de criptografia é melhor adaptado às necessidades do século XXI. A criptografia AES pode ser usada tanto em software quanto em hardware, e o tamanho do bloco fixo é de 128 bits. Enquanto as teclas podem ser escolhidas à vontade entre 128, 192 e 256 bits. Comprimento de 128 bits, sendo um padrão. E, como seu antecessor, aplica criptografia de bloco.

O resultado da criptografia com esse método gera uma matriz de 4 linhas por 4 colunas. À qual, em seguida, são aplicadas uma série de rodadas de criptografia baseadas em operações matemáticas de acordo com o comprimento de suas chaves. Para uma chave de 128 bits, são aplicadas 10 rodadas de criptografia, para uma chave de 192 bits, 12 rodadas e, para uma chave de 256 bits, são necessárias 14 rodadas.

E, embora hoje seja um algoritmo amplamente usado, muitos criptografadores começam a duvidar de sua segurança. Como a possibilidade de ataques foi registrada em várias rodadas de criptografia, muito perto do número de rodadas necessário para a criptografia.

##### Quão segura é a criptografia simétrica?
Em termos de segurança, a criptografia simétrica não é tão confiável devido ao fato de que a chave privada deve ser compartilhada para descriptografá-la. Nesse tipo de criptografia, toda a segurança é refletida na chave. Portanto, compartilhá-lo representa uma grande vulnerabilidade se os sistemas de comunicação adequados não forem usados. No entanto, quando esse método é usado, dois parâmetros essenciais devem ser atendidos para que seja considerado seguro, que são:

- Após a criptografia das informações, a chave usada para criptografia e descriptografia não pode ser obtida. Nem as informações contidas na mensagem criptografada.
- O custo da descriptografia de informações deve ser maior que as mesmas informações contidas na mensagem criptografada.

#### [Chaves assimétricas](https://academy.bit2me.com/pt/o-que-%C3%A9-criptografia-assim%C3%A9trica/) (uso de chaves publica e privada)
Na criptografia Assimétrica (ou criptografia de chave pública) temos que a chave de cifração é diferente da chave de decifração e uma não pode ser facilmente gerada a partir da outra. Basicamente temos que no processo de encriptação utilizaremos uma chave “k1” em cima da mensagem em texto puro que então irá gerar um texto cifrado. Após isso, no processo de descriptografia usaremos outra chave “k2” em cima do texto cifrado e teremos como resposta de volta o texto claro.

Basicamente na criptografia assimétrica temos que a chave pública pode ser conhecida por todos e é utilizada para cifrar o texto claro. Por sua vez, a chave privada deve permanecer secreta e é utilizada para decifrar o texto cifrado. Esse processo nos garante a confidencialidade da informação. Porém, também é possível utilizar a chave privada para cifrar o texto claro e a respectiva chave pública para decifrar a mensagem criptografada. Neste caso, busca-se garantir a autenticidade. É caso típico de assinaturas digitais.

Para entendermos melhor como funciona esse processo imagina que eu queira enviar uma mensagem para o meu amigo João. Neste caso, devemos cifrar a mensagem com a chave pública de João. Ao receber a mensagem cifrada, João decifra a mensagem com a sua chave privada. Podemos notar que a confidencialidade está garantida, pois somente a chave privada de João pode decifrar a mensagem criptografada e somente ele possui essa chave, não a distribuindo para ninguém. Outra forma de utilizar a criptografia assimétrica é garantindo a autenticidade. Exemplificando o processo agora podemos imaginar que eu cifre a mensagem utilizando a minha chave privada e envie essa mensagem para João, podemos verificar que agora não foi utilizada a chave pública de João e sim a minha própria chave privada que somente eu e mais ninguém tem acesso. Como somente a minha chave pública pode decifrar a mensagem João tem certeza que quem enviou a mensagem foi eu.

Nesta criptografia temos também um alto custo computacional para criptografar e descriptografar. Na maioria dos casos o tamanho da chave é grande, maior que as utilizadas na criptografia simétrica, mas nem sempre isso é verdade, depende do algoritmo utilizado.

Portanto, uma chave pública é disponibilizada gratuitamente a qualquer pessoa que queira enviar uma mensagem. Uma segunda chave privada é mantida em sigilo, para que somente a própria pessoa a tenha. Isso significa que não precisaremos se preocupar com o envio das chaves públicas na Internet. Um problema com a criptografia assimétrica, no entanto, é que ela é mais lenta do que a criptografia simétrica. Ela requer muito mais capacidade de processamento para criptografar e descriptografar o conteúdo da mensagem.

Existem diferentes algoritmos assimétricos sendo uns dos mais conhecidos o RSA que tem esse nome devido aos seus desenvolvedores Rivest, Shamir, e Adleman. Este algoritmo é amplamente utilizado nos navegadores, para sites seguros e para criptografar e-mails.

##### [RSA](https://www.rfc-editor.org/rfc/rfc8017.html)
O RSA é o método de criptografia mais utilizado no mundo. No RSA utilizamos duas chaves, uma chave para encriptação e outra para decriptação. Ele resolve o problema de distribuição de chaves da criptografia simétrica usando envelopamento digital e a segurança é baseada na fatoração de números extensos. Quanto maior a chave maior a segurança, porém o processamento também é maior.

A construção de chaves é feita através da multiplicação de dois números primos relativamente grandes que gera um número que será elevado a um expoente que é um número público, e após isso ele é novamente elevado a outro expoente que é um número privado. Assim teremos um número público e um número privado. O processo de descriptografia (em que os números primos são novamente gerados) será revertido através de fatoração, que é o inverso da multiplicação.

O RSA foi construído sobre uma das áreas mais clássicas da matemática, a teoria dos números. Ele se baseia na dificuldade em fatorar um número em seus componentes primos (números divisíveis por 1 e por ele mesmo). Todo número inteiro positivo maior que 1 pode ser decomposto de forma única em um produto de números primos, por exemplo, 26 é um produto de 2 * 13, 44 é um produto de 2 * 2 * 11. Apesar de parecer simples fatorar esses números pequenos, a situação fica bastante complexa e demorada quando temos que fatorar números grandes não podendo ser resolvidos em um tempo polinomial determinístico. No RSA a chave pública e a chave privada são geradas com base na multiplicação de dois números primos e o resultado desta multiplicação será público, mas se o número for grande o suficiente, fatorar este número para descobrir os primos que multiplicamos para formá-lo pode demorar anos. Por isso que o RSA é seguro, sendo impossível quebrar a sua criptografia.

O método do RSA se dá primeiramente com a construção de uma tabela atribuindo a cada letra um número. Isto é necessário visto que o RSA codifica somente números. Após isso, escolhemos os números primos e quanto maior for esses números melhor. A RSA Data Security, que é responsável pela padronização do RSA, recomenda que se utilizem chaves de 2048 bits (o que resulta em um número com 617 dígitos) se quisermos garantir que a chave não seja quebrada até pelo menos o ano de 2030. Após a atribuição de números para as letras agora temos que calcular a função “totiente” que diz a quantidade de co-primos de um numero que são menores que ele mesmo. Feito isso, o próximo passo é calcular a chave pública que é onde escolhe-se um número "e" em que 1 < e < função totiente. Com a chave pública em mãos podemos agora cifrar a mensagem aplicando, para cada letra, a fórmula “c = m ^ e mod n”, onde "e" é a chave pública e "m" é o valor numérico da letra.

Para exemplificar o funcionamento do algoritmo vamos escolher inicialmente dois números primos quaisquer “P” e “Q”. Obviamente que vamos escolher dois números primos pequenos apenas por questão de exemplificação. Portanto, consideramos que “P = 17” e “Q = 11”.

Após definirmos os valores dos números primos devemos calcular dois novos números N e Z de acordo com os números P e Q escolhidos, portanto temos que:

```
N = P * Q

Z = (P-1)*(Q-1)
```

Assim, após substituir os valores teremos como resultado:
``` 
N = 17 * 11 = 187

Z = 16 * 10 = 160
```

O próximo passo é definir um número D que tenha a propriedade de ser primo em relação a Z. Podemos escolher qualquer número como, por exemplo, o número “7”.

Agora podemos começar o processo de criação da chave pública e da chave privada. Devemos encontrar um número E que satisfaça a propriedade "(E * D) mod Z = 1". Se tomarmos o número “1” e substituindo os valores na fórmula teremos "E = 1 => (1 * 7) mod 160 = 7" que não satisfaz a condição, pois o resultado foi “7”. Se tomarmos os números “2”, “3” até o “22” nenhum satisfará a condição, mas o número “23” satisfará resultando em "E = 23 => (23 * 7) mod 160 = 1". Outros números também satisfazem essa condição, como “183”, “343”, “503”, etc.

Dessa forma, tomamos como referência “E = 23”. Agora podemos definir as chaves de encriptação e desencriptação. Para criptografar utilizamos “E” e “N”, esse par de números é utilizado como chave pública. Para descriptografar utilizamos “D” e “N”, esse par de números é utilizado como chave privada.

Assim, temos as equações definidas abaixo:
``` 
Texto Criptografado = (Texto Puro ^ E) mod N

Texto Puro = (texto Criptografado ^ D) mod N
``` 

Como um exemplo prático vamos imaginar uma mensagem bastante simples que tem o número “4” no seu corpo e será retornada ao destinatário. Para criptografar essa mensagem teríamos o texto original como sendo “4”, o texto criptografado seria "(4 ^ 23) mod 187" que é "70.368.744.177.664 mod 187" resultando em “64”.

Para descriptografar destinatário recebe o texto “64”. Recebido o texto criptografado e aplicando a fórmula temos que o texto original será "(64 ^ 7) mod 187" ou "4.398.046.511.104 mod 187" que resulta em “4” que é o texto originalmente criado. Como o RSA trabalha com número devemos converter um alfabeto em número, assim a letra A seria 0, B seria 1, C seria 2, e assim por diante.

Podemos notar que a escolha dos números primos envolvidos é fundamental para o algoritmo, por isso escolhe-se números primos gigantes para garantir que a chave seja inquebrável.

#### Prós e contras da criptografia assimétrica
##### Vantagens
- Este sistema oferece uma alta taxa de segurança, pois o esquema de criptografia é altamente complexo. A análise criptográfica desses sistemas é complicada e os ataques de força bruta para quebrá-lo são ineficientes e impraticáveis.
- Permite proteger canais de comunicação abertos e públicos, graças ao esquema de chaves públicas e privadas. Isso permite que remetente e destinatário compartilhem informações com segurança.
- O sistema também permite a autenticação das informações criptografadas, graças a um processo de assinatura digital.
- Oferece um alto nível de confidencialidade, integridade e garante o não repúdio às informações.
##### Desvantagens
- Comparado ao sistema de criptografia simétrica, é computacionalmente mais caro.
- O sistema de criptografia é suscetível a elementos além da programação do sistema de criptografia. Por exemplo, um gerador de números aleatórios com defeito comprometeria completamente o sistema de criptografia.
- A complexidade dos algoritmos resulta em dificuldades na análise de sua operação e segurança. Isso torna a detecção de falhas ou bugs mais complexa e difícil nesses sistemas.
- Alguns esquemas de propagação de confiança são centralizados. Este é um ponto importante de falha que pode resultar em adulteração de certificado se a estrutura estiver comprometida.


### Afinal, qual é a diferença entre a criptografia simétrica e assimétrica?
A criptografia simétrica usa uma chave privada para criptografar e descriptografar um e-mail criptografado.
A criptografia assimétrica usa a chave pública do destinatário para criptografar a mensagem. Então, se o destinatário quiser descriptografar a mensagem, ele terá que usar sua chave privada para descriptografar. Se as chaves corresponderem, então a mensagem é descriptografada.

### Qual encriptação é mais segura?
A criptografia assimétrica é considerada mais segura, pois você não precisa compartilhar chaves, a chave pública já está disponível publicamente. Com a criptografia simétrica, você tem que compartilhar a frase-chave de uma forma ou de outra, portanto corre o risco de vazar a frase-chave e comprometer potencialmente a mensagem criptografada.

### Fontes e links uteis:
- https://academy.bit2me.com/pt/que-es-criptografia-simetrica/
- https://www.devmedia.com.br/criptografia-assimetrica-criptografando-e-descriptografando-dados-em-java/31213
- https://academy.bit2me.com/pt/o-que-%C3%A9-curva-el%C3%ADptica-ecdsa/
- https://en.wikipedia.org/wiki/PKCS

## [JWT](https://jwt.io/)

O [JWT (JSON Web Token)](https://jwt.io/) é definido no site oficial na seguinte forma http://jwt.io: “JWT é um padrão aberto que define uma forma compacta e auto-contida para transmitir de forma segura, informações entre duas partes como objeto JSON”.

Quando estamos trabalhando com API’s, nós precisamos pensar na segurança no momento no momento de trafegar os dados e principalmente no nível de permissão que cada usuário deverá ter. Existem muitas formas de se fazer isso, mas uma que vem se destacando a cada dia que se passa é o JWT (JSON Web Token), por ser muito seguro e fácil de se implementar. Nas próximas sessões, será abordado a sua teoria com alguns exemplos e no final iremos criar uma aplicação com Node.js para exemplificarmos melhor o seu funcionamento.

Bom, o JWT (JSON Web Token) é um sistema de transferência de dados que pode ser enviado via POST ou em um cabeçalho HTTP (header) de maneira “segura”, essa informação é assinada digitalmente por um algoritmo HMAC, ou um par de chaves pública/privada usando RSA. Podemos ver na imagem a baixo um cenário onde será requisitado um token através do Verbo HTTP POST, que irá devolver um token validado para que nas próximas requisições que utilizem os Verbos HTTP possam utilizar.

O JWT é divido em três partes separadas por um “.” essas três partes são o Header,Payload e a Signature

### Header

O header é a primeira parte do JWT e ele é divido em duas partes, o algoritmo de codificação e o tipo do token e essas duas partes são encodadas em Base64, ficaria assim:

``` JSON
{
    "alg": "HS256",
    "typ": "JWT"
}
```

A propriedade “alg" define o algoritmo do token que nesse caso é o HMAC SHA256 e a propriedade “typ" é o tipo do token que é o JWT. 

Após ser enconcado em Base64 o header fica assim:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
```

### Payload (Claims)
Os payloads são objetos JSON que contem os claims, nessa parte que nós trabalhamos com os “pedidos”, carga de dados ou dados enviados. Existem 3 tipos de claims em Payloads: reserved, public, e private claims.

Reserved claims: Atributos não obrigatórios (mas recomendados) que podem ser um conjunto de informações uteis e interoperáveis normalmente utilizados por protocolos de segurança em API’s:

| Chave |  Descrição |
|:-:|:-|
|**iss** | (Issuer) Origem do token |
|**iat** | (issueAt) Timestamp de quando o token foi gerado |
|**exp** | (Expiration) Timestamp de quando o token expira |
|**sub** | (Subject) Entidade a quem o token pertence, normalmente o ID do usuário |
|**Publiclaims** | São atributos que definem o uso do JWT e informações úteis para a aplicação | 
|**Private claims** | São atributos definidos especialmente para compartilhar informações entre aplicações |

**Exemplo:**
``` JSON 
{
    "nome":"fulano",
    "admin": true
}
```

Após ser enconcado em Base64 o payload ficaria assim:

```
eyJub21lIjoiRnVsYW5vIiwiYWRtaW4iOnRydWV9
```

### Signature

Por último temos signature que é o header e payload codificado com o algoritmo do header junto com uma palavra segredo que é usada pra codificar e não deve ser compartilhada com ninguém.

Após ser enconcado em Base64 ficaria assim:

```
IShPdPgMqjygLcv6FpePbFuRLJHBTdeKSNDQIpR-X2E

``` 

Então nosso token completo fica assim:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJub21lIjoiRnVsYW5vIiwiYWRtaW4iOnRydWV9.IShPdPgMqjygLcv6FpePbFuRLJHBTdeKSNDQIpR-X2E 
```

### Fontes e links uteis:
- https://jwt.io/
- https://www.rfc-editor.org/rfc/rfc7519
- https://www.devmedia.com.br/como-o-jwt-funciona/40265
- https://auth0.com/blog/how-to-handle-jwt-in-python/
- https://pyjwt.readthedocs.io/en/latest/usage.html
- https://imasters.com.br/desenvolvimento/json-web-token-conhecendo-o-jwt-na-teoria-e-na-pratica

## Mitigação de riscos e boas práticas
### Healthcheck
### CircuitBrake
### Caches
### API Gateways/ BFF
### SQL Injections
### DDOS

## [Swagger e OpenAPI](https://swagger.io/docs/specification/about/)
#### Fontes e links uteis:
- https://swagger.io/docs/specification/about/
- https://gr1d.io/2022/04/15/swagger/
- https://medium.com/@ronilsonribeiro/como-interpretar-um-swagger-cdc331b68804

## Outras ferramentas de desenvolvimento de APIs