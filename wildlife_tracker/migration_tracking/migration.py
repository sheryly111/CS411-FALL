from typing import Any 
from wildlife_tracker.migration_tracking import MigrationPath 

class Migration:
    def __init__(self, 
                 current_date: str, 
                 current_location: str, 
                 migration_id : int,
                 migration_path: MigrationPath,
                 status: str,
                 paths: dict[int, MigrationPath] = {}
                 ) -> None:
        self.current_date = current_date 
        self.current_location = current_location 
        self.migration_id = migration_id
        self.migration_path = migration_path
        self.status = status 
        self.paths = paths 
    
    def schedule_migration(self, migration_path: MigrationPath) -> None:
        pass

    def update_migration_details(self, migration_id: int, **kwargs: Any) -> None:
        pass
