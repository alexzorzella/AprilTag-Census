import os
import csv
import shutil
from pathlib import Path
import imageio

from matplotlib import pyplot as plt

from moms_apriltag import ApriltagBoard
from moms_apriltag import TagGenerator2
from moms_apriltag import TagGenerator3

IMAGE_DIR = "./tags/"
CSV_FILENAME = "./tags.csv"
FAMILY = f"tag36h11"

def main():
    image_dir = Path(IMAGE_DIR)

    if Path(CSV_FILENAME).exists():
        os.remove(Path(CSV_FILENAME))

    if image_dir.exists():
        shutil.rmtree(image_dir)

    image_dir.mkdir(exist_ok=True)

    with open(CSV_FILENAME, 'w') as csv_file:
        writer = csv.writer(csv_file)

        for i in range(586):
            tg = TagGenerator2(FAMILY)
            tag = tg.generate(i, 16)

            tag_name = f"{FAMILY}_{i}"

            filename = str(image_dir / f"{tag_name}.png")
            imageio.imwrite(filename, tag)

            writer.writerow([tag_name])

            print(f"Wrote {filename}")

if __name__ == "__main__":
    main()