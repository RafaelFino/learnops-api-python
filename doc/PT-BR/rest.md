# Table of Contents
1. [REST](#rest)
	1. [Os Verbos](#os-verbos)
		1. [Cuidado com a Semântica de seus serviços](#cuidado-com-a-semntica-de-seus-servios)
		2. [Aplique corretamente o HTTP Status Code](#aplique-corretamente-o-http-status-code)
		3. [Respostas de erros padrões](#respostas-de-erros-padres)
		4. [Versionamento de API](#versionamento-de-api)
		5. [Algumas dicas de segurança na construção de APIs](#algumas-dicas-de-segurana-na-construo-de-apis)
		6. [Fontes e links uteis:](#fontes-e-links-uteis)

# REST
O protocolo HTTP define um conjunto de métodos de requisição responsáveis por indicar a ação a ser executada para um dado recurso. Embora esses métodos possam ser descritos como substantivos, eles também são comumente referenciados como HTTP Verbs (Verbos HTTP). Cada um deles implementa uma semântica diferente, mas alguns recursos são compartilhados por um grupo deles, como por exemplo, qualquer método de requisição pode ser do tipo safe, idempotent ou cacheable.

- API [REST]((https://standards.rest/)) são projetadas para recursos, que tratam de qualquer tipo de objeto, dados ou serviço que possa ser acessado pelo cliente;
- Um recurso tem um identificador, o qual se trata de um URI que identifica exclusivamente esse recurso;
- Os clientes interagem com um serviço por meio da troca de representações de recursos (JSON ou XML)

Veja mais no [site do padrão](https://standards.rest/)

## Os Verbos
Tanto GET como POST na verdade são [métodos HTTP](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Methods), definidos pela [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html#name-methods). Eles indicam para o servidor qual a ação que o cliente deseja realizar. Quando realizamos uma requisição obrigatoriamente precisamos informar um método.

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
