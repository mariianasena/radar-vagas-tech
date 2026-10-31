
import requests


def buscar_remotive():
    url = "https://remotive.com/api/remote-jobs"

    resposta = requests.get(url, timeout=20)
    resposta.raise_for_status()

    dados = resposta.json()

    return dados.get("jobs", [])



def buscar_remoteok():
    url = "https://remoteok.com/api"

    cabecalhos = {
        "User-Agent": "RadarVagasTech/1.0"
    }

    resposta = requests.get(
        url,
        headers=cabecalhos,
        timeout=20
    )

    resposta.raise_for_status()
    dados = resposta.json()

    if not isinstance(dados, list):
        return []

    vagas = [
        vaga for vaga in dados
        if isinstance(vaga, dict) and vaga.get("position")
    ]

    return vagas


    
def padronizar_remotive(vagas):
    resultado = []

    for vaga in vagas:
        resultado.append({
            "titulo": vaga.get("title", ""),
            "empresa": vaga.get("company_name", ""),
            "local": vaga.get("candidate_required_location", ""),
            "link": vaga.get("url", ""),
            "fonte": "Remotive"
        })

    return resultado


def padronizar_remoteok(vagas):
    resultado = []

    for vaga in vagas:
        resultado.append({
            "titulo": vaga.get("position", ""),
            "empresa": vaga.get("company", ""),
            "local": vaga.get("location", ""),
            "link": vaga.get("url", ""),
            "fonte": "Remote OK"
        })

    return resultado


def padronizar_remotive(vagas):
    resultado = []

    for vaga in vagas:
        resultado.append({
            "titulo": vaga.get("title", ""),
            "empresa": vaga.get("company_name", ""),
            "local": vaga.get("candidate_required_location", ""),
            "link": vaga.get("url", ""),
            "fonte": "Remotive"
        })

    return resultado
