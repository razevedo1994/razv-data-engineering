import requests
import pandas as pd
import backoff

url = "https://economia.awesomeapi.com.br/json/last/"

moedas = ["USD-BRL", "EUR-BRL", "BTC-BRL"]


@backoff.on_exception(
    backoff.expo,
    (requests.exceptions.ConnectionError, requests.exceptions.HTTPError),
    max_tries=3,
)
def get_price(url: str, moedas: list):
    json_responses = []
    for moeda in moedas:
        endpoind = url + moeda
        response = requests.get(endpoind)
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
