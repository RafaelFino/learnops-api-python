# Segurança
## Autenticações
### O que é um token de autenticação
Chamamos de [token de autenticação](https://pt.wikipedia.org/wiki/Token_(chave_eletr%C3%B4nica)#:~:text=Token%20%C3%A9%20um%20dispositivo%20eletr%C3%B4nico,conectado%20a%20uma%20porta%20USB.) um conjunto de caracteres, chave que indentifica uma operação. Por exemplo:

Imagine uma API que tem um nível de proteção que precisa de usuário e senha (chamamos também de credênciais) para liberar acesso aos seus serviços, a cada requisição o cliente iria precisar enviar esses dados e a API validar se essas credênciais possuem acesso a esses serviços. 

Parece custoso e pouco seguro, certo? Nesses casos podemos ter um serviço responsável por validar se um usuário e senha são válidos e gerar um **token**, que pode identificar esse usuário nas próximas requisições.

Nesse caso, na autenticação por token, o usuário insere login e senha na plataforma, o que gera um token (que podemos também chamar de certificado digital) que o permite navegar pelos recursos do seu interesse, dentro de um prazo determinado, sem a necessidade de utilizar os dados do login novamente.

#### Fontes e links uteis:
- https://pt.wikipedia.org/wiki/Token_(inform%C3%A1tica)
- https://blog.engdb.com.br/autenticacao-por-token/
- https://www.linkedin.com/pulse/autentica%C3%A7%C3%A3o-baseada-em-token-uma-aplica%C3%A7%C3%A3o-rest-tarcisio-carvalho/?originalSubdomain=pt

### Criptografias
Através da [criptografia](https://en.wikipedia.org/wiki/Cryptography) obtemos diversas propriedades importantes como a confidencialidade (sigilo da informação), integridade (garantia que a mensagem não foi alterada), autenticidade (quem foi a autor da mensagem) e irretratabilidade ou não repúdio (capacidade de não negar a construção da mensagem). Temos ainda que a criptografia Simétrica garante a confidencialidade e a integridade, enquanto que a criptografia Assimétrica garante a confidencialidade, integridade, autenticidade e a irretratabilidade ou não repúdio.

Assim sendo, podemos classificar os algoritmos através do número de chaves (simétrico ou assimétrico). Nos algoritmos simétricos uma chave é usada tanto para criptografar quanto para descriptografar (podemos ter mais que uma se a segunda for facilmente derivada da primeira), enquanto que nos algoritmos assimétricos temos mais que uma chave e ambas são completamente independentes uma das outras.

Outra classificação para os algoritmos é em relação aos métodos de operação que podem ser dois: de substituição e de transposição. Mais uma importante classificação é em relação ao modo de processamento que pode ser: os cifradores de bloco e cifradores de fluxo. Cifradores de Bloco operam sobre 8 bits ou 16 bits e funcionam com complementos para que todos blocos tenham o mesmo tamanho. Cifradores de Fluxo é onde a cifragem ocorre bit a bit continuo. Essas classificações são importantes e nos permitem melhor organizar cada algoritmo criptográfico.

Nessa importante área de segurança da informação ainda temos duas ciências muito estudas: a Criptologia que se divide em Criptografia e que tem como foco o estudo de como tornar algo legível em ilegível e a Criptoanálise que estuda a arte de quebrar textos cifrados. Por fim, temos a Estagonologia que se divide em Esteganografia que estuda a ocultação da informação e Esteganoanálise que é a arte de revelar informações ocultas.

A criptografia através de cifras ocorre com a cifração da mensagem original através de operações de transposição e substituição de seus caracteres, resultando numa mensagem cifrada. Para decifração basta aplicar o processo inverso. Temos dois tipos de cifras, as cifras mono alfabéticas e as cifras poli alfabéticas. As cifras mono alfabéticas são compostas pela mais famosa de todas que é conhecida como Cifra de César onde basicamente cada letra do alfabeto é deslocada da sua posição um número fixo de lugares k, tal que 1<=k<=25 (número de letras que compõem o alfabeto). Originalmente a cifra anda três posições. Portanto, por exemplo, a palavra "senha" seria cifrada como "vhqkd", assim "s" andou três posições e foi para o "v", "e" andou mais três posições e foi para o "h" e assim por diante. A Cifra de César ainda é utilizada em algumas aplicações mais simples que necessitam de alguma criptografia. Por sua vez, as cifras poli alfabéticas são compostas pela cifra de Vigenère que consiste no uso de várias cifras de César em sequencia, com diferentes valores de deslocamento ditados por uma palavra-chave.

Os sistemas criptográficos são compostos por dois tipos: Simétricos e Assimétricos. Na próxima seção veremos mais sobre a criptografia Assimétrica estudando seus conceitos, funcionamento, algoritmos e como podemos aplica-los na prática utilizando a linguagem de programação Java que suporta amplamente a criptografia Assimétrica.

#### Chaves simétricas
O ciframento de uma mensagem (processo em que um conteúdo é criptografado) é baseado em 2 componentes:

- um algoritmo;
- uma chave de segurança.

##### Algoritmo
O algoritmo trabalha junto com a chave, de forma que eles tornam um conteúdo sigiloso com um conjunto único de regras.

##### A Chave (senha)
A [criptografia simétrica](https://academy.bit2me.com/pt/que-es-criptografia-simetrica/) faz uso de uma única chave, que é compartilhada entre o emissor e o destinatário de um conteúdo. Essa chave é uma cadeia própria de bits, que vai definir a forma como o algoritmo vai cifrar um conteúdo.

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

#### Chaves assimétricas (chaves publica e privada)
Na [criptografia Assimétrica](https://academy.bit2me.com/pt/o-que-%C3%A9-criptografia-assim%C3%A9trica/) (ou criptografia de chave pública) temos que a chave de cifração é diferente da chave de decifração e uma não pode ser facilmente gerada a partir da outra. Basicamente temos que no processo de encriptação utilizaremos uma chave "k1" em cima da mensagem em texto puro que então irá gerar um texto cifrado. Após isso, no processo de descriptografia usaremos outra chave "k2" em cima do texto cifrado e teremos como resposta de volta o texto claro.

Basicamente na criptografia assimétrica temos que a chave pública pode ser conhecida por todos e é utilizada para cifrar o texto claro. Por sua vez, a chave privada deve permanecer secreta e é utilizada para decifrar o texto cifrado. Esse processo nos garante a confidencialidade da informação. Porém, também é possível utilizar a chave privada para cifrar o texto claro e a respectiva chave pública para decifrar a mensagem criptografada. Neste caso, busca-se garantir a autenticidade. É caso típico de assinaturas digitais.

Para entendermos melhor como funciona esse processo imagina que eu queira enviar uma mensagem para o meu amigo João. Neste caso, devemos cifrar a mensagem com a chave pública de João. Ao receber a mensagem cifrada, João decifra a mensagem com a sua chave privada. Podemos notar que a confidencialidade está garantida, pois somente a chave privada de João pode decifrar a mensagem criptografada e somente ele possui essa chave, não a distribuindo para ninguém. Outra forma de utilizar a criptografia assimétrica é garantindo a autenticidade. Exemplificando o processo agora podemos imaginar que eu cifre a mensagem utilizando a minha chave privada e envie essa mensagem para João, podemos verificar que agora não foi utilizada a chave pública de João e sim a minha própria chave privada que somente eu e mais ninguém tem acesso. Como somente a minha chave pública pode decifrar a mensagem João tem certeza que quem enviou a mensagem foi eu.

Nesta criptografia temos também um alto custo computacional para criptografar e descriptografar. Na maioria dos casos o tamanho da chave é grande, maior que as utilizadas na criptografia simétrica, mas nem sempre isso é verdade, depende do algoritmo utilizado.

Portanto, uma chave pública é disponibilizada gratuitamente a qualquer pessoa que queira enviar uma mensagem. Uma segunda chave privada é mantida em sigilo, para que somente a própria pessoa a tenha. Isso significa que não precisaremos se preocupar com o envio das chaves públicas na Internet. Um problema com a criptografia assimétrica, no entanto, é que ela é mais lenta do que a criptografia simétrica. Ela requer muito mais capacidade de processamento para criptografar e descriptografar o conteúdo da mensagem.

Existem diferentes algoritmos assimétricos sendo uns dos mais conhecidos o RSA que tem esse nome devido aos seus desenvolvedores Rivest, Shamir, e Adleman. Este algoritmo é amplamente utilizado nos navegadores, para sites seguros e para criptografar e-mails.

##### RSA
O [RSA](https://www.rfc-editor.org/rfc/rfc8017.html) é o método de criptografia mais utilizado no mundo. No RSA utilizamos duas chaves, uma chave para encriptação e outra para decriptação. Ele resolve o problema de distribuição de chaves da criptografia simétrica usando envelopamento digital e a segurança é baseada na fatoração de números extensos. Quanto maior a chave maior a segurança, porém o processamento também é maior.

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
