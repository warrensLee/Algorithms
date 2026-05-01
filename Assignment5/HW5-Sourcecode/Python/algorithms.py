def rabinKarpSearch(pattern: str, text: str) -> list[int]:
    matches: list[int] = []

    d = 256             # number of ASCII characters
    q = 101             # a prime number to reduce collisions (for modulo operations)
    m = len(pattern)    # the length of this specific pattern
    n = len(text)       # the length of the text to search within
    p = 0               # hash value for pattern
    t = 0               # hash value for the current text
    h = 1               # high order digit multiplier

    # safety net: if pattern is empty or longer than text, return no matches
    if m == 0 or m > n:
        return matches

    # compute h = pow(d, m-1) % q
    for i in range(m - 1):
        h = (h * d) % q

    # compute initial hash values for pattern and first window of text
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    # now slide the pattern over text one by one to compare 
    for i in range(n - m + 1):

        # if hash values match, check characters one by one
        if p == t:
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                matches.append(i)

        # calculate hash value for the next window
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q

    return matches



def floydWarshall(V: int, dist: list[list[int]]) -> None:
    INF = int(1e8)

    # for each intermediate vertex
    for k in range(V):
        # pick all vertices as source one by one
        for i in range(V):
            # pick all vertices as destination
            # for the above picked source
            for j in range(V):
                # shortest path from i to j 
                if dist[i][k] != INF and dist[k][j] != INF:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


def solveTSP(
    mask: int,
    pos: int,
    n: int,
    dist: list[list[int]],
    dp: list[list[int]],
) -> int:
    
    # if all cities have been visited, return to the starting city
    if mask == (1 << n) - 1:
        return dist[pos][0]
    
    # if this state has already been computed, return the stored result
    if dp[mask][pos] != -1:
        return dp[mask][pos]
    
    answer = int(1e8)

    # go to each unvisited city
    for city in range(n):
        if (mask & (1 << city)) == 0:
            new_cost = dist[pos][city] + solveTSP(
                mask | (1 << city),
                city,
                n,
                dist,
                dp
            )

            answer = min(answer, new_cost)

    # store the result in dp table before returning
    dp[mask][pos] = answer
    return answer