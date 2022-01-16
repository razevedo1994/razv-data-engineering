import requests
import pandas as pd
from exceptions import (
    BadRequestException,
    NotFoundException,
)

url = "https://economia.awesomeapi.com.br/json/last/"

moedas = ["USD-BRL", "EUR-BRL", "BTC-BRL"]


def handle_response(response):
    exceptions_for_status_code = {
        "400": BadRequestException(
            "Invalid request, e.g. using an unsupported HTTP method."
        ),
        "404": NotFoundException(
            "Requests to resources that don't exist or are missing."
        ),
    }

    if not response.ok:
        raise exceptions_for_status_code[str(response.status_code)]

    return


def get_price(url: str, moedas: list):
    json_responses = []
    for moeda in moedas:
        endpoind = url + moeda
        response = requests.get(endpoind)
        handle_response(response)
        json_responses.append(response.json())

    return json_responses


def build_dataframe(responses: list):
    data = []
    for response in responses:
        for key, value in response.items():
            data.append(value)

    dataframe = pd.DataFrame(data)
    dataframe.to_csv("cotacoes.csv")


def main(url: str, moedas: list):
    responses = get_price(url, moedas)
    build_dataframe(responses)


if __name__ == "__main__":
    main(url, moedas)
