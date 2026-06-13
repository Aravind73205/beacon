import json
from pathlib import Path
from datetime import datetime


class MemoryService:
    """
    Service for customer memory operations
    """

    def __init__(self):
        self.memory_file = Path("data/memory_store.json")

        if not self.memory_file.exists():
            self.memory_file.parent.mkdir(parents=True, exist_ok=True)

            with open(self.memory_file, "w") as file:
                json.dump([], file)


    def _load_memory(self):
        """
        load memory records.
        """
        with open(self.memory_file, "r") as file:
            return json.load(file)


    def _save_memory(self, data):
        """
        Save memory records
        """
        with open(self.memory_file, "w") as file:
            json.dump(data, file, indent=4)


    def save_customer_analysis(self, customer_analysis):
        """
        save customer analysis
        """

        memory = self._load_memory()

        customer_analysis["timestamp"] = (datetime.now().isoformat())
        memory.append(customer_analysis)
        self._save_memory(memory)


    def get_customer_history(self,customer_id):
        """
        get customer history
        """

        memory = self._load_memory()

        return [
            record
            for record in memory
            if record.get("customer_id") == customer_id
        ]


    def get_latest_analysis(self, customer_id):
        """
        get latest analysis for a customer
        """

        history = self.get_customer_history(customer_id) 
        return history[-1] if history else None