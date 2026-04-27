from sho3a3 import Sho3a3
from masfofah import Masfofah

class Masfofah:
    def __init__(self, data):
        self.rows = [row if isinstance(row, Sho3a3) else Sho3a3(row) for row in data]
        self.shaper = (len(self.rows), len(self.rows[0]) if self.rows else 0)

    def __repr__(self):
        return "masfofah:\n" + "\n".join(str(r) for r in self.rows)

    def shape(self):
        return self.shaper

    def __len__(self):
        return len(self.rows)

    def __getitem__(self, place):
        return self.rows[place]

    def __add__(self, other):
        assert self.shape() == other.shape()
        return Masfofah([self.rows[i] + other.rows[i] for i in range(len(self.rows))])

    def __sub__(self, other):
        assert self.shape() == other.shape()
        return Masfofah([self.rows[i] - other.rows[i] for i in range(len(self.rows))])

    def extract_columns(self):
        r, c = self.shape()
        cols = []
        for j in range(c):
            cols.append(Sho3a3([self.rows[i][j] for i in range(r)]))
        return Masfofah(cols)

    def __mul__(self, other):
        assert self.shape()[1] == other.shape()[0]
        other_cols = other.extract_columns()
        res = []
        for row in self.rows:
            res.append([row * col for col in other_cols.rows])
        return Masfofah(res)

    def man8ool(self):
        return self.extract_columns()

    def sum(self, axis: int):
        if axis == 0:
            return Sho3a3([c.sum() for c in self.extract_columns().rows])
        return Sho3a3([r.sum() for r in self.rows])

    def add(self, other, axis=0):
        if axis == 1:
            self.rows.extend(other.rows)
        else:
            for i in range(len(self.rows)):
                self.rows[i].sho3a3.extend(other.rows[i].sho3a3)
        self.shaper = (len(self.rows), len(self.rows[0]))
