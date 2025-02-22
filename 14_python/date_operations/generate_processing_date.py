from datetime import datetime, timedelta


class GenerateProcessingDate:
    """
    This class is used to generate the processing date for a D-2 ingestion scenario.
    """

    def __init__(self):
        self.today = datetime.now()
        self.interval = 2

    def get_processing_date(self):
        day_of_week = self.today.weekday()

        interval = self.interval = (
            4 if day_of_week == 1 or day_of_week == 2 else self.interval
        )
        return self.today - timedelta(days=interval)


if __name__ == "__main__":
    processing_date = GenerateProcessingDate().get_processing_date()
    print(processing_date)
