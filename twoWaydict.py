class Tdic(dict):
    def __setKV__(self, k, v):

        if k in self:
            del self[k]
        if v in self:
            del self[v]
        Tdic.__setKV__(self, k, v)
        Tdic.__setKV__(self, v, k)
