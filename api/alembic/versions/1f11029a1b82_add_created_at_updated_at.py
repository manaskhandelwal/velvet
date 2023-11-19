"""add created_at & updated_at

Revision ID: 1f11029a1b82
Revises: e70f6100eaaf
Create Date: 2023-11-19 21:58:12.826103

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1f11029a1b82"
down_revision: Union[str, None] = "e70f6100eaaf"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

tables = ["users", "moments", "cherish_relation", "follow_relation"]


def upgrade() -> None:
    created_at = sa.Column("created_at", sa.DateTime())
    updated_at = sa.Column("updated_at", sa.DateTime())

    for table in tables:
        op.add_column(table, created_at)
        op.add_column(table, updated_at)


def downgrade() -> None:
    for table in tables:
        op.drop_column(table, "created_at")
        op.drop_column(table, "updated_at")
