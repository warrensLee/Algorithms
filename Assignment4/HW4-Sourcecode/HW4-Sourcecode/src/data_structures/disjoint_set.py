class DisjointSet:
    def __init__(self, n: int):
        self.parent = [-1] * n

    def find(self, u: int) -> int:
        if self.parent[u] == -1:
            return u
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def is_on_same_set(self, u: int, v: int) -> int:
        return 1 if self.find(u) == self.find(v) else 0

    def join(self, u: int, v: int) -> None:
        pu = self.find(u)
        pv = self.find(v)
        if pu != pv:
            self.parent[pu] = pv
