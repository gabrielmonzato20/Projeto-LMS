from django.db import models

from django.db import models
class Aluno(models.Model):
    def save(self):
     	if self.email == "":
     		self.email =  'email nao fornecido'
     	if self.login=='':
     		raise Exception('')
     	if len(Aluno.objects.filter(login=self.login))>0:
     		raise Exception('')
     	if len(Professor.objects.filter(login=self.login)) >0  or len(Aluno.objects.filter(login=self.login)) > 0:
     		raise Exception("")
     	super(Aluno,self).save()
    nome = models.TextField(max_length=255)
    email =models.TextField(max_length=255)
    celular = models.TextField(max_length=20)
    login = models.TextField(max_length=20)
    senha = models.TextField(max_length=20)

class Professor(models.Model):
	def __str__(self):
		return self.nome + self.email
	def save(self):
		if self.login == "":
			raise Exception('')
		if self.email == "":
			self.email = 'email nao fornecido'
		if len(Professor.objects.filter(login=self.login).exclude(id=self.id)) >= 1:
			raise Exception("")
		if len(Aluno.objects.filter(login=self.login))!=0:
			raise Exception("")
		super(Professor,self).save()
	nome = models.TextField(max_length=255)
	email = models.TextField(max_length=255)
	celular = models.TextField(max_length=20)
	login = models.TextField(max_length=20)
	senha = models.TextField(max_length=20)
class Disciplina(models.Model):
	def __str__(self):
		return self.ementa + " "+self.nome
	def save(self):
		if len(Disciplina.objects.filter(nome = self.nome)) >=1:
			raise Exception('')

		super(Disciplina,self).save()
	nome = models.TextField(max_length=50)
	ementa = models.TextField(max_length=5000)
class DisciplinaOfertada(models.Model):
	def __str__(self):
		return self.curso
	def save(self):
		if self.curso not in ['ADS', 'SI','BD']:
			raise Exception('')
		if len(DisciplinaOfertada.objects.filter(ano=self.ano ,semestre=self.semestre, turma=self.turma, curso=self.curso , disciplina=self.disciplina)) >=1:
			raise Exception("")
		if len(Professor.objects.filter(id=self.professor))<1:
			raise Exception("")
		if len(Disciplina.objects.filter(id=self.disciplina))<1:
			raise Exception("")
		super(DisciplinaOfertada,self).save()



	curso = models.TextField(max_length=255)
	turma = models.TextField(max_length=5)
	ano = models.IntegerField()
	semestre = models.IntegerField()
	professor = models.IntegerField()
	disciplina = models.IntegerField()
class Matricula(models.Model):
    def save(self):
        if len(Matricula.objects.all())>=3:
            raise Exception("")

        disciplina_matricula = self.ofertada_para_disciplina(self.disciplinaOfertada)
        disciplinas_aluno = []
        matriculas_aluno = Matricula.objects.filter(aluno=self.aluno)
        for matricula in matriculas_aluno:
            disciplinas_aluno.append(self.ofertada_para_disciplina(matricula.disiplinaOfertada))

        if disciplina_matricula in disciplinas_aluno:
            raise Exception('')

        #if len(DisciplinaOfertada.objects.filter(disciplina = self.disciplina_para_ofertada(disciplinaOfertada) )) >1:
        #    raise Exception('')

        super().save()
    aluno = models.IntegerField(null=True)
    disiplinaOfertada=models.IntegerField(null=True)



    def ofertada_para_disciplina(self,disciplinaOfertadaId):
        disciplinasOfertadas = DisciplinaOfertada.objects.filter(id=disciplinaOfertadaId)
        disciplinaOfertada = disciplinasOfertadas[0]
        nro_disciplina = disciplinaOfertada.disciplina
        return nro_disciplina
    '''erro null    aluno = models.IntegerField()
    disiplinaOfertada=models.IntegerField() '''
''' if Matricula.objects.filter(aluno=self.aluno)) len(DisciplinaOfertada.objects.filter(id=self.disiplinaOfertada)[0].disciplina):'''
