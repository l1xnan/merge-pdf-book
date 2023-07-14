import re
import subprocess
from pathlib import Path

from pypdf import PdfWriter

base_url = "https://github.com/Visualize-ML"

names = [
    "Book1_Python-For-Beginners",
    "Book2_Beauty-of-Data-Visualization",
    "Book3_Elements-of-Mathematics",
    "Book4_Power-of-Matrix",
    "Book5_Essentials-of-Probability-and-Statistics",
    "Book6_First-Course-in-Data-Science",
    "Book7_Visualizations-for-Machine-Learning",
]

for name in names:
    print("=" * 30)
    print(name)
    repo = f"{base_url}/{name}.git"
    res = subprocess.run(["git", "clone", repo, f"repos/{name}"], capture_output=True)

    files = sorted(Path(f"repos/{name}").glob("*.pdf"))

    merger = PdfWriter()

    for pdf in files:
        bookmark = pdf.stem
        if "Ch" in bookmark:
            if items := re.findall(r"Ch_?(\d{2})_{1,2}([^_]+)_+([^_]+)_+([^_]+)", bookmark):
                chapter, title, *_ = items[0]
                bookmark = f"{chapter.replace('Ch', '')}-{title}"
        print(bookmark)
        merger.append(pdf, bookmark)

    merger.write(f"{name}.pdf")
    merger.close()

if __name__ == '__main__':
    pass
