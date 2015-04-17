dojudge
=======

Juiz de problemas de maratonas.

### Rodando

Tem um *Dockerfile* pra ajudar :)

```shellscript
$ docker build -t dojudge .
$ docker run --name judge1 -p 9090:9090 dojudge
```

### Exemplo de Uso

A aplicação recebe o código e as informações do problema através de uma
requisição HTTP POST. Compila, executa e retorna o status da execução.

```shellscript
$ cat /tmp/abacate.cpp
#include <iostream>

using namespace std;

int main () {
    cout << "teste" << endl;
    return 0;
}
$ curl -X POST --data-binary @/tmp/abacate.cpp -H 'X-Judge-Problem: 1' -H 'X-Judge-Lang: c++' http://localhost:9090
```
