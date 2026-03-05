from scripts.queries import get_s3_client
from scripts.config import S3_BUCKET


def main():
    s3 = get_s3_client()

    response = s3.list_objects_v2(Bucket=S3_BUCKET)

    for obj in response.get("Contents", []):
        print(obj["Key"])


if __name__ == "__main__":
    main()