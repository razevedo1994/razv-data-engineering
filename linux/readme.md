# Comandos Linux

- `pwd`: Exibe o diretorio atual.
- `ls`: Lista os arquivos e diretorios.
- `echo`: Exibe uma mensagem no terminal.
```
echo "Bem vindo" > bemvindo.txt

Direciona a saida do echo em um arquivo.

echo "Bem vindo" >> bemvindo.txt

Concatena uma saida a um arquivo ja existente.
```
- `cat`: Le um arquivo.
```
cat bemvindo.txt
```
- `ls -l`: Mostra informacoes sobre os arquivos e pastas do diretorio atual.
- `ls -la`: Mostra informacoes sobre os arquivos e pastas do diretorio atual, incluindo arquivos e pastas ocultos.
- `man`: Comando de ajuda do Linux. Exibe um manual acerca do comando desejado.
```
man pwd
```
- `whoami`: Exibe o nome do usuario.
- `cd "diretorio"`: Entra em um diretorio.
- `cd ..`: Retorna ao diretorio anterior.
- `mkdir`: Cria um diretorio.
- `rmdir`: Apaga um diretorio. Obs: So apaga diretorios vazios.
- `rm`: Apaga arquivo.
```
Exemplo: rm arquivo.txt
```
- `rm -r`: Apaga um diretorio recursivamente.
- `cp`: Copia um arquivo:
```
cp mensagem.txt bemvindo.txt
```
- `mv`: Move ou renomeia um arquivo:
```
mv mensagem.txt bemvindo2.txt

mv bemvindo2.txt diretorio2/
```
- `ls *`: Aplica o ls em todos aquivos/diretorios do diretorio atual.
- `cp -r`: Copia o diretorio recursivamente.
- `zip -r`: Zipa um diretorio.
```
zip -r work.zip diretorio/
```
- `unzip`: Descompacta aquivo zipado.
```
unzip work.zip
```




