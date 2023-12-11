def comptar_vocals(paraula):
    return paraula.lower().count('a'), paraula.lower().count('e'), paraula.lower().count('i'), paraula.lower().count('o'), paraula.lower().count('u')

a, e, i, o, u = comptar_vocals("Ratapinyada")
print(f"Hi ha {a} a's, {e} e's, {i} i's, {o} o's i {u} u's.")
