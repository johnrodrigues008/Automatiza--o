# Automatização de backups

### Descrição:

```
      Esse codigo tem como objetivo efetuar backups de pastas fazendo tratativas de erros de acordo com os niveis de pastas, esse formato é de um backup incremental então ele efetua o backup geral da pasta é depois quando é rodado novamente ele atualiza o codigo, caso exclua um arquivo da "pasta origim ou pasta a ser clonada" ele automaticamente exclui o arquivo na pasta clonada removendo lixos e alterações removidas.
```

### Observações:

      Para utilizar o codigo é necessario que atualize o caminho das pastas que estão entre parenteses:

```
      src_folder = r'C:\Users\John Rodrigues\Desktop\pasta1'
      dst_folder = r'C:\Users\John Rodrigues\Desktop\pasta2'
```

