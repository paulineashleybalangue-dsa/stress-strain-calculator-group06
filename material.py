class Material:

    def __init__(self, name: str, properties: MaterialProperties):
        self.name = name
        self.properties = properties

    def can_withstand_stress(self, stress_pa: float) -> bool:
        return stress_pa < self.properties.yield_strength
