# =============================================
# SISTEMA DE ACOMPANHAMENTO ESCOLAR
# Cadastro de aluno, disciplina e notas
# Cálculo automático da média e do resultado
# =============================================

import os

os.system("cls" if os.name == "nt" else "clear")

# -----------------------------
# CONFIGURAÇÃO
# -----------------------------

MEDIA_MINIMA = 6.0

# -----------------------------
# ENTRADA DE DADOS
# -----------------------------

print("=" * 50)
print("SISTEMA DE ACOMPANHAMENTO ESCOLAR")
print("=" * 50)

nome_aluno = input("Digite o nome do aluno: ").strip()
cpf_aluno = input("Digite o CPF do aluno (xxx.xxx.xxx-xx): ").strip()
disciplina = input("Digite o nome da matéria: ").strip()

# -----------------------------
# LANÇAMENTO DAS NOTAS
# -----------------------------

notas = []

quantidade = int(input("Quantas notas deseja lançar? "))

for i in range(quantidade):
    while True:
        try:
            nota = float(
                input(f"Digite a nota {i + 1} (0 a 10): ")
                .replace(",", ".")
            )

            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("Erro: a nota deve estar entre 0 e 10.")

        except ValueError:
            print("Digite uma nota válida.")

# -----------------------------
# CÁLCULO DA MÉDIA
# -----------------------------

if len(notas) > 0:

    media = sum(notas) / len(notas)

    # -----------------------------
    # RESULTADO
    # -----------------------------

    if media >= MEDIA_MINIMA:
        resultado = "APROVADO"
    else:
        resultado = "REPROVADO"

    # -----------------------------
    # BOLETIM DO ALUNO
    # -----------------------------

    print("\n" + "=" * 50)
    print("BOLETIM ESCOLAR")
    print("=" * 50)

    print(f"Aluno: {nome_aluno}")
    print(f"CPF: {cpf_aluno}")
    print(f"Matéria: {disciplina}")

    print("-" * 50)

    for i, nota in enumerate(notas, start=1):
        print(f"Nota {i}: {nota:.1f}")

    print("-" * 50)

    print(f"Média final: {media:.1f}")
    print(f"Resultado: {resultado}")

    print("=" * 50)

else:
    print("Nenhuma nota foi lançada.")