"""Initial migration

Revision ID: 9227a145b93f
Revises: 
Create Date: 2024-12-15 13:51:36.331826

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9227a145b93f"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Création de la table agents
    op.create_table(
        "agents",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(255), nullable=False, unique=True),
        sa.Column("properties", sa.JSON, nullable=True),
    )

    # Création de la table universes
    op.create_table(
        "universes",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(255), nullable=False, unique=True),
        sa.Column("description", sa.String(500), nullable=True),
        sa.Column("properties", sa.JSON, default={}),
        sa.Column(
            "color", sa.String(7), nullable=True
        ),  # Couleur hexadécimale (#RRGGBB)
    )


def downgrade() -> None:
    # Suppression des tables dans l'ordre inverse
    op.drop_table("universes")
    op.drop_table("agents")
