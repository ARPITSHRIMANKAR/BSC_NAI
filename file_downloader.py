import csv
import os
import urllib.request


def download_files(csv_file, output_dir):
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            url = row[0]
            filename = os.path.basename(url)
            output_path = os.path.join(output_dir, filename)
            print(f"Downloading file {i+1}: {url}")
            try:
                urllib.request.urlretrieve(url, output_path)
            except urllib.error.URLError as e:
                print(f"Error downloading file: {e}")
            else:
                print(f"Saved file to {output_path}")


if __name__ == "__main__":
    csv_file = "output.csv"
    output_dir = "downloads"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    download_files(csv_file, output_dir)