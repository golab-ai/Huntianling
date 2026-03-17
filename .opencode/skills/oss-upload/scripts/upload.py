import argparse
import os
from datetime import timedelta
from pathlib import Path
from dotenv import load_dotenv
import alibabacloud_oss_v2 as oss

load_dotenv()

def upload_and_share(
    bucket_name: str,
    object_name: str,
    local_file_path: str,
    region: str,
    expires_hours: int = 1
):
    credentials_provider = oss.credentials.EnvironmentVariableCredentialsProvider()
    cfg = oss.config.load_default()
    cfg.credentials_provider = credentials_provider
    cfg.region = region
    client = oss.Client(cfg)

    put_request = oss.PutObjectRequest(
        bucket=bucket_name,
        key=object_name,
    )

    uploader = client.uploader()
    upload_result = uploader.upload_file(put_request, filepath=local_file_path)

    get_request = oss.GetObjectRequest(bucket=bucket_name, key=object_name)
    presign_result = client.presign(get_request, expires=timedelta(hours=expires_hours))

    return {
        "etag": upload_result.etag,
        "url": presign_result.url,
        "expires_hours": expires_hours
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--bucket", default=os.getenv("OSS_BUCKET_NAME"))
    parser.add_argument("--key", required=True)
    parser.add_argument("--file", required=True)
    parser.add_argument("--region", default=os.getenv("OSS_REGION"))
    parser.add_argument("--prefix", default=os.getenv("OSS_UPLOAD_PREFIX", ""))
    parser.add_argument("--expires", type=int, default=int(os.getenv("OSS_EXPIRES_HOURS", 1)))

    args = parser.parse_args()

    full_key = f"{args.prefix}{args.key}" if args.prefix else args.key

    result = upload_and_share(args.bucket, full_key, args.file, args.region, args.expires)
    print(f"[Preview]({result['url']})")
