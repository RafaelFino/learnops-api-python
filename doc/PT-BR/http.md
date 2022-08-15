# Table of Contents
1. [HTTP](#http)
	1. [Entendendo APIs](#entendendo-apis)
		1. [O que é HTTP?](#o-que-http)
		2. [O que é Request?](#o-que-request)
		3. [O que é Response?](#o-que-response)
		4. [O que é 200, 404, 301 e outros números? Esses são os HTTP Status Code?](#o-que-200-404-301-e-outros-nmeros-esses-so-os-http-status-code)
		5. [Lista com os principais códigos de retorno](#lista-com-os-principais-cdigos-de-retorno)
		6. [Estrutura](#estrutura)

# HTTP
## Entendendo APIs
### O que é HTTP?
O [HTTP]( https://www.rfc-editor.org/rfc/rfc9110.html) é um protocolo de comunicação. Através dele o cliente e o servidor conseguem se comunicar, seguindo um conjunto de regras bem definidas (por isso chamamos de protocolo). Por exemplo, se estivermos falando de uma aplicação web, o cliente é o navegador, ele envia um pedido para o servidor web usando o protocolo HTTP, com base nesse pedido, se tudo estiver correto, o servidor responde também usando o mesmo protocolo o conteúdo solicitado.

Veja a especificação completa da [RFC HTTP]( https://www.rfc-editor.org/rfc/rfc9110.html) para maiores detalhes

### O que é Request?
A [Request](https://www.rfc-editor.org/rfc/rfc2616.html#section-5) ou requisição traduzindo diretamente para português, é o pedido que um cliente realiza a nosso servidor. Esse pedido contém uma série de dados que são usados para descrever exatamente o que o cliente precisa. Vamos pensar que um cliente precisa cadastrar um novo produto, ele deve passar todos os dados necessários para o cadastro acontecer de maneira correta, inclusive os dados que foram digitados pelo usuário em um formulário, no caso de uma aplicação web. No navegador toda vez que trocamos de página ou apertamos enter na barra de endereço uma nova request é feita. Independente se estamos apenas pedindo a exibição de uma página, cadastrando um novo recurso, atualizando ou excluindo.

### O que é Response?
Vimos que o cliente envia uma Request (requisição) ao servidor. Essa requisição possui todas as informações acerca do que o cliente espera receber de volta. O servidor web ao receber essas informações precisa enviar uma resposta ao cliente, nesse ponto entra a Response. A [Response](https://datatracker.ietf.org/doc/html/rfc8246) (resposta) nada mais é do que a resposta que o servidor envia ao cliente. Essa resposta pode conter os dados que realmente o cliente esperava receber ou uma resposta informando que alguma coisa deu errado.

### O que é 200, 404, 301 e outros números? Esses são os HTTP Status Code?
Esses números são os chamados [códigos HTTP](https://datatracker.ietf.org/doc/html/rfc6585). Quando o cliente faz uma requisição ele espera uma resposta. O servidor pode realmente responder o que o cliente esperava ou devolver outra informação, justamente nesse ponto entram os códigos HTTP. O servidor utiliza um código desse na resposta para indicar o que aconteceu.

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
