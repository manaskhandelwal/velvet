"""add total_cherishes to moment

Revision ID: 7a73cede577b
Revises: 1f11029a1b82
Create Date: 2023-11-20 01:27:04.402324

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "7a73cede577b"
down_revision: Union[str, None] = "1f11029a1b82"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("moments", sa.Column("total_cherishes", sa.Integer(), default=0))


def downgrade() -> None:
    op.drop_column("moments", "total_cherishes")
