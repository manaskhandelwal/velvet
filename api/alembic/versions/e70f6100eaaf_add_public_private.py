"""add public private

Revision ID: e70f6100eaaf
Revises: f1b7d91a2c44
Create Date: 2023-11-19 09:35:50.460867

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e70f6100eaaf"
down_revision: Union[str, None] = "f1b7d91a2c44"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users", sa.Column("private", sa.Boolean(), default=False))
    op.add_column("moments", sa.Column("private", sa.Boolean(), default=False))


def downgrade() -> None:
    op.drop_column("users", "private")
    op.drop_column("moments", "private")
