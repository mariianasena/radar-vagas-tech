
from fontes import (
    buscar_remotive,
    buscar_remoteok,
    padronizar_remotive,
    padronizar_remoteok
)

import requests

print("=" * 40)
print("         RADAR DE VAGAS TECH")
print("=" * 40)

palavras_tecnologia = [
    "developer", "software", "python", "data",
    "analyst", "engineer", "support", "help desk",
    "service desk", "qa", "tester", "testing",
    "security", "cloud", "devops",
    "desenvolvedor", "programador",
    "tecnologia", "infraestrutura"
]

palavras_iniciante = [
    "intern", "internship", "estagio", "estágio",
    "trainee", "junior", "júnior", "jr",
    "entry level", "entry-level",
    "graduate", "apprentice"
]

palavras_experiente = [
    "senior", "sênior", "sr.",
    "lead", "principal", "staff"
]

try:
    print("\nBuscando vagas remotas de tecnologia...")

    vagas_remotive = buscar_remotive()
    vagas_remoteok = buscar_remoteok()

    todas_vagas = (
        padronizar_remotive(vagas_remotive)
        + padronizar_remoteok(vagas_remoteok)
    )

    print(f"\nTotal de vagas encontradas: {len(todas_vagas)}")

    vagas_brasil = []

    for vaga in todas_vagas:
        local = (vaga.get("local") or "").lower()

        if any(
            palavra in local
            for palavra in ["brazil", "brasil", "worldwide"]
        ):
            vagas_brasil.append(vaga)

    vagas_tecnologia = []

    for vaga in vagas_brasil:
        cargo = (vaga.get("titulo") or "").lower()

        if any(
            palavra in cargo
            for palavra in palavras_tecnologia
        ):
            vagas_tecnologia.append(vaga)

    vagas_iniciantes = []

    for vaga in vagas_tecnologia:
        cargo = (vaga.get("titulo") or "").lower()

        iniciante = any(
            palavra in cargo
            for palavra in palavras_iniciante
        )

        suporte = any(
            palavra in cargo
            for palavra in ["support", "help desk", "service desk"]
        )

        experiente = any(
            palavra in cargo
            for palavra in palavras_experiente
        )

        if (iniciante or suporte) and not experiente:
            vagas_iniciantes.append(vaga)

    print(f"Vagas com localização compatível: {len(vagas_brasil)}")
    print(f"Vagas de tecnologia: {len(vagas_tecnologia)}")
    print(f"Possíveis vagas para iniciantes: {len(vagas_iniciantes)}")

    print("\n" + "=" * 40)
    print("       OPORTUNIDADES ENCONTRADAS")
    print("=" * 40)

    if not vagas_iniciantes:
        print("\nNenhuma vaga inicial encontrada nesta busca.")

    for vaga in vagas_iniciantes[:10]:
        print("\n" + "-" * 40)
        print("Cargo:", vaga.get("titulo"))
        print("Empresa:", vaga.get("empresa"))
        print("Localização:", vaga.get("local"))
        print("Fonte:", vaga.get("fonte"))
        print("Link:", vaga.get("link"))

    print("\nBusca finalizada!")

except requests.RequestException as erro:
    print("Erro ao buscar vagas:", erro)
