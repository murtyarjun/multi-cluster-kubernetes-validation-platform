import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.services.inventory_service import InventoryService

service = InventoryService()

print(service.get_environments())

print(service.get_groups("PROD"))

print(len(service.get_clusters("PROD", ["Payments"])))