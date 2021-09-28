<h1 align="center"> XIoT </h1>


Para acessar o help dp programa digite:


```bash
sudo ./xiot help
```


Existem, por enquanto **duas formas de rodar o XIoT**.

Uma delas, roda somente o **IPv6 sem o Gateway Service**. A outra roda o **XIA + IPv6** com o **Gateway Service** do XIA, que converte XIP para IPv6.


#Para rodar o XIoT é preciso:

1) Clone o diretorio do XIoT:

```bash
https://jira.inatel.br/bitbucket/projects/ILAB/repos/xiot/browse
```



2) Entre na pasta /installation-scripts$ e execute os scripts que nela estão.


Ou seja. na ordem:

```bash
sudo sh install-devel
```

Pode ser que de algum erro na instalação do **gcc++-7**. Veja na Internet como contornar, mas é preciso que ele esteja instalado com sucesso para que o xia-compile na maquina local. 


```bash
sudo sh install-docker	
sudo sh install-xia
sudo sh install-cooja
```


Verifique se tudo compilou direito. O Wireshark é opcional.


3) Crie as imagens usadas pelo programa.


Para isso, entre na pasta **/docker** e rode o programa:

```bash
sudo sh make-images
```


Outra forma de fazer a mesma coisa é rodar na pasta **/xiot**:

```bash
sudo ./xiot build
```


Observe se ocorre algum erro ao longo da criação das imagens, principalmente no que tange a compilação do xia-core na imagem xia-base. Observe que o que é feito aqui é similiar a instalação loca, só que dentro dos containers.

Se houver erro, pode ser necessário editar os arquivos Dockerfile dentro de cada pasta individual. Nelas, também existem Init que são executados na construção das imagens.


**Para saber se deu certo, digite**:


```bash
sudo docker images
```


As imagens que começam com xia, são do cenário hibrido (XIA + IPv6 com Gateway Service). Já as que começam com ipv6, são puramente IPv6, sem XIA.

Observe ainda que tanto as imagens do XIA híbrido, quanto do puro IPv6 são criadas a partir da imagem que termina com -base no nome.



4) Execute o xiot, como por exemplo:


```bash
sudo ./xiot start
```


Ou ainda, outro exemplo:


```bash
sudo ./xiot -a xia -d 30 -r 10000 -l 8 -g 1 -G 1 -c 1 -C 1 start
```


A cada teste, o XIoT cria uma pasta com o nome do experimento na pasta **/log**. O nome da pasta já indica a configuração do experimento realizado.


5) Por fim, podemos **acessar os resultados** sumarizados dos experimentos **utilize** os **scripts** disponibilizados no **diretório collectors**:


Para **XIA + IPv6**:


```bash
sudo ./collector /home/user/workspace/xiot/logs/host_name/
```


Para **IPV6 puro**:

```bash
sudo ./ipv6-collector /home/user/workspace/xiot/logs/host_name/
```

Versão disponível para **Python3.6** (válida para XIA + IPv6 ou IPv6 puro):

#Requisitos:

- Python > 3.6
- [pandas 1.2.3](https://pandas.pydata.org)
- [xlsxwriter 1.3.7](https://pypi.org/project/XlsxWriter/)

```bash
sudo ./collector_Python36 <path_to_results> <arquitetura> 
```

O diretorio acima é só um exmeplo. Abra a pasta /xiot/logs e veja o que tem lá. Use o caminho até um pasta interna a essa pasta /xiot/logs/. É nela que estarão os resultados da execução.


Se ocorrer erro na execução do comando, pode ser que alguma pasta de resultado tenha arquivos corrompidos, devido a interrupção de execução de algum cenário.







