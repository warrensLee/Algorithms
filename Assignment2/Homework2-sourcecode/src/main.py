import os
import sys
from pathlib import Path
from typing import Dict, List

from graph import Graph
from bfs import bfs
from dfs import dfs
from rdfs import rdfs


def test_graph(alg_name: str) -> bool:
    g = Graph(6)
    g.insert_edge(0, 1)
    g.insert_edge(1, 2)
    g.insert_edge(1, 3)
    g.insert_edge(2, 4)
    g.insert_edge(4, 3)
    g.insert_edge(4, 5)

    if alg_name == "bfs":
        searchfn = bfs
    elif alg_name == "dfs":
        searchfn = dfs
    else:
        searchfn = rdfs

    print(f"Path from 0 to 5 by {alg_name}: ", end="")
    path = g.search(0, 5, searchfn)
    print(" ".join(str(x) for x in path))
    return True


def search_on_campus(start: str = "BELL", destination: str = "HAPG", alg_name: str = "bfs") -> None:
    # Make paths robust regardless of where the script is run from.
    project_root = Path(__file__).resolve().parent.parent
    info_path = project_root / "assets" / "map_info.txt"

    with info_path.open("r", encoding="utf-8") as reader:
        n, m = map(int, reader.readline().split())
        name2index: Dict[str, int] = {}
        index2name: Dict[int, str] = {}
        xs: List[int] = []
        ys: List[int] = []

        for _ in range(n):
            index_s, name, x_s, y_s = reader.readline().split()
            index = int(index_s)
            x = int(x_s)
            y = int(y_s)
            xs.append(x)
            ys.append(y)
            name2index[name] = index
            index2name[index] = name

        g = Graph(n)

        if alg_name == "bfs":
            searchfn = bfs
        elif alg_name == "dfs":
            searchfn = dfs
        else:
            searchfn = rdfs

        for _ in range(m):
            u_s, v_s = reader.readline().split()
            g.insert_edge(int(u_s), int(v_s))

    path = g.search(name2index[start], name2index[destination], searchfn)

    # Keep the original C++ message (note it prints `start` twice in the prefix).
    print(f"Path from {start} to  detination: {start}", end="")
    for i in range(1, len(path)):
        print(f" -> {index2name[path[i]]}", end="")
    print()

    # Visualization (optional).
    # By default, we *only save* the
    # visualization to a file. To force a GUI window, set HW2_SHOW_GUI=1 and ensure a
    # working display is available.
    try:
        import cv2
    except Exception:
        print("You have to use OpenCV to visualize your map road")
        return

    img_path = project_root / "assets" / "map.png"
    image = cv2.imread(str(img_path))
    if image is None:
        print("Could not load map image for visualization.")
        return

    for i in range(n):
        cv2.circle(image, (xs[i], ys[i]), 10, (255, 0, 0), -1)
        cv2.putText(
            image,
            index2name[i],
            (xs[i], ys[i] - 10),
            cv2.FONT_HERSHEY_DUPLEX,
            0.7,
            (255, 0, 0),
            1,
        )

    for i in range(len(path)):
        if i > 0:
            cv2.line(
                image,
                (xs[path[i]], ys[path[i]]),
                (xs[path[i - 1]], ys[path[i - 1]]),
                (255, 0, 0),
                4,
            )

    out_path = project_root / "bin" / f"path_{start}_{destination}_{alg_name}.png"
    cv2.imwrite(str(out_path), image)
    print(f"Saved visualization to: {out_path}")

    if os.environ.get("HW2_SHOW_GUI") == "1":
        # Only attempt GUI if explicitly requested.
        cv2.imshow(f"Path from {start} to {destination}", image)
        cv2.waitKey(0)


def main(argv: List[str]) -> int:
    if len(argv) < 2:
        print("Usage: python3 src/main.py <bfs|dfs|rdfs>")
        return 2

    alg_name = argv[1]
    print(f"Perform unit test on your {alg_name} implementation")
    test_graph(alg_name)

    print("\n\n")
    search_on_campus("JBHT", "HAPG", alg_name)
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
