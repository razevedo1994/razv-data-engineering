#!usr/bin/env python3

import pandas as pd



if __name__ == "__main__":
    data = [{"product_id": 123456, "reviews": [{"review_id": 321, "comment": "good", "date": "2023-06-01"}, {"review_id": 654, "comment": "bad", "date": "2023-04-23"}]}, 
            {"product_id": 123457, "reviews": [{"review_id": 987, "comment": "good", "date": "2023-01-01"}, {"review_id": 998, "comment": "bad", "date": "2023-06-11"}]}]

    df = pd.DataFrame.from_dict(data)

    exploded_df = df.explode('reviews').reset_index(drop=True)

    final_df = exploded_df.join(pd.json_normalize(exploded_df["reviews"])).drop(columns=["reviews"])

    print(final_df)
