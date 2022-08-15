# Table of Contents
1. [JWT](#jwt)
    1. [Header](#header)
    2. [Payload (Claims)](#payload-claims)
    3. [Signature](#signature)
    4. [Fontes e links uteis](#fontes-e-links-uteis)

# JWT

O [JWT (JSON Web Token)](https://jwt.io/) é definido no site oficial na seguinte forma http://jwt.io: "JWT é um padrão aberto que define uma forma compacta e auto-contida para transmitir de forma segura, informações entre duas partes como objeto JSON".

Quando estamos trabalhando com API’s, nós precisamos pensar na segurança no momento no momento de trafegar os dados e principalmente no nível de permissão que cada usuário deverá ter. Existem muitas formas de se fazer isso, mas uma que vem se destacando a cada dia que se passa é o JWT (JSON Web Token), por ser muito seguro e fácil de se implementar. Nas próximas sessões, será abordado a sua teoria com alguns exemplos e no final iremos criar uma aplicação com Node.js para exemplificarmos melhor o seu funcionamento.

Bom, o JWT (JSON Web Token) é um sistema de transferência de dados que pode ser enviado via POST ou em um cabeçalho HTTP (header) de maneira "segura", essa informação é assinada digitalmente por um algoritmo HMAC, ou um par de chaves pública/privada usando RSA. Podemos ver na imagem a baixo um cenário onde será requisitado um token através do Verbo HTTP POST, que irá devolver um token validado para que nas próximas requisições que utilizem os Verbos HTTP possam utilizar.

O JWT é divido em três partes separadas por um "." essas três partes são o Header,Payload e a Signature

## Header

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

## Payload (Claims)
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

## Signature

Por último temos signature que é o header e payload codificado com o algoritmo do header junto com uma palavra segredo que é usada pra codificar e não deve ser compartilhada com ninguém.

Após ser enconcado em Base64 ficaria assim:

```
IShPdPgMqjygLcv6FpePbFuRLJHBTdeKSNDQIpR-X2E

``` 

Então nosso token completo fica assim:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJub21lIjoiRnVsYW5vIiwiYWRtaW4iOnRydWV9.IShPdPgMqjygLcv6FpePbFuRLJHBTdeKSNDQIpR-X2E 
```

## Fontes e links uteis
- https://jwt.io/
- https://www.rfc-editor.org/rfc/rfc7519
- https://www.devmedia.com.br/como-o-jwt-funciona/40265
- https://auth0.com/blog/how-to-handle-jwt-in-python/
- https://pyjwt.readthedocs.io/en/latest/usage.html
- https://imasters.com.br/desenvolvimento/json-web-token-conhecendo-o-jwt-na-teoria-e-na-pratica