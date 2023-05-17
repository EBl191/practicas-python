from materias_aprobadas import Semester, Basic_subject

first_semester = Semester('first', 3, 18, True)

logic_I = Basic_subject('Lógica I', 'Departamento de Lógica y Filosofía de las ciencias', 'Ricardo Silva', 4)

theorethic_philosophy_I = Basic_subject('Teorética I', 'Departamento de Filosofía Teorética', 'Luz Marina Barreto', 4)

philosophy_of_praxis_I = Basic_subject('Filosofía de la praxis', 'Departamento de Filosofía de la praxis', 'J.R.Herrera', 4)

History_of_philosophy_I = Basic_subject('Historia de la Filosofía I', 'Departamento de Historia de la Filosofía', 'Guadalupe Yanes', 4)


theorethic_philosophy_I.enroll()