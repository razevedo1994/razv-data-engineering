import datetime
from ingestors import AwsDaySummaryIngestor
from writers import S3Writer

import logging

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)


def lambda_handler(event, context):
    logger.info(f"{event}")
    logger.info(f"{context}")

    AwsDaySummaryIngestor(
        writer=S3Writer,
        coins=["BTC", "ETH", "LTC"],
        default_start_date=datetime.date(2021, 6, 1),
    )
