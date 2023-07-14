import re
import subprocess
from pathlib import Path

from pypdf import PdfWriter

base_url = "https://github.com/Visualize-ML"

names = [
    ("Book1_Python-For-Beginners", "编程不难"),
    ("Book2_Beauty-of-Data-Visualization", "可视之美"),
    ("Book3_Elements-of-Mathematics", "数学要素"),
    ("Book4_Power-of-Matrix", "矩阵力量"),
    ("Book5_Essentials-of-Probability-and-Statistics", "统计至简"),
    ("Book6_First-Course-in-Data-Science", "数据有道"),
    ("Book7_Visualizations-for-Machine-Learning", "机器学习"),
]

Path("repos").mkdir(exist_ok=True, parents=True)

for name, book in names:
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

    merger.write(f"{name}_{book}.pdf")
    merger.close()

if __name__ == "__main__":
    pass
