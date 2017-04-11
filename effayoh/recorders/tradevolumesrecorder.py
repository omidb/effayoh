"""
Provide a trade volumes recorder.

The trade volume recorder records the changes in total trade volume of a
collection of countries during model execution. By default, the trade
volume recorder records trade for all the countries in the network.

"""


class TradeVolumeRecorder:

    def __init__(self, countries=[]):
        self.countries = []
        self.volumes = []

    def record(self, network):
        if self.countries:
            self.record_countries(network)
        else:
            self.record_all(network)

    def record_countries(self, network):
        acc = 0.0
        for u, v, data in network.edges(data=True):
            if not (u in self.countries and v in self.countries):
                continue
            acc += data["exports"]
        else:
            self.volumes.append(acc)

    def record_all(self, network):
        acc = 0.0
        for u, v, data in network.edges(data=True):
            acc += data["exports"]
        else:
            self.volumes.append(acc)
