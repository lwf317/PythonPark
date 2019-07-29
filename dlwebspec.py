import argparse
import urllib


SPEC_URL_FMT = "http://172.19.16.247/Download/EntityName?model_name={}&entity_name=forrd2"


def download(models):
    for model in models:
        url = SPEC_URL_FMT.format(model)
        local = "{}.xlsx".format(model)
        urllib.urlretrieve(url, local)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--models", help="The cameras whose spec are desired.", nargs='*')
    args = parser.parse_args()
    download(args.models)


if __name__ == "__main__":
    main()
