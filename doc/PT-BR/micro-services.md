# Table of Contents
1. [Micro Serviços](#micro-servios)
	1. [Qual a relação entre as APIs e os microserviços?](#qual-a-relao-entre-as-apis-e-os-microservios)
		1. [O que são Microserviços?](#o-que-so-microservios)
		2. [Componentes do Microserviços](#componentes-do-microservios)
		3. [Tipos de Microserviços](#tipos-de-microservios)
	2. [Os microserviços são RESTful?](#os-microservios-so-restful)
		1. [Como os Microserviços funcionam?](#como-os-microservios-funcionam)
		2. [Como as APIs funcionam?](#como-as-apis-funcionam)
		3. [Microserviços vs API: Benefícios de cada um deles](#microservios-vs-api-benefcios-de-cada-um-deles)
		4. [Benefícios do uso de APIs](#benefcios-do-uso-de-apis)
		5. [Microserviços e API podem trabalhando juntos](#microservios-e-api-podem-trabalhando-juntos)
		6. [Fontes e links uteis:](#fontes-e-links-uteis)

# Micro Serviços
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