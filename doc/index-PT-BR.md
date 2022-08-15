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
- Não é um "framework".
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

Em outras palavras, uma API é um software intermediário entre dois aplicativos interagindo uma com a outra. Ela conecta dois computadores ou programas de computador através de uma interface.

Não confunda esta interface com a interface do usuário, que conecta uma pessoa a um computador ou programa de computador. A API conecta peças de software e computadores entre si e não é para ser usada diretamente pelo usuário final, exceto pelo programador que deseja integrá-la a uma solução de software.

As APIs simplificam a programação e podem realmente esconder os detalhes internos de um sistema, como por exemplo como ele funciona, e expor peças úteis para um programador enquanto mantém as peças consistentes apesar das mudanças internas. Você pode encontrar uma variedade de APIs hoje em dia para vários propósitos, tais como sistemas operacionais, bibliotecas de software, linguagens de programação, hardware de computador, etc.

Além disso, construir uma API requer que você siga um padrão ou documento chamado especificação da API que lhe diz como usar ou construir uma API.

As APIs consistem de muitas partes diferentes atuando como uma coleção de serviços ou ferramentas para o uso do programador. O programador ou programa que usa estas partes deve fazer uma "chamada" ou solicitação primeiro. Estas chamadas são referidas como solicitações, métodos, pontos finais ou sub-rotinas.

### Componentes de uma API
As APIs incluem especificações técnicas que explicam a troca de dados entre serviços através de solicitações de processamento e entrega de dados. Elas também possuem uma interface de software para permitir que os aplicativos troquem informações. As APIs também têm:

- Protocolos: São um conjunto de regras para definir a forma como os aplicativos interagem entre si, como HTTP, SOAP, XML-RPC, REST, etc.
- Formato: Este é o estilo para a troca de dados entre aplicativos. Ele define como a API irá recuperar os dados e fornecê-los aos consumidores. A API pode fazer solicitações através de um protocolo e recuperar informações em um determinado formato, como XML ou resposta JSON.
- Procedimentos: São tarefas, ações ou funções específicas que um aplicativo executa.
- Ferramentas: Elas são usadas para construir APIs. Você pode encontrar muitas ferramentas disponíveis para construir, testar e gerenciar suas APIs, tais como AWS, IBM Cloud, SoapUI, JMeter, etc.

### Tipos de APIs
As APIs são de diferentes tipos baseados em diferentes parâmetros. Com base na política de lançamento, as APIs são categorizadas em três tipos – públicas, privadas e partners.

#### APIs públicas
Eles estão disponíveis para uso por qualquer usuário ou desenvolvedor de terceiros e permitem que você aumente o conhecimento da sua marca e renda com a execução adequada. Eles são de dois tipos – abertos e comerciais.

- APIs abertas: As funcionalidades são públicas e as pessoas podem usá-las livremente sem qualquer restrição ou aprovação da editora. Sua documentação e descrição também deve estar disponível para uso público para criar novos aplicativos.
- APIs comerciais: Estão disponíveis para uso público, mas você pode ter que pagar certas taxas para usar a API. Muitos editores oferecem um teste gratuito das APIs por um período limitado antes que as pessoas paguem uma taxa de assinatura.

#### APIs privadas
As APIs públicas são projetadas para melhorar os serviços e soluções dentro de uma empresa. Seus desenvolvedores podem usá-las para integrar aplicativos e sistemas de TI e construir aplicativos e sistemas usando os sistemas existentes.

Embora os aplicativos estejam disponíveis para uso público, a interface do aplicativo está disponível apenas para pessoas que trabalham com o proprietário da API. Isto permite que os editores ou proprietários da API controlem o uso da API e salvaguardem sua integridade.

#### APIs partner
APIs partner podem ser promovidas abertamente, mas são compartilhadas somente com os parceiros comerciais da editora que assinaram um acordo mútuo. APIs partner são comumente usadas para integração de software.

Uma empresa pode conceder a seus parceiros acesso a certas capacidades ou dados enquanto monitora aspectos chave. Ela monitorará continuamente como os ativos compartilhados são usados, gerenciará a identidade corporativa através dos aplicativos e assegurará que os terceiros que utilizam suas APIs ofereçam uma boa experiência ao usuário.

Com base em casos de uso, as APIs são de diferentes tipos:

#### APIs Web
As APIs Web são um tipo comum de API que fornece funcionalidade legível por máquina e transferência de dados entre dois ou mais serviços ou sistemas baseados na Web que representam uma arquitetura cliente-servidor. Elas são usadas principalmente para fornecer respostas do servidor e solicitações de aplicativos web usando o Protocolo de Transferência HyperText (HTTP).

APIs Web ajudam a estender a funcionalidade de um aplicativo ou site. Por exemplo, você pode usar o Google Map API para adicionar um mapa com a localização da sua organização ao seu site.

#### APIs de Sistema Operacional
APIs de sistemas operacionais (SO) definem como um aplicativo pode usar os serviços e recursos de um sistema operacional. Cada sistema operacional compreende diferentes APIs, tais como a API do Windows.

#### APIs de banco de dados
As APIs de banco de dados são usadas para interagir com um aplicativo com um sistema de gerenciamento de banco de dados (SGBD). Seus desenvolvedores podem aproveitar bancos de dados, escrever consultas para acesso aos dados, alterar tabelas e realizar outras ações.

#### APIs remotas
APIs remotas são padrões de comunicação para aplicativos que rodam em múltiplas máquinas. É chamada de “remota” porque uma solução de software pode acessar recursos externos a partir de um dispositivo que faz uma solicitação.

Neste arranjo, dois aplicativos remotas se comunicam uma com a outra através de uma rede (internet). Portanto, um grande número de APIs remotas são desenvolvidas seguindo um padrão web. Exemplos de APIs remotas podem ser Java Remote Method Invocation API.

