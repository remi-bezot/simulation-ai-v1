from app.core.agents.types.agent_type import AgentType
from app.core.agents.interfaces.i_trader import ITrader
from app.core.agents.trading_skills import TradingSkills


class TraderAgentType(AgentType, ITrader):
    """
    Type d'agent pour les commerçants.
    """

    def __init__(self, name: str):
        super().__init__(name)
        self.trading_skills = TradingSkills()

    def get_type_name(self) -> str:
        """
        Retourne le nom du type d'agent.

        :return: Le nom du type d'agent.
        """
        return "Trader"

    def buy(self, item: str, quantity: int, price: float):
        """
        Acheter un article.

        :param item: L'article à acheter.
        :param quantity: La quantité à acheter.
        :param price: Le prix de l'article.
        """
        if self.has_trading_skill("buying"):
            total_cost = quantity * price
            if self.resources.use_resource("money", total_cost):
                self.resources.add_resource(item, quantity)
                print(
                    f"L'agent commerçant achète {quantity} {item}(s) pour {total_cost} unités monétaires"
                )
            else:
                print(
                    f"L'agent commerçant n'a pas assez d'argent pour acheter {quantity} {item}(s)"
                )
        else:
            print(
                f"L'agent commerçant n'a pas les compétences nécessaires pour acheter {item}"
            )

    def sell(self, item: str, quantity: int, price: float):
        """
        Vendre un article.

        :param item: L'article à vendre.
        :param quantity: La quantité à vendre.
        :param price: Le prix de l'article.
        """
        if self.has_trading_skill("selling"):
            if self.resources.use_resource(item, quantity):
                total_revenue = quantity * price
                self.resources.add_resource("money", total_revenue)
                print(
                    f"L'agent commerçant vend {quantity} {item}(s) pour {total_revenue} unités monétaires"
                )
            else:
                print(
                    f"L'agent commerçant n'a pas assez de {item} pour vendre {quantity} unités"
                )
        else:
            print(
                f"L'agent commerçant n'a pas les compétences nécessaires pour vendre {item}"
            )

    def learn_trading_skill(self, skill: str):
        """
        Apprendre une compétence de commerce.

        :param skill: La compétence de commerce à apprendre.
        """
        self.trading_skills.learn_skill(skill)

    def has_trading_skill(self, skill: str) -> bool:
        """
        Vérifie si l'agent a une compétence de commerce.

        :param skill: La compétence de commerce à vérifier.
        :return: True si l'agent a la compétence, sinon False.
        """
        return self.trading_skills.has_skill(skill)
