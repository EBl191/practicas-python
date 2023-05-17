"""Departamentos: """
teoretica = []
historia = []
logica = []
praxis = []
departamentos = [teoretica, historia, praxis, logica]

"""Asignaturas básicas: """
asignaturas_basicas = []
cr_asignaturas_basicas = 32

"""Autores: """
autores = []
cr_autores = 30

"""Electivas: """
cr_cursos_electivos = 16
cr_seminarios_electivos = 24
electivas_filosoficas = [cr_cursos_electivos, cr_seminarios_electivos]
cr_electivas_filosoficas = cr_cursos_electivos + cr_seminarios_electivos

electivas_extrafilosoficas = []
cr_electivas_extrafilosoficas = 30

""" Idiomas modernos: """
idiomas_modernos = []
cr_idiomas_modernos = 6


""" Tesis: """
trabajo_licenciatura = []
cr_trabajo_licenciatura = 12

"""Asignaturas y créditos: """
asignaturas = [asignaturas_basicas, autores, electivas_filosoficas, electivas_extrafilosoficas,idiomas_modernos, trabajo_licenciatura]

creditos_asignaturas = [cr_asignaturas_basicas, cr_autores, cr_electivas_filosoficas, cr_electivas_extrafilosoficas, cr_idiomas_modernos, cr_trabajo_licenciatura]

creditos_licenciatura = 132

"""Asignaturas aprobadas primer semestre: """

teoretica_I = {
    'asignatura': "Teorética I",
    'créditos' : 4,
    'profesor/a' : "Luz Marina Barreto",
    'departamento' : "Teorética"
}

teoretica.append(teoretica_I)

praxis_I = {
    'asignatura': "Praxis I",
    'créditos' : 4,
    'profesor/a' : "Rafael Herrera",
    'departamento' : "praxis"
}

praxis.append(praxis_I)

logica_I = {
    'asignatura': "Lógica I",
    'créditos' : 4,
    'profesor/a' : "Ricardo Silva",
    'departamento' : "logica"
}

logica.append(logica_I)

historia_I = {
    'asignatura': "Historia I",
    'créditos' : 4,
    'profesor/a' : "Guadalupa Yanes",
    'departamento' : "historia"
}

historia.append(historia_I)

primer_semestre = [
    teoretica_I,
    praxis_I,
    logica_I,
    historia_I
]

