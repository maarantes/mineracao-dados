import pandas as pd
import random

df_cursos = pd.DataFrame({
    "id_curso": [1, 2, 3],
    "nome_curso": ["Ciência da Computação", "Engenharia Civil", "Administração"]
})

df_disciplinas = pd.DataFrame({
    "id_disciplina": [101, 102, 103, 104, 105],
    "nome_disciplina": ["Algoritmos", "Cálculo I", "Estruturas", "Gestão", "Marketing"],
    "id_curso": [1, 1, 2, 3, 3]
})

df_professores = pd.DataFrame({
    "id_professor": [1, 2, 3, 4],
    "nome_professor": ["Dr. Silva", "Dra. Souza", "Dr. Oliveira", "Dra. Lima"]
})

df_alunos = pd.DataFrame({
    "id_aluno": range(1, 11),
    "nome_aluno": [f"Aluno {i}" for i in range(1, 11)],
    "id_curso": [random.randint(1, 3) for _ in range(10)]
})

df_matriculas = pd.DataFrame({
    "id_matricula": range(1, 31),
    "id_aluno": [random.randint(1, 10) for _ in range(30)],
    "id_disciplina": [random.randint(101, 105) for _ in range(30)],
    "id_professor": [random.randint(1, 4) for _ in range(30)]
})

df_cursos.to_csv("cursos.csv", index=False)
df_disciplinas.to_csv("disciplinas.csv", index=False)
df_professores.to_csv("professores.csv", index=False)
df_alunos.to_csv("alunos.csv", index=False)
df_matriculas.to_csv("matriculas.csv", index=False)

print("Arquivos CSV gerados com sucesso!")