#### As APIs também podem ser de mais tipos:
- APIs REST: As APIs REST ou RESTful APIs são projetadas para fazer solicitações e receber respostas HTTP. Ela é baseada em vários comandos HTTP – GET, POST, PUT, e DELETE.
- APIs RPC: As APIs de Chamada de Procedimento Remoto (RPC) são APIs antecipadas projetadas para executar um bloco de código em servidores diferentes. Ela se transforma em Web API quando você a usa através de HTTP.
- APIs SOAP: Simple Object Access Control Protocol (SOAP) refere-se a um protocolo padrão que depende de programação e sistemas baseados em XML e tem dados maiores e mais caros. Eles oferecem um alto nível de segurança e são amplamente utilizados em aplicativos baseados em finanças.

### Fontes e links uteis:
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

- API REST são projetadas para recursos, que tratam de qualquer tipo de objeto, dados ou serviço que possa ser acessado pelo cliente;
- Um recurso tem um identificador, o qual se trata de um URI que identifica exclusivamente esse recurso;
- Os clientes interagem com um serviço por meio da troca de representações de recursos (JSON ou XML)

### O que são os [verbos](https://www.rfc-editor.org/rfc/rfc9110.html#name-methods)? GET, POST e etc?
Tanto GET como POST na verdade são [métodos HTTP](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Methods). Eles indicam para o servidor qual a ação que o cliente deseja realizar. Quando realizamos uma requisição obrigatoriamente precisamos informar um método.

 - **[GET](https://www.rfc-editor.org/rfc/rfc9110.html#name-get)** – é usado quando o cliente deseja obter recursos do servidor
 - **[POST](https://www.rfc-editor.org/rfc/rfc9110.html#name-post)** – é usado quando o cliente deseja enviar dados para processamento ao servidor, como os dados de um formulário, por exemplo.
 - **[PUT](https://www.rfc-editor.org/rfc/rfc9110.html#name-put)** – é usado quando o cliente deseja atualizar um dado de um recurso que está no servidor
 - **[DELETE](https://www.rfc-editor.org/rfc/rfc9110.html#name-delete)** – é usado quando uo cliente deseja apagar um dado dew um recurso que está no servidor

Existem outros métodos HTTP. Os dois métodos citados acima são os mais usados, principalmente em aplicações web. Quando o usuário digita um endereço e aperta enter na barra de endereço do navegador, ele realiza uma requisição do tipo GET. Já quando preenchemos um formulário e clicamos em enviar geralmente o método usado é o POST.

### Cuidado com a Semântica de seus serviços
Devemos tomar cuidados na organização da semântica do nossos serviços. Uma boa semântica dos serviços farão eles serem de fácil leitura e compreensão.

Veja algumas dicas para a construção de uma boa semântica:

- Organize sua API em torno de recurso;
- Concentre-se nas entidades comerciais que sua API expõe;
- O caminho de sua API ou URI (UNIFORM RESOUCE IDENTIFIER) deve ser baseado em substantivos e não em verbos

Veja aqui alguns exemplo:
| Faça | Evite |
|:-:|:-|
| GET /items | GET /getItems |
| GET /items/123 | GET /getItemById |
| POST /items | POST /createItem |

### Aplique corretamente o HTTP Status Code
O HTTP Status Code é a forma que seus serviços irão retornar as respostas para seus clientes. É importante aplicar corretamente o HTTP Status Code para cada operação, veja abaixo como podemos retornar corretamente o HTTP Status Code para cada Verbo HTTP.

| Verbo/Método | Tipo de retorno |
|:-: |:-|
| **GET** | Retorne 200 (OK) para caso de sucesso |
| **GET** | Retorne 404 (NOT FOUND) se a entidade não for encontrada |
| **POST** |Retorne 201 (CREATED) para caso um novo recurso seja criado com sucesso | 
| **POST** |Retorne 400 (BAD REQUEST) caso a solicitação contenha dados inválidos | 
| **POST** |Retorne 422 (Unprocessable Entity) caso a solicitação caia em alguma regra de  | negócio
| **PUT** |Retorne 200 (OK)  se for atualizar um recurso existente | 
| **PUT** |Retorne 400 (BAD REQUEST) caso a solicitação contenha dados inválidos | 
| **PUT** |Considere utilizar 409 (CONFLICT) caso não consiga atualizar um recurso existente | 
| **DELETE** |Retorne 204 (No Content) para sucesso | 
| **DELETE** |Retorne 404 (NOT FOUND) se a entidade não for encontrada | 

### Respostas de erros padrões
Devemos criar padrões de respostas dos nossos serviços em caso de erros. Considere sempre utilizar um objeto no qual abrange o erro, o código do erro, mensagem do erro e uma lista de detalhes para caso de múltiplos erros.

Veja como o nosso objeto de resposta de erro deve parecer:

``` JSON
//Erros genéricos
{
 "code": "0001",
 "message": "Acesso negado!"
}
//Erros de campos específicos
{
    "code": "0002",
    "errors": [
        {"nome": ["Nome em branco"]},
        {"idade": ["Idade em branco", "Você é menor de idade"]}
    ]
}
```

### Versionamento de API
Sempre que possível também, versione sua API. O versionamento dos seus serviços irá permitir que você controle quais clientes podem usar determinadas versões de APIs e permitirá direcionar o seus clientes para utilizar versões novas ou mesmo em preview.

Abaixo um exemplo de como podemos versionar nossas APIs:

- POR URL: api/com/v1
- POR SUBDOMÍNIO: v1.api.com
- POR HEADER: “Accept”=“application/vnd.api.v1.json” 
- POR QUERYSTRING: api.com/endpoint?version=2.0

### Algumas dicas de segurança na construção de APIs
- Implemente OAuth para os seus clientes consumirem suas API REST;
- Habilite o CORS (CROSS-ORIGIN RESOURCE SHARING) para controlar o acesso a sua API REST
- Evite o uso de Token estático para acesso a sua API
- Sempre use HTTPS para comunicação de sua API
- Não trafegue dados sensíveis na sua API sem criptografia adequada

### Fontes e links uteis:
- https://standards.rest/
- https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Methods
- https://www.rfc-editor.org/rfc/rfc9110.html#name-methods
- https://www.treinaweb.com.br/blog/o-que-e-http-request-get-post-response-200-404

## Qual a relação entre as APIs e os microserviços?

### O que são Microserviços?
Microserviços são serviços menores, acoplados frouxamente, que você pode implantar independentemente. Aqui, “serviços” referem-se a diferentes funções de um aplicativo.

Assim, em uma arquitetura de microserviços, as funções de um aplicativo são divididas em muitos componentes menores que servem a propósitos específicos. Estes componentes ou serviços são de granulação fina e normalmente têm pilhas de tecnologia, métodos de gerenciamento de dados e bancos de dados separados. Eles podem se comunicar com outros serviços do aplicativo através de APIs REST, corretores de mensagens e streaming.

A arquitetura de microserviços é uma abordagem eficaz para a construção de aplicativos. Uma vez que os serviços são livremente acoplados e distribuídos, mesmo que algo aconteça em um dos serviços, isso não afetará o resto do sistema, ao contrário das abordagens tradicionais.

O acoplamento solto ajuda a reduzir as complexidades e dependências de um aplicativo. Assim, as equipes de desenvolvimento podem acelerar o processo de desenvolvimento de novos componentes de aplicativo e atender às crescentes necessidades do negócio.

Aqui, os termos “microserviços” e “microserviços” são distintos um do outro. Um microserviço representa a funcionalidade central de um aplicativo e roda independentemente. Por outro lado, o termo “microserviços” significa a arquitetura completa para a construção de um aplicativo. Ele vai além das funções principais e do acoplamento solto – ele também reestrutura seus processos de desenvolvimento e comunicação para permitir a integração de novas funcionalidades, fornecer escalabilidade e prepará-lo para falhas e problemas.

### Componentes do Microserviços
Os principais componentes dos microserviços são API, lógica de negócios, camada de acesso aos dados e banco de dados. Vamos olhar para a versão expandida de diferentes componentes:

- Clientes: Estes podem ser aplicativos, sites, ou outros serviços. A arquitetura dos microserviços inclui vários tipos de clientes para lidar com algumas tarefas, tais como realizar uma busca, configuração, construção, etc.
- API Gateway: Este é o ponto de entrada para os clientes para que eles possam encaminhar pedidos para serviços adequados. A razão para usar um API Gateway é que os clientes não ligam diretamente para os serviços. O uso de API Gateways oferecerá muitos benefícios como manter os serviços atualizados, fornecendo balanceamento de carga, segurança e muito mais.
- Provedores de identidade: As solicitações dos clientes são encaminhadas aos provedores de identidade para autenticar essas solicitações e comunicá-las aos serviços internos através de um API gateway.
- Tratamento de dados: Microserviços têm bancos de dados privados para armazenar suas informações e implementar funcionalidades de negócios.
- Envio de mensagens: Microserviços interagem entre si através de mensagens para gerenciar as solicitações dos clientes. Estas mensagens podem ser de dois tipos: síncronas, onde o servidor espera obter uma resposta em tempo real, ou assíncronas, onde o cliente não espera por nenhuma resposta antes de agir.
- Conteúdo estático: Microserviços, após comunicarem-se entre si, implantam outro conteúdo estático em um serviço de armazenamento em nuvem para permitir a entrega direta do conteúdo aos clientes usando uma rede de entrega de conteúdo (CDN).
- Entrega do serviço: Este é um guia de microserviços para encontrar rotas de comunicação entre os microserviços. Ele gerencia uma lista de serviços onde os nós são encontrados.

### Tipos de Microserviços
Os microserviços podem ser categorizados em dois tipos amplos – microserviços stateless e stateful.

- Microserviços sem Estado: Estes são os blocos de construção de sistemas distribuídos. Eles não mantêm ou armazenam nenhum estado de sessão entre duas solicitações, daí o nome “stateless” micro-services. Além disso, mesmo que uma instância de serviço seja removida, a lógica geral de processamento do serviço não é afetada. Esta é a razão pela qual os sistemas distribuídos aproveitam os microserviços “stateless”.
- Microserviços estáticos: Os microserviços estáticos mantêm ou armazenam estados ou dados de sessão em código. Microserviços que se comunicam entre si sempre mantêm solicitações de serviço.
Os microserviços sem Estado são usados mais amplamente, mas você pode usar o estado para múltiplos cenários.

Por exemplo, suponha que um cliente faz um pedido. Aqui “pedido” representa um microserviço. Então, o serviço de pedido começa a verificar o status do produto usando outro serviço – inventário. Quando cada pedido é independente de pedidos futuros ou anteriores, isto significa que o sistema segue uma arquitetura sem estado.

Quando você tenta buscar as informações do produto através de uma chamada, você obterá o mesmo resultado independentemente das solicitações ou contexto anteriores. E mesmo se um pedido falhar, ele não colocará em risco o processamento geral do negócio. Outro microserviço estará pronto para manter o processo funcionando.

## Os microserviços são RESTful?
Bem, não necessariamente. Vamos rever brevemente as diferenças:

- Microserviços: Este é um conjunto de funções e serviços que atuam como blocos de construção de um aplicativo.
- APIs RESTful: Estas representam os protocolos, comandos e regras para integrar todos os microserviços em uma única aplicativo.

Microserviços é sobre o estilo de design e arquitetura de um aplicativo, e você pode construir microserviços com ou sem o uso de uma API RESTful. Dito isto, usar RESTful tornará muito mais fácil desenvolver microserviços acoplados frouxamente.

O RESTful API surgiu antes dos microserviços. Ela assume que todos os objetos têm interfaces uniformes e são completamente agnósticos de linguagem e acoplados frouxamente. Aqui, a semântica e as interfaces permanecem as mesmas, e a implementação de API pode mudar facilmente a qualquer momento sem afetar os consumidores. Portanto, RESTful e os Microserviços podem resolver problemas diferentes; eles ainda podem trabalhar juntos.


### Como os Microserviços funcionam?
Para entender como os microserviços funcionam, vamos voltar ao passado.

O desenvolvimento de software tradicional, que ainda continua em muitas organizações, utiliza uma arquitetura monolítica. Um “monólito” se refere a uma única e grande aplicativo que contém todas as suas funcionalidades e características e armazena tudo em um único lugar.

Isto significa que todos os componentes de um aplicativo, incluindo a lógica comercial, acesso aos dados e IU, são armazenados no mesmo local.

O desenvolvimento deste software é, de fato, fácil e vem naturalmente. É por isso que muitos ainda optam por ele. Entretanto, ele fica complicado se você quiser adicionar mais funcionalidade ao seu aplicativo a fim de torná-la atraente ou aumentar seu propósito, usabilidade, segurança, etc. Adicionar mais funcionalidades à base de código existente pode aumentar a complexidade e o tamanho do monólito, o que convida a várias questões, como por exemplo:

- A mudança pode afetar o aplicativo geral, mesmo se você quiser fazer uma pequena mudança. Você pode exigir a redistribuição do aplicativo completa, que é arriscada e consome tempo e recursos.
- Devido à sua estrutura rigidamente acoplada, os monólitos não são flexíveis. Portanto, ele também restringe a pilha de tecnologia, especialmente quando o aplicativo é escalonado. Você pode encontrar dificuldade em mudar sua pilha de tecnologia e pode ser forçado a usar as tecnologias antigas com tantos problemas subjacentes.
- É arriscado porque se alguma vulnerabilidade for deixada despida e a parte for comprometida, o ataque pode se espalhar pelo aplicativo, comprometendo todo o aplicativo e seus dados.
Portanto, quebrar as funções de um aplicativo em diferentes partes parece ser uma excelente abordagem para abordar todas essas questões, que é exatamente o que os microserviços fazem. Vamos entender como a arquitetura dos microserviços é colocada em movimento.

Em uma arquitetura de microserviços, os aplicativos são estruturados em serviços reutilizáveis e discretos, comunicando-se através de uma API. Cada serviço é organizado em torno de um processo de negócios particular e adere a um protocolo de comunicação como o HTTP. Estes serviços menores são então integrados separadamente com suas dependências e outros dados no aplicativo.

Portanto, se você quiser fazer algumas mudanças em uma funcionalidade, você pode fazer isso sem afetar as outras partes do aplicativo com facilidade.

Essas capacidades tornam os microserviços desejáveis para abordagens modernas de desenvolvimento de software como o DevOps. Embora a arquitetura de microserviços não seja inteiramente um conceito novo, uma vez que ela evoluiu de abordagens tradicionais e da Arquitetura Orientada a Serviços (SOA), ela está agora difundida devido aos recentes avanços tecnológicos, como a contenção.

Usando containers Linux, você pode facilmente executar várias partes do aplicativo separadamente em um único hardware com controles maiores.

### Como as APIs funcionam?
A interface de programação do aplicativo (API) fornece respostas dos usuários aos sistemas e envia as respostas de volta aos usuários.

Esta é a versão mais simples de colocar como uma API funciona, mas muita coisa acontece em segundo plano. Uma API permite que um desenvolvedor faça uma solicitação ou uma chamada para transferir informações. Esta interação acontece através da programação JSON. Ela também executa muitas ações como adicionar e remover dados, coletar informações e atualizar detalhes. 

Sem APIs, muitas das coisas divertidas que você faz online não seriam possíveis, como jogar jogos de vídeo online, encomendar produtos de lojas virtuais, encontrar o perfil no Facebook de um amigo há muito perdido, e assim por diante.

A API funciona como uma interface intermediária para permitir que dois aplicativos interajam uma com a outra e atendam ao seu pedido.

Por exemplo, quando você quer pedir acessórios de bicicleta da Amazon, você visita o aplicativo e coloca o item em seu carrinho. Em seguida, a interface o levará para o endereço de entrega e página de pagamentos para que você entre.

É aqui que ocorre a comunicação entre os aplicativos, graças à API. Por exemplo, se você escolheu o Google Pay como seu processador de pagamento, o aplicativo enviará suas credenciais bancárias para outro aplicativo para verificação. Uma vez verificada e confirmada, a segunda aplicativo irá notificar o Google Pay para completar esta transação.

Uma vez que você tenha inserido seu PIN e procedido com a transação, o Google Pay facilitará a troca de dados e completará o pagamento. Naquele momento, seu pedido será feito.

Ao permitir que os produtos e serviços de software se comuniquem entre si, as APIs simplificam o desenvolvimento de aplicativos, o dinheiro e o tempo. APIs dariam a você a flexibilidade e o controle do projeto para inovar.

### Microserviços vs API: Benefícios de cada um deles
Vamos comparar microserviços vs API sobre como eles são benéficos para desenvolvedores, usuários finais e empresas.

#### Benefícios da utilização de Microserviços
Dividir as funções de um aplicativo em serviços menores ou microserviços tem muitas vantagens. Vejamos um por um.

- Modularidade: Significa dividir os serviços em diferentes módulos com seu próprio conjunto de funcionalidades e dependências para tornar-se um aplicativo fácil de desenvolver, testar e entender. Isto reduz as complexidades e dificuldades que as empresas enfrentam com a abordagem monolítica de desenvolvimento de software.
- Desenvolvimento distribuído: A arquitetura de microserviços agiliza o processo de desenvolvimento, já que equipes menores podem ter a responsabilidade de desenvolver, testar, implantar e expandir serviços separadamente e em paralelo.
- Escalabilidade: Nos microserviços, uma abordagem acoplada frouxamente é implementada, separando a lógica de negócios, a camada de acesso aos dados e o banco de dados. Em contraste, os microserviços podem ser desenvolvidos e implantados independentemente para executar suas tarefas e podem ser escalados facilmente. Devido à escala precisa, você pode escalar apenas aqueles componentes que você deseja.
- Implantação independente: Como os serviços são pequenos e podem ser implantados de forma independente, qualquer mudança que você fizer não afetará todo o aplicativo. Então, quando você quiser atualizar um recurso, você pode pegar um microserviço para começar a trabalhar diretamente nele e implementá-lo sem reimplantar o aplicativo completo.
- Integração sem emendas: Com os microserviços, você pode realmente modernizar o seu aplicativo monolítico atual. Isto pode ser feito usando a integração de sistemas legados e heterogêneos. Microserviços também são fáceis de integrar com muitas tecnologias e ferramentas para ajudar a melhorar as características, funcionalidade e segurança do seu aplicativo.
- Flexibilidade: Microserviços oferece a você uma melhor flexibilidade. Você está livre para usar qualquer pilha de tecnologia com linguagens de programação, bibliotecas, frameworks e outras ferramentas se for suportado por diferentes componentes ou serviços. Assim, você pode construir os serviços mais recentes e mais avançados para complementar seu aplicativo com as últimas características e recursos de segurança.
- Segurança: A arquitetura Microserviços ajuda a aumentar a segurança do seu aplicativo. Eles são feitos para lidar com compromissos e falhas. Como vários tipos de serviços se comunicam dentro desta arquitetura, um serviço pode falhar devido a problemas no servidor, cyberattacks, etc. Mesmo se um dos serviços falhar, ele não derrubará a aplicativo inteira; as outras partes ainda terão o desempenho esperado.
- Roteamento simples: Microserviços seguem uma abordagem simples de roteamento para receber solicitações e transmitir respostas de acordo. Microserviços são desenvolvidos com endpoints inteligentes ou clientes que podem processar informações e aplicar lógica de negócios de acordo com os requisitos. Entretanto, outras estratégias como os Enterprise Service Buses (ESBs) não fazem isso. Eles utilizam sistemas de alta tecnologia para aplicar políticas de negócios e roteamento de mensagens.
- Aumento da produtividade: Em uma metodologia de desenvolvimento distribuído onde as responsabilidades são divididas, ela ajuda a aumentar a produtividade organizacional. Uma grande tarefa pode ser dividida em tarefas menores que parecem facilmente realizáveis com precisão.
- Manutenção e Depuração mais fáceis: Criar serviços menores é mais fácil para os desenvolvedores codificarem e depurarem. Eles podem analisar os serviços em geral rapidamente para detectar erros e problemas em contraste com a cena quando eles tiveram que analisar um aplicativo massiva com todas as suas dependências e características.
- Tempo mais rápido para o mercado: Como resultado de um desenvolvimento de código, teste, depuração e implantação mais rápidos enquanto garante a qualidade, seu tempo de colocação no mercado será mais rápido. Você pode obter feedback antecipado e melhorar seu aplicativo mais rapidamente ao invés de implantar tudo de uma só vez. Isto o ajudará a produzir aplicativos de qualidade que os clientes adoram usar.

Embora os microserviços pareçam ser uma abordagem eficiente que pode lhe oferecer muitos benefícios (o que ele faz), há alguns desafios também.

- A mudança de uma arquitetura monolítica tradicional para microserviços pode ser complexa, com muitos serviços, equipes e implantações.
- Novas versões de software podem apresentar problemas de compatibilidade com versões anteriores
- As redes irão ter mais problemas de conectividade e latência
- Os dados de registro podem ser um fardo

No entanto, o DevOps pode resolver muitos desses problemas; ele pode ter seus próprios desafios. O cálculo dos riscos e benefícios ainda pesa muito mais do que os riscos.

### Benefícios do uso de APIs
As APIs se tornaram cruciais no mundo moderno dos negócios, com pessoas alavancando a internet e os serviços como nunca antes. Aqui estão alguns dos benefícios das APIs:

- Velocidade: As APIs oferecem uma velocidade incrível para várias tarefas tanto para as empresas quanto para os usuários. Elas ajudam a acelerar as operações para oferecer agilidade para as empresas e reduzir os incômodos para os clientes. Por exemplo, se você quiser encomendar algo online, você pode ir diretamente ao seu aplicativo e verificar se o item está disponível ou não.
- Escalabilidade: Se você é um negócio em crescimento, a primeira coisa que você deve assegurar é se a sua pilha de tecnologia é escalável ou não. Ela lhe oferecerá a oportunidade de fazer seu negócio crescer com o tempo. Usar uma API lhe dará uma tremenda flexibilidade e escalabilidade para expandir seus produtos, aumentar o número de catálogos, gerenciar dados cada vez maiores e lidar com riscos crescentes de segurança.
- Segurança: O uso de APIs é uma ótima maneira de aumentar a segurança do seu aplicativo. A razão é que quando você faz uma chamada de API, você não está diretamente conectado a um servidor web. Ao invés disso, você está enviando uma pequena quantidade de dados que a API entrega para o servidor e recebe respostas do servidor. Portanto, seu aplicativo permanece a salvo de atacantes.
- Aumenta a produtividade: O uso de APIs permitirá que os desenvolvedores implementem mais funcionalidades rapidamente. Ao invés de fazer isso do zero. Isso economizará muito tempo e esforço para o negócio e para os desenvolvedores que podem dedicar tempo à inovação.
- Reduz o custo de TI: Construir um aplicativo, seja ela pequena ou grande, envolve um investimento significativo. Você precisará de tecnologias, ferramentas e pessoas junto com outros recursos para apoiar o seu processo de desenvolvimento. Mas você pode evitar todos eles uma vez, usando uma API adequada para construir seu aplicativo ou melhorar sua funcionalidade sem gastar uma fortuna.
- Promove a Colaboração: Manter uma conectividade e comunicação suave e segura se tornou um problema para as organizações devido ao aumento dos riscos de segurança. Mas o uso de APIs privadas pode ajudar a aumentar a comunicação e a colaboração em sua equipe ou organização.
- Impulsiona a Inovação: A forte competição entre as verticais da indústria tornou a inovação crucial para as empresas. Além disso, as demandas dos clientes estão mudando, mas as empresas devem se esforçar para atender a essas demandas.
- Melhor experiência do cliente: As APIs são benéficas também para os usuários finais. Elas ajudam os clientes a interagir com as empresas sem problemas e os fazem entender seus desafios, preferências e interesses. Por sua vez, as empresas podem levar esses inputs para trabalhar neles e melhorar seus produtos e serviços, ao mesmo tempo em que apresentam soluções inovadoras para atender às suas demandas.
Com as APIs, as empresas também podem personalizar as experiências dos clientes, o que é um fator chave para determinar o seu sucesso. Por exemplo, você pode usar APIs baseadas em inteligência artificial (IA) para analisar a jornada de compra de seus clientes, desde quando eles visitaram seu site até quando finalmente compraram de você. Isto o ajudará a mapear as dificuldades deles e resolvê-las e adicionar novas funcionalidades como mais opções de pagamento para tornar a compra mais fácil para eles.

Assim como os microserviços, os APIs também vêm com certos desafios, apesar de oferecerem benefícios fantásticos, como por exemplo:

- Nem todas as APIs são seguras, o que é a principal preocupação das organizações enquanto utilizam as APIs. Isso pode tornar seu aplicativo vulnerável a cibe ataques. Portanto, se você quiser usar uma API, escolha-a cuidadosamente, tendo em mente seus aspectos de segurança e conformidade.
- APIs podem fazer a performance de seu aplicativo depender da performance deles. Portanto, se a API tiver alguns problemas, ela afetará a performance de seu aplicativo, mesmo que seu aplicativo não tenha nenhum problema em si mesma. Isto implica que se a API for comprometida por um atacante, seus dados também podem ser.
- As APIs são tão boas que as organizações podem acabar usando muitas delas, mesmo em centenas. Agora, o problema é que quando múltiplas APIs rodam com seus serviços, dependências e pontos finais, pode se tornar difícil para a organização lidar com elas. Você pode se sentir sobrecarregado para controlar o uso das APIs em sua organização, monitorar dados e proteger sua segurança.

### Microserviços e API podem trabalhando juntos
Microserviços e API podem trabalhar juntos em um aplicativo. Embora eles possam existir separadamente, usar ambos juntos em seu aplicativo pode ajudar as organizações a implementar efetivamente a arquitetura de microserviços.

Muitas empresas enfrentam dificuldades para implantar a arquitetura de microserviços quando já possuem outras arquiteturas implantadas. Além disso, integrar múltiplos e menores serviços e se beneficiar deles é problemático.

Portanto, implementar uma estratégia de integração usando APIs é essencial para tirar o máximo proveito da arquitetura de microserviços.

Usando APIs, as empresas podem alcançar toda a flexibilidade e velocidade que o microservice oferece, além de reduzir a complexidade no desenvolvimento e implementação de software.

API pode fazer com que seja fácil construir e gerenciar seus microserviços enquanto permite que este novo modelo coexista com sistemas tradicionais ou legados. Desta forma, você não tem que descartar todos os seus sistemas legados uma única vez, o que pode colocar um estresse significativo nas organizações. Além disso, você pode expor suas funcionalidades de microserviços como produtos, o que ajuda a aumentar o valor do negócio tanto externa quanto internamente.

Além disso, APIs podem ajudar a reduzir os custos de TI para fazer uma integração ponto a ponto entre seus aplicativos SaaS e sistemas legados. Desta forma, você pode rapidamente adicionar ou remover microserviços com base nas suas necessidades de negócios. Eles também padronizam o gerenciamento de tráfego, monitoramento, auditoria, registro, segurança, etc., em toda a organização.

Assim, a combinação de microserviços com API permite que você alcance toda a bondade dos microserviços e limite seus inconvenientes.



### Fontes e links uteis:
- https://kinsta.com/pt/blog/microservicos-vs-api/

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

A criptografia através de cifras ocorre com a cifração da mensagem original através de operações de transposição e substituição de seus caracteres, resultando numa mensagem cifrada. Para decifração basta aplicar o processo inverso. Temos dois tipos de cifras, as cifras mono alfabéticas e as cifras poli alfabéticas. As cifras mono alfabéticas são compostas pela mais famosa de todas que é conhecida como Cifra de César onde basicamente cada letra do alfabeto é deslocada da sua posição um número fixo de lugares k, tal que 1<=k<=25 (número de letras que compõem o alfabeto). Originalmente a cifra anda três posições. Portanto, por exemplo, a palavra "senha" seria cifrada como "vhqkd", assim "s" andou três posições e foi para o "v", "e" andou mais três posições e foi para o "h" e assim por diante. A Cifra de César ainda é utilizada em algumas aplicações mais simples que necessitam de alguma criptografia. Por sua vez, as cifras poli alfabéticas são compostas pela cifra de Vigenère que consiste no uso de várias cifras de César em sequencia, com diferentes valores de deslocamento ditados por uma palavra-chave.

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
Na criptografia Assimétrica (ou criptografia de chave pública) temos que a chave de cifração é diferente da chave de decifração e uma não pode ser facilmente gerada a partir da outra. Basicamente temos que no processo de encriptação utilizaremos uma chave "k1" em cima da mensagem em texto puro que então irá gerar um texto cifrado. Após isso, no processo de descriptografia usaremos outra chave "k2" em cima do texto cifrado e teremos como resposta de volta o texto claro.

Basicamente na criptografia assimétrica temos que a chave pública pode ser conhecida por todos e é utilizada para cifrar o texto claro. Por sua vez, a chave privada deve permanecer secreta e é utilizada para decifrar o texto cifrado. Esse processo nos garante a confidencialidade da informação. Porém, também é possível utilizar a chave privada para cifrar o texto claro e a respectiva chave pública para decifrar a mensagem criptografada. Neste caso, busca-se garantir a autenticidade. É caso típico de assinaturas digitais.

Para entendermos melhor como funciona esse processo imagina que eu queira enviar uma mensagem para o meu amigo João. Neste caso, devemos cifrar a mensagem com a chave pública de João. Ao receber a mensagem cifrada, João decifra a mensagem com a sua chave privada. Podemos notar que a confidencialidade está garantida, pois somente a chave privada de João pode decifrar a mensagem criptografada e somente ele possui essa chave, não a distribuindo para ninguém. Outra forma de utilizar a criptografia assimétrica é garantindo a autenticidade. Exemplificando o processo agora podemos imaginar que eu cifre a mensagem utilizando a minha chave privada e envie essa mensagem para João, podemos verificar que agora não foi utilizada a chave pública de João e sim a minha própria chave privada que somente eu e mais ninguém tem acesso. Como somente a minha chave pública pode decifrar a mensagem João tem certeza que quem enviou a mensagem foi eu.

Nesta criptografia temos também um alto custo computacional para criptografar e descriptografar. Na maioria dos casos o tamanho da chave é grande, maior que as utilizadas na criptografia simétrica, mas nem sempre isso é verdade, depende do algoritmo utilizado.

Portanto, uma chave pública é disponibilizada gratuitamente a qualquer pessoa que queira enviar uma mensagem. Uma segunda chave privada é mantida em sigilo, para que somente a própria pessoa a tenha. Isso significa que não precisaremos se preocupar com o envio das chaves públicas na Internet. Um problema com a criptografia assimétrica, no entanto, é que ela é mais lenta do que a criptografia simétrica. Ela requer muito mais capacidade de processamento para criptografar e descriptografar o conteúdo da mensagem.

Existem diferentes algoritmos assimétricos sendo uns dos mais conhecidos o RSA que tem esse nome devido aos seus desenvolvedores Rivest, Shamir, e Adleman. Este algoritmo é amplamente utilizado nos navegadores, para sites seguros e para criptografar e-mails.

##### [RSA](https://www.rfc-editor.org/rfc/rfc8017.html)
O RSA é o método de criptografia mais utilizado no mundo. No RSA utilizamos duas chaves, uma chave para encriptação e outra para decriptação. Ele resolve o problema de distribuição de chaves da criptografia simétrica usando envelopamento digital e a segurança é baseada na fatoração de números extensos. Quanto maior a chave maior a segurança, porém o processamento também é maior.

A construção de chaves é feita através da multiplicação de dois números primos relativamente grandes que gera um número que será elevado a um expoente que é um número público, e após isso ele é novamente elevado a outro expoente que é um número privado. Assim teremos um número público e um número privado. O processo de descriptografia (em que os números primos são novamente gerados) será revertido através de fatoração, que é o inverso da multiplicação.

O RSA foi construído sobre uma das áreas mais clássicas da matemática, a teoria dos números. Ele se baseia na dificuldade em fatorar um número em seus componentes primos (números divisíveis por 1 e por ele mesmo). Todo número inteiro positivo maior que 1 pode ser decomposto de forma única em um produto de números primos, por exemplo, 26 é um produto de 2 * 13, 44 é um produto de 2 * 2 * 11. Apesar de parecer simples fatorar esses números pequenos, a situação fica bastante complexa e demorada quando temos que fatorar números grandes não podendo ser resolvidos em um tempo polinomial determinístico. No RSA a chave pública e a chave privada são geradas com base na multiplicação de dois números primos e o resultado desta multiplicação será público, mas se o número for grande o suficiente, fatorar este número para descobrir os primos que multiplicamos para formá-lo pode demorar anos. Por isso que o RSA é seguro, sendo impossível quebrar a sua criptografia.

O método do RSA se dá primeiramente com a construção de uma tabela atribuindo a cada letra um número. Isto é necessário visto que o RSA codifica somente números. Após isso, escolhemos os números primos e quanto maior for esses números melhor. A RSA Data Security, que é responsável pela padronização do RSA, recomenda que se utilizem chaves de 2048 bits (o que resulta em um número com 617 dígitos) se quisermos garantir que a chave não seja quebrada até pelo menos o ano de 2030. Após a atribuição de números para as letras agora temos que calcular a função "totiente" que diz a quantidade de co-primos de um numero que são menores que ele mesmo. Feito isso, o próximo passo é calcular a chave pública que é onde escolhe-se um número "e" em que 1 < e < função totiente. Com a chave pública em mãos podemos agora cifrar a mensagem aplicando, para cada letra, a fórmula "c = m ^ e mod n", onde "e" é a chave pública e "m" é o valor numérico da letra.

Para exemplificar o funcionamento do algoritmo vamos escolher inicialmente dois números primos quaisquer "P" e "Q". Obviamente que vamos escolher dois números primos pequenos apenas por questão de exemplificação. Portanto, consideramos que "P = 17" e "Q = 11".

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

O próximo passo é definir um número D que tenha a propriedade de ser primo em relação a Z. Podemos escolher qualquer número como, por exemplo, o número "7".

Agora podemos começar o processo de criação da chave pública e da chave privada. Devemos encontrar um número E que satisfaça a propriedade "(E * D) mod Z = 1". Se tomarmos o número "1" e substituindo os valores na fórmula teremos "E = 1 => (1 * 7) mod 160 = 7" que não satisfaz a condição, pois o resultado foi "7". Se tomarmos os números "2", "3" até o "22" nenhum satisfará a condição, mas o número "23" satisfará resultando em "E = 23 => (23 * 7) mod 160 = 1". Outros números também satisfazem essa condição, como "183", "343", "503", etc.

Dessa forma, tomamos como referência "E = 23". Agora podemos definir as chaves de encriptação e desencriptação. Para criptografar utilizamos "E" e "N", esse par de números é utilizado como chave pública. Para descriptografar utilizamos "D" e "N", esse par de números é utilizado como chave privada.

Assim, temos as equações definidas abaixo:
``` 
Texto Criptografado = (Texto Puro ^ E) mod N

Texto Puro = (texto Criptografado ^ D) mod N
``` 

Como um exemplo prático vamos imaginar uma mensagem bastante simples que tem o número "4" no seu corpo e será retornada ao destinatário. Para criptografar essa mensagem teríamos o texto original como sendo "4", o texto criptografado seria "(4 ^ 23) mod 187" que é "70.368.744.177.664 mod 187" resultando em "64".

Para descriptografar destinatário recebe o texto "64". Recebido o texto criptografado e aplicando a fórmula temos que o texto original será "(64 ^ 7) mod 187" ou "4.398.046.511.104 mod 187" que resulta em "4" que é o texto originalmente criado. Como o RSA trabalha com número devemos converter um alfabeto em número, assim a letra A seria 0, B seria 1, C seria 2, e assim por diante.

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

O [JWT (JSON Web Token)](https://jwt.io/) é definido no site oficial na seguinte forma http://jwt.io: "JWT é um padrão aberto que define uma forma compacta e auto-contida para transmitir de forma segura, informações entre duas partes como objeto JSON".

Quando estamos trabalhando com API’s, nós precisamos pensar na segurança no momento no momento de trafegar os dados e principalmente no nível de permissão que cada usuário deverá ter. Existem muitas formas de se fazer isso, mas uma que vem se destacando a cada dia que se passa é o JWT (JSON Web Token), por ser muito seguro e fácil de se implementar. Nas próximas sessões, será abordado a sua teoria com alguns exemplos e no final iremos criar uma aplicação com Node.js para exemplificarmos melhor o seu funcionamento.

Bom, o JWT (JSON Web Token) é um sistema de transferência de dados que pode ser enviado via POST ou em um cabeçalho HTTP (header) de maneira "segura", essa informação é assinada digitalmente por um algoritmo HMAC, ou um par de chaves pública/privada usando RSA. Podemos ver na imagem a baixo um cenário onde será requisitado um token através do Verbo HTTP POST, que irá devolver um token validado para que nas próximas requisições que utilizem os Verbos HTTP possam utilizar.

O JWT é divido em três partes separadas por um "." essas três partes são o Header,Payload e a Signature

### Header

O header é a primeira parte do JWT e ele é divido em duas partes, o algoritmo de codificação e o tipo do token e essas duas partes são encodadas em Base64, ficaria assim:

``` JSON
{
    "alg": "HS256",
    "typ": "JWT"
}
```

A propriedade "alg" define o algoritmo do token que nesse caso é o HMAC SHA256 e a propriedade "typ" é o tipo do token que é o JWT. 

Após ser enconcado em Base64 o header fica assim:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
```

### Payload (Claims)
Os payloads são objetos JSON que contem os claims, nessa parte que nós trabalhamos com os "pedidos", carga de dados ou dados enviados. Existem 3 tipos de claims em Payloads: reserved, public, e private claims.

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
Existem muitas [boas práticas](https://www.crummy.com/writing/speaking/2008-QCon/act3.html) envolvidas ao se construir sistemas que irão expor APIs, algumas relacionadas a arquitetura e outras a segurança

### Fontes e links uteis:
- https://renatogroffe.medium.com/asp-net-core-boas-pr%C3%A1ticas-na-implementa%C3%A7%C3%A3o-de-apis-rest-setembro-2019-1d4f6b6e8352
- https://imasters.com.br/back-end/6-melhores-praticas-para-arquiteturas-baseadas-em-microservices

### APIs de Healthcheck
É um tipo de serviço nos sistemas que expõem APIs capaz de informar se esse serviço está funcionando adequadamente, ou seja, se está capacitado a responder requisições a ele feitas

O Health Checks nada mais é que um middleware que nos fornecem um endpoint configurável que nos retorna o estado atual da aplicação.

#### Fontes e links uteis:
- https://balta.io/blog/aspnet-health-check

### Arquitetura de CircuitBrake
### Caches
### API Gateways/ BFF
### SQL Injections

## [Swagger e OpenAPI](https://swagger.io/docs/specification/about/)
#### Fontes e links uteis:
- https://swagger.io/docs/specification/about/
- https://gr1d.io/2022/04/15/swagger/
- https://medium.com/@ronilsonribeiro/como-interpretar-um-swagger-cdc331b68804

## Outras ferramentas de desenvolvimento de APIs