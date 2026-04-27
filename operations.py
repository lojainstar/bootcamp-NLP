
def masfofah_asfar(rows, cols):
    return Masfofah([[0]*cols for _ in range(rows)])


def masfofah_wahidat(rows, cols):
    return Masfofah([[1]*cols for _ in range(rows)])


def i9n3_masfofatan(qaimah):
    return Masfofah(qaimah)

def i9n3_sho3a3an(qaimah):
    return Masfofah([qaimah])
