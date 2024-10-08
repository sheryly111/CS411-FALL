from typing import Any, Optional

class Animal:
    def __init__(self, 
                 animal_id: int,
                 health_status: Optional[str],
                 species: str
                 ) -> None:
        self.animal_id = animal_id 
        self.health_status = health_status
        
        pass