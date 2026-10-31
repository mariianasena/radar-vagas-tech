
import requests

print("=" * 40)
print("         RADAR DE VAGAS TECH")
print("=" * 40)

print("\nBuscando vagas remotas de tecnologia...")

url = "https://remotive.com/api/remote-jobs"

try:
    resposta = requests.get(url, timeout=20)
    resposta.raise_for_status()

    dados = resposta.json()
    vagas = dados.get("jobs", [])

    vagas_brasil = []

    for vaga in vagas:
        local = vaga.get("candidate_required_location") or ""
        local = local.lower()

        if "brazil" in local or "brasil" in local or "worldwide" in local:
            vagas_brasil.append(vaga)

    palavras_tecnologia = [
        "developer", "software", "python",
        "data", "analyst", "engineer",
        "support", "help desk", "service desk",
        "qa", "tester", "testing",
        "security", "cloud", "devops",
        "desenvolvedor", "programador",
        "tecnologia", "infraestrutura"
    ]

    vagas_tecnologia = []

    for vaga in vagas_brasil:
        cargo = (vaga.get("title") or "").lower()

        if any(palavra in cargo for palavra in palavras_tecnologia):
            vagas_tecnologia.append(vaga)


    palavras_iniciante = [
        "intern", "internship", "estagio",
        "estágio", "trainee", "junior",
        "júnior", "jr", "entry level",
        "entry-level", "graduate", "apprentice"
    ]

    palavras_experiente = [
        "senior", "sênior", "sr.",
        "lead", "principal", "staff"
    ]

    vagas_iniciantes = []
    vagas_outros_niveis = []

    for vaga in vagas_tecnologia:
        cargo = (vaga.get("title") or "").lower()
        palavras_cargo = cargo.replace("-", " ").split()

        iniciante = any(
            palavra in cargo
            for palavra in palavras_iniciante
        )

        experiente = any(
            palavra in palavras_cargo
            for palavra in palavras_experiente
        )

        if iniciante and not experiente:
            vagas_iniciantes.append(vaga)
        else:
            vagas_outros_niveis.append(vaga)

    print(f"Vagas com indicativo de nível inicial: {len(vagas_iniciantes)}")

    print(f"Vagas com cargos de tecnologia: {len(vagas_tecnologia)}")

    print(f"\nTotal de vagas recebidas: {len(vagas)}")
    print(f"Vagas possivelmente disponíveis no Brasil: {len(vagas_brasil)}")

    print("\nPrimeiras vagas filtradas:\n")

    for vaga in vagas_iniciantes[:10]:
        print("-" * 40)
        print("Cargo:", vaga.get("title"))
        print("Empresa:", vaga.get("company_name"))
        print("Localização:", vaga.get("candidate_required_location"))
        print("Link:", vaga.get("url"))

except requests.RequestException as erro:
    print("Erro ao buscar vagas:", erro)
