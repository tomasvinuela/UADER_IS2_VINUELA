from typing import NamedTuple
class Avion_base(NamedTuple):
    id_avion: int
    name: str = ''
    body: str = ''
    wing1: str = ''
    wing2: str = ''
    turbine1: str = ''
    turbine2: str = ''
    railway: str = ''


class Constructor_avion(object):
    def __init__(self, id_avion):
        self.id_avion = id_avion
        self.name = None

    def build(self):
        return Avion_base(self.id_avion, self.name)


avion_prueba = Constructor_avion(25)
