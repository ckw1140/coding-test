N = int(input())

st = set()
for _ in range(N):
    name, action = input().split()

    if action == "enter":
        st.add(name)
    if action == "leave":
        st.remove(name)

st = list(st)
st.sort()
st = st[::-1]

for name in st:
    print(name)