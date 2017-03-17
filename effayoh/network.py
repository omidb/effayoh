from networkx import DiGraph

class Network(DiGraph):

    def __init__(self):
        self.aggregated_codes = {}
        super().__init__()

    def __getitem__(self, key):
        if key in self.aggregated_codes:
            key = self.aggregated_codes[key]
        return super().__getitem__(key)
