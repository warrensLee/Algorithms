from graph import Graph
from algorithms import rabinKarpSearch, floydWarshall, solveTSP


def main() -> int:
    # 1. Load Map Data
    map_file = "map_info.txt"

    try:
        with open(map_file, "r", encoding="utf-8") as reader:
            tokens = iter(reader.read().split())

            n = int(next(tokens))
            m = int(next(tokens))

            name2index: dict[str, int] = {}
            index2name: dict[int, str] = {}

            for _ in range(n):
                building_id = int(next(tokens))
                name = next(tokens)
                x = int(next(tokens))
                y = int(next(tokens))
                name2index[name] = building_id
                index2name[building_id] = name

            G = Graph(n)
            for _ in range(m):
                u = int(next(tokens))
                v = int(next(tokens))
                G.insertEdge(u, v)  # Populates both AdjList and AdjMatrix
    except OSError:
        print(f"Error: Could not open {map_file}")
        return -1

    # 2. Rabin-Karp: Identify a destination building by keyword
    print("\n========================================================")
    print("   ALGORITHM 1: SMART CAMPUS DIRECTORY SEARCH")
    print("========================================================")

    search_query = "HILL"
    campus_catalogue = "BELL_JBHT_HILL_WJWH_HAPG"

    print(f"Action: Scanning campus database for: [{search_query}]")
    print("Method: Rabin-Karp Rolling Hash (Digital Fingerprinting)")
    print("--------------------------------------------------------")

    found = rabinKarpSearch(search_query, campus_catalogue)

    if found:
        print("STATUS: Success! Building identified.")
        for pos in found:
            # Visualize where the match is in the string
            print(f"Location: Found '{search_query}' at position {pos} in the record.")
            print(f"Visual: {campus_catalogue}")
            print("        " + (" " * pos) + ("^" * len(search_query)))
    else:
        print("STATUS: Building not found.")
        print("Check spelling or update the campus catalogue.")
        return -1
    print("--------------------------------------------------------")

    # 3. Floyd-Warshall: Pre-calculate all shortest paths on campus
    print("\n========================================================")
    print("   ALGORITHM 2: CAMPUS-WIDE NAVIGATION CALCULATOR")
    print("========================================================")
    print("Status: Analyzing all possible walking routes...")

    distMatrix = G.getDistanceMatrix()
    floydWarshall(n, distMatrix)

    print("Success: Shortest paths between all buildings calculated.")
    print("\nHow to read the table below:")
    print("- The numbers represent the minimum number of 'steps' between buildings.")
    print("- 'INF' means there is currently no connected path between those two buildings.")
    print("--------------------------------------------------------")

    # Header Row with Building Names
    print("FROM \\ TO\t", end="")
    for i in range(min(5, n)):
        # Truncate name to 4 letters for a clean table look
        shortName = index2name[i][:4]
        print(f"{shortName}\t", end="")
    print()
    print("-" * 60)

    # Data Rows
    for i in range(min(5, n)):
        rowName = index2name[i][:4]
        print(f"{rowName} |     \t", end="")

        for j in range(min(5, n)):
            if distMatrix[i][j] >= 1e8:  # Checking against our 'Infinity'
                print("--- \t", end="")
            elif i == j:
                print("0 \t", end="")  # Staying put
            else:
                print(f"{distMatrix[i][j]} \t", end="")
        print()
    print("--------------------------------------------------------")
    print(
        f"Example: To get from {index2name[0]} to {index2name[1]}, "
        f"it takes {distMatrix[0][1]} connection(s)."
    )

    # 4. TSP: Find the optimal tour for a mission (visit first 4 buildings)
    print("\n========================================================")
    print("   ALGORITHM 3: EFFICIENT CAMPUS TOUR PLANNER (TSP)")
    print("========================================================")

    tourSize = 4  # Number of buildings to include in the tour
    if n >= tourSize:
        print(
            f"Mission: Visit {tourSize} locations and return to start with minimum walking."
        )
        print("Target Stops: ", end="")
        for i in range(tourSize):
            suffix = " -> " if i < tourSize - 1 else " -> [Return]"
            print(f"{index2name[i]}{suffix}", end="")
        print()

        print("Status: Solving the 'Traveling Salesperson' puzzle...")

        # DP with Bitmasking initialization
        tspDP = [[-1 for _ in range(tourSize)] for _ in range(1 << tourSize)]
        optimalCost = solveTSP(1, 0, tourSize, distMatrix, tspDP)

        print("--------------------------------------------------------")
        print("RESULT: Optimal route identified.")
        print(f"Total Walking Distance: {optimalCost} connections.")
        print(
            f"Efficiency: This is the shortest possible path out of all {tourSize}! "
            "potential combinations."
        )
    else:
        print("Notice: Map size too small for a multi-stop tour optimization.")
        return -1
    print("========================================================")

if __name__ == "__main__":
    raise SystemExit(main())
