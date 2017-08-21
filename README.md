# CUriTools
Uma ferramenta de linha de commando para interagir com o web site URI online
judge(https://www.urionlinejudge.com.br/)

## Configuracão

Para usar a ferramenta basta colocar no diretório onde os problemas são
resolvidos um arquivo .uri.settings. O arquivo deve conter duas linhas
    user : {nome do usuario} 
    password {senha do usuario}

ps: nunca commite esse arquivo.

## Uso

Para visualizar as suas ultimas submissões:
    curitools -r

Para enviar um problema basta usar:
    curitools -s numero_do_problema

O arquivo para resolver o problema deve ter o nome do problema. 
