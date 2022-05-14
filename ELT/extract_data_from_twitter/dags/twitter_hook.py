from airflow.hooks.http_hook import HttpHook
import requests
import json


class TwitterHook(HttpHook):
    def __init__(self, query, conn_id=None, start_time=None, end_time=None):
        self.query = query
        self.conn_id = conn_id or "twitter_default"
        self.start_time = start_time
        self.end_time = end_time
        super().__init__(http_conn_id=self.conn_id)

    def create_url(self):
        query = self.query
        tweet_fields = "tweet.fields=author_id,conversation_id,created_at,id,in_reply_to_user_id,public_metrics,text"
        user_fields = "expansions=author_id&user.fields=id,name,username,created_at"
        start_time = f"&start_time={self.start_time}" if self.start_time else ""
        end_time = f"&end_time={self.end_time}" if self.end_time else ""

        url = f"{self.base_url}/2/tweets/search/recent?query={query}&{tweet_fields}&{user_fields}{start_time}{end_time}"

        return url

    def connect_to_endpoint(self, url, session):
        response = requests.Request("GET", url)
        prep = session.prepare_request(response)
        self.log.info(f"URL: {url}")
        return self.run_and_check(session, prep, {}).json()

    def paginate(self, url, session, next_token=""):
        if next_token:
            full_url = f"{url}&next_token={next_token}"
        else:
            full_url = url

        data = self.connect_to_endpoint(full_url, session)

        yield data
        if "next_token" in data.get("meta", {}):
            yield from self.paginate(url, session, data["meta"]["next_token"])

    def run(self):
        session = self.get_conn()

        url = self.create_url()

        yield from self.paginate(
            url, session
        )


# if __name__ == "__main__":
#     for pg in TwitterHook("AluraOnline").run():
#         print(json.dumps(pg, indent=4, sort_keys=True))
