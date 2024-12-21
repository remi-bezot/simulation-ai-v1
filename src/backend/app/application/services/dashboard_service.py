from typing import List, Dict, Any


class DashboardService:
    """
    Service pour gérer les opérations liées au tableau de bord.
    """

    def get_dashboard_data(self) -> List[Dict[str, Any]]:
        """
        Retourne les données statiques du tableau de bord.

        :return: Liste de DashboardData représentant les données du tableau de bord.
        """
        return [
            {"id": 1, "name": "Janvier", "value": 30},
            {"id": 2, "name": "Février", "value": 45},
            {"id": 3, "name": "Mars", "value": 50},
        ]
