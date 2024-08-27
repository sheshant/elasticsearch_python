import csv
from myapp.models import ChatGPTTweets  # Replace with your actual app and model


def bulk_save_from_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file, delimiter=',', quotechar='"', lineterminator="")  # Assumes the first row is header
        objects = []

        for row in reader:
            print(row)
            # Create an instance of MyModel for each row
            obj = ChatGPTTweets(
                id=row["id"],
                date=row["date"],
                content=row["content"],
                username=row["username"],
                like_count=row["like_count"],
                retweet_count=row["retweet_count"],
            )
            objects.append(obj)

        # Bulk create the objects in the database
        # ChatGPTTweets.objects.bulk_create(objects, batch_size=100000)

# bulk_save_from_csv('/Users/sheshantsingh/Downloads/Twitter Jan Mar.csv')
bulk_save_from_csv('/Users/sheshantsingh/Downloads/cr.csv')
