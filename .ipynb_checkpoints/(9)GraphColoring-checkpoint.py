from collections import defaultdict

class Graph:
    def __init__(self, subjects):
        self.subjects, self.graph = subjects, defaultdict(list)
    def a(self, s1, s2):
        self.graph[s1].append(s2)
        self.graph[s2].append(s1)
    def c(self):
        cm, ac = {}, set(range(1, len(self.subjects) + 1))
        for s in self.subjects:
            uc = {cm[n] for n in self.graph[s] if n in cm}
            acolor = ac - uc
            if acolor: cm[s] = min(acolor)
            else: cm[s] = len(ac) + 1
            ac.add(cm[s])
        return cm
    def t(self):
        return max(self.c().values())

def main():
    n = int(input("Enter the number of subjects: "))
    s, st, g = [], {}, Graph
    for i in range(n):
        sub = input(f"Enter subject {i + 1}: ")
        s.append(sub)
        n_st = int(input(f"Enter the number of students for {sub}: "))
        st_list = [input(f"Enter student {j + 1} for {sub}: ") for j in range(n_st)]
        st[sub] = st_list
    gr = g(s)
    for _ in range(int(input("Enter the number of edges: "))):
        e = input("Enter edge (subject1 subject2): ").split()
        gr.a(e[0], e[1])
    print(f"\nMinimum time slots needed: {gr.t()}")

if __name__ == "__main__":
    main()
