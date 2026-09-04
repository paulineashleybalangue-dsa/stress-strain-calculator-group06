class Material:

    def __init__(self, name: str, properties: MaterialProperties):
        self.name = name
        self.properties = properties

    def can_withstand_stress(self, stress_pa: float) -> bool:
        return stress_pa < self.properties.yield_strength

class Metal(Material):

    def __init__(
        self,
        name: str,
        properties: MaterialProperties,
        is_ferrous: bool = False,
    ):
        super().__init__(name, properties)
        self.is_ferrous = is_ferrous
