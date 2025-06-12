from django.db import models





class Hospede(models.Model):
    cod_hospede = models.AutoField(primary_key=True)
    nome_hospede = models.CharField(max_length=50)
    sobrenome_hospede = models.CharField(max_length=50)
    email_hospede = models.EmailField(max_length=200)
    senha_hospede = models.CharField(max_length=50)
    cpf_hospede = models.CharField(max_length=11)
    telefone_hospede = models.CharField(max_length=15)
    data_nascimento = models.DateField()

    def __str__(self):
        return f'{self.nome_hospede} {self.sobrenome_hospede}'

class Tipo_quarto(models.Model):
    cod_tipo_quarto = models.AutoField(primary_key=True)
    nome_tipo = models.CharField(max_length=20)
    preco_tipo = models.DecimalField()

    def __str__(self):
        return self.nome_tipo


class Turno(models.Model):
    cod_turno = models.AutoField(primary_key=True)
    nome_turno = models.CharField(max_length=10)
    inicio_turno = models.DateTimeField()
    termino_turno = models.DateTimeField()

    def __str__(self):
        return self.nome_turno


class Cargos(models.Model):
    cod_cargo = models.AutoField(primary_key=True)
    nome_cargo = models.CharField(max_length=25)
    salario_cargo = models.DecimalField(max_digits=6 ,decimal_places=2)

    def __str__(self):
        return self.nome_cargo


class Quartos(models.Model):
    cod_quarto = models.AutoField(primary_key=True)
    tipo_quarto = models.ForeignKey(Tipo_quarto, on_delete=models.PROTECT)
    camas = models.IntegerField()
    disponibilidade = models.BinaryField()

    def __str__(self):
        return f'{self.cod_quarto} {self.tipo_quarto}'


class Funcionarios(models.Model):
    cod_funcionario = models.AutoField(primary_key=True)
    cod_turno = models.ForeignKey(Turno, on_delete=models.PROTECT)
    cod_cargo = models.ForeignKey(Cargos, on_delete=True)
    nome_funcionario = models.CharField(max_length=50)
    sobrenome_funcionario = models.CharField(max_length=50)
    cpf_funcionario = models.CharField(max_length=11)
    email_funcionario = models.EmailField(max_length=200)
    telefone_funcionario = models.CharField(15)

    def __str__(self):
        return f'{self.nome_funcionario} {self.sobrenome_funcionario}'


class Estado(models.Model):
    cod_servico = models.
    cod_funcionario = models.
    nome_servico = models.
    preco_servico_adicional = models.

    def __str__(self):
        return self.nome


class Estado(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return self.nome


class Estado(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return self.nome


class Estado(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return self.nome
        
class Reserva(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return self.nome