# CUriTools [![Build Status](https://travis-ci.org/gutorc92/curitools.svg?branch=master)](https://travis-ci.org/gutorc92/curitools)
Uma ferramenta de linha de commando para interagir com o web site [URI](https://www.urionlinejudge.com.br/) online
judge

## Instalação

```
    pip install curitools 
```
## Configuração

Para usar a ferramenta basta colocar no diretório home do usuário 
um arquivo .uri.settings. O arquivo deve conter duas linhas:

```
    user: nome do usuario
    password: senha do usuario
```

Substitua nome do usuário pelo seu email do Uri e senha do usuario por 
sua senha em formato de texto. 

ps: nunca comite esse arquivo.

## Uso

Para visualizar as suas ultimas submissões:

```
    curitools -r
```

Para enviar um problema basta usar:

```
    curitools -s numero_do_problema
```

O arquivo em que sua solucão foi feita deve ter o numero do problema como nome. 
Por exemplo, você deseja submter o problema 1010 se sua solucao for desenvolvida
em c++ o ser arquivo deve se chamar 1010.cpp.


