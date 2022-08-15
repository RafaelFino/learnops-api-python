# Json
## Mas o que é Json
[JSON]((https://jsonapi.org/)?) é basicamente um formato leve de troca de informações/dados entre sistemas. Mas JSON significa JavaScript Object Notation, ou seja, só posso usar com JavaScript correto? Na verdade não e alguns ainda caem nesta armadilha.

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

