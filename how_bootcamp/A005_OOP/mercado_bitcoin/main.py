import datetime
import time
from schedule import repeat, every, run_pending
from ingestors import AwsDaySummaryIngestor
from writers import S3Writer

if __name__ == "__main__":
    day_summary_ingestor = AwsDaySummaryIngestor(
        writer=S3Writer,
        coins=["BTC", "ETH", "LTC"],
        default_start_date=datetime.date(2021, 6, 1),
    )

    @repeat(every(1).seconds)
    def job():
        day_summary_ingestor.ingest()

    while True:
        run_pending()
        time.sleep(0.5)
