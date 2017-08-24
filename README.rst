CUriTools
==============
Uma ferramenta de linha de commando para interagir com o web site `URI`__  online
judge

__ https://www.urionlinejudge.com.br/

Instalação
-----------------
.. code:: python
  
  pip install curitools

Configuração
-----------------

Para usar a ferramenta basta colocar no diretório onde os problemas são
resolvidos um arquivo .uri.settings. O arquivo deve conter duas linhas:

.. code:: python

    user : nome do usuario
    password: senha do usuario


**nunca comite esse arquivo**

Uso
-----------------

Para visualizar as suas ultimas submissões:

.. code:: python

    curitools -r


Para enviar um problema basta usar:

.. code:: python

    curitools -s numero_do_problema


O arquivo para resolver o problema deve ter o nome do problema. 
