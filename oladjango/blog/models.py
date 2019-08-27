from django.db import models

# Create your models here.
class Post(models.Model):
    autor = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    resumo = models.CharField(max_length=50)

    def __str__(self):
        return self.autor

class Produto(models.Model):        
    descricao = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    fornecedor = models.ForeignKey('Fornecedor', on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao

class Fornecedor(models.Model):
    nome = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=18)
    endereco = models.CharField(max_length=50)
 #   cidade = models.ForeignKey('Cidade', on_delete=models.CASCADE, null=True)

    def __str__(self) :
        return self.nome
#criar classe de fornecedor contendo nome, cnpj e endereco

#criar cadastro de cidade e vincular ao fornecedor
