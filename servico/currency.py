import asyncio

import httpx


bandeira_valor = {
    "ar": {
        "country_name": "argentina",
        "currency_code": "ars",
    },
    "br": {
        "country_name": "brazil",
        "currency_code": "brl",
    },
    "au": {
        "country_name": "australia",
        "currency_code": "aud",
    },
    "ca": {
        "country_name": "canada",
        "currency_code": "cad",
    },
    "cl": {
        "country_name": "chile",
        "currency_code": "clp",
    },
    "us": {
        "country_name": "united states",
        "currency_code": "usd",
    },
    "gb": {
        "country_name": "united kingdom",
        "currency_code": "gbp",
    },
    "de": {
        "country_name": "germany",
        "currency_code": "eur",
    },
}


BASE_URL = (
    "https://cdn.jsdelivr.net/npm/"
    "@fawazahmed0/currency-api@latest/"
    "v1/currencies"
)



async def buscar_moeda(
    client: httpx.AsyncClient,
    moeda: str,
) -> dict:

    url = f"{BASE_URL}/{moeda}.json"

    response = await client.get(url)
    response.raise_for_status()

    return response.json()


async def buscar_cotacao(
    client: httpx.AsyncClient,
    moeda_origem: str,
    moeda_destino: str,
) -> float:

    dados = await buscar_moeda(client, moeda_origem)

    return dados[moeda_origem][moeda_destino]


async def buscar_cotacoes_brl(
    client: httpx.AsyncClient,
) -> dict:

    usd, cad, gbp, eur = await asyncio.gather(
        buscar_cotacao(client, "usd", "brl"),
        buscar_cotacao(client, "cad", "brl"),
        buscar_cotacao(client, "gbp", "brl"),
        buscar_cotacao(client, "eur", "brl"),
    )

    return {
        "usd": usd,
        "cad": cad,
        "gbp": gbp,
        "eur": eur,
    }
