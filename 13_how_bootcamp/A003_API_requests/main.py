import requests
import pandas as pd
import backoff
import logging


log = logging.getLogger()
log.setLevel(logging.DEBUG)
formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch = logging.StreamHandler()
ch.setFormatter(formater)
log.addHandler(ch)


url = "https://economia.awesomeapi.com.br/json/last/"

moedas = ["USD-BRL", "EUR-BRL", "BTC-BRL"]


@backoff.on_exception(
    backoff.expo,
    (requests.exceptions.ConnectionError, requests.exceptions.HTTPError),
    max_tries=3,
)
def get_price(url: str, moedas: list):
    log.info("Initiating requests.")
    json_responses = []
    for moeda in moedas:
        endpoind = url + moeda
        response = requests.get(endpoind)
        json_responses.append(response.json())

    log.info("Completed requests.")
    return json_responses


def build_csv(responses: list):
    log.info("Starting build csv.")
    data = []
    for response in responses:
        for key, value in response.items():
            data.append(value)

    dataframe = pd.DataFrame(data)
    log.info("Generating csv.")
    dataframe.to_csv("cotacoes.csv")


def main(url: str, moedas: list):
    responses = get_price(url, moedas)
    build_csv(responses)


if __name__ == "__main__":
    main(url, moedas)
