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
    preco_tipo = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome_tipo


class Turno(models.Model):
    cod_turno = models.AutoField(primary_key=True)
    nome_turno = models.CharField(max_length=10)
    inicio_turno = models.TimeField()
    termino_turno = models.TimeField()

    def __str__(self):
        return self.nome_turno


class Cargos(models.Model):
    cod_cargo = models.AutoField(primary_key=True)
    nome_cargo = models.CharField(max_length=25)
    salario_cargo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome_cargo


class Quartos(models.Model):
    cod_quarto = models.AutoField(primary_key=True)
    tipo_quarto = models.ForeignKey(Tipo_quarto, on_delete=models.PROTECT)
    camas = models.IntegerField()
    disponibilidade = models.BooleanField(default=True)

    def __str__(self):
        return f'Quarto {self.cod_quarto} - {self.tipo_quarto.nome_tipo}'


class Funcionarios(models.Model):
    cod_funcionario = models.AutoField(primary_key=True)
    cod_turno = models.ForeignKey(Turno, on_delete=models.PROTECT)
    cod_cargo = models.ForeignKey(Cargos, on_delete=models.PROTECT)
    nome_funcionario = models.CharField(max_length=50)
    sobrenome_funcionario = models.CharField(max_length=50)
    cpf_funcionario = models.CharField(max_length=11)
    email_funcionario = models.EmailField(max_length=200)
    telefone_funcionario = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.nome_funcionario} {self.sobrenome_funcionario}'


class Servicos(models.Model):
    cod_servico = models.AutoField(primary_key=True)
    cod_funcionario = models.ForeignKey(Funcionarios, on_delete=models.PROTECT)
    nome_servico = models.CharField(max_length=30)
    preco_servico_adicional = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome_servico


class Reserva(models.Model):
    STATUS_CHOICES = [
        ('ativa', 'Ativa'),
        ('cancelada', 'Cancelada'),
        ('finalizada', 'Finalizada'),
    ]
    cod_reserva = models.AutoField(primary_key=True)
    cod_hospede = models.ForeignKey(Hospede, on_delete=models.CASCADE)
    cod_quarto = models.ForeignKey(Quartos, on_delete=models.PROTECT)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f'Reserva {self.cod_reserva} - {self.status}'


class Reserva_Servicos(models.Model):
    cod_servico_acionado = models.AutoField(primary_key=True)
    cod_reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    cod_servico = models.ForeignKey(Servicos, on_delete=models.CASCADE)

    def __str__(self):
        return f'Serviço {self.cod_servico.nome_servico} na Reserva {self.cod_reserva.cod_reserva}'

class Pagamento(models.Model):
    cod_pagamento = models.AutoField(primary_key=True)
    cod_reserva = models.ForeignKey(Reserva, on_delete=models.PROTECT)
    pagamento_final = models.DecimalField(max_digits=10, decimal_places=2)
    pagamento_inicial = models.DecimalField(max_digits=10, decimal_places=2)
    desconto = models.DecimalField(max_digits=10, decimal_places=2)
    efetuado = models.CharField(max_length=10)
    metodo_pagamento = models.CharField(max_length=15)