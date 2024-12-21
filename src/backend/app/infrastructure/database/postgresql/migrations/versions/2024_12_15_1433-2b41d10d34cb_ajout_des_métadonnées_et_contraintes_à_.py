"""Ajout des métadonnées et contraintes à l'agent

Revision ID: 2b41d10d34cb
Revises: 9227a145b93f
Create Date: 2024-12-15 14:33:44.008014

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "2b41d10d34cb"
down_revision: Union[str, None] = "9227a145b93f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Ajout de contraintes et modification de la table "agents"
    op.alter_column(
        "agents",
        "name",
        existing_type=sa.String(),
        nullable=False,
        comment="Nom de l'agent (obligatoire)",
    )
    op.alter_column(
        "agents",
        "properties",
        existing_type=sa.JSON(),
        nullable=True,
        comment="Propriétés de l'agent au format JSON",
    )
    op.create_index(
        "ix_agents_name",
        "agents",
        ["name"],
        unique=True,
        postgresql_where=sa.text("name IS NOT NULL"),
    )


def downgrade() -> None:
    # Suppression des modifications en cas de rollback
    op.drop_index("ix_agents_name", table_name="agents")
    op.alter_column("agents", "name", existing_type=sa.String(), nullable=True)
    op.alter_column("agents", "properties", existing_type=sa.JSON(), nullable=True)
