# Table of Contents
1. [Sistemas Distribuídos](#sistemas-distribudos)
	1. [Desafios dos sistemas distrubuídos](#desafios-dos-sistemas-distrubudos)
		1. [O que é um sistema distribuído?](#o-que-um-sistema-distribudo)
		2. [Características de um sistema distribuído](#caractersticas-de-um-sistema-distribudo)
		3. [Conceitos importantes ao se falar de sistemas computacionais distribuídos](#conceitos-importantes-ao-se-falar-de-sistemas-computacionais-distribudos)
		4. [SOA - Orientação a serviços:](#soa--orientao-a-servios)

# Sistemas Distribuídos
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