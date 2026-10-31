
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

    print(f"\nTotal de vagas recebidas: {len(vagas)}")

    print("\nPrimeiras vagas encontradas:\n")

    for vaga in vagas[:10]:
        print("-" * 40)
        print("Cargo:", vaga.get("title"))
        print("Empresa:", vaga.get("company_name"))
        print("Localização:", vaga.get("candidate_required_location"))
        print("Link:", vaga.get("url"))

except requests.RequestException as erro:
    print("Erro ao buscar vagas:", erro)
