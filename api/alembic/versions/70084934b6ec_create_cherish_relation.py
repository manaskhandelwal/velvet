"""create cherish relation

Revision ID: 70084934b6ec
Revises: 76dd9d343d6e
Create Date: 2023-11-19 00:13:19.771571

"""
from __future__ import annotations
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '70084934b6ec'
down_revision: Union[str, None] = '76dd9d343d6e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "cherish_relation",
        sa.Column(
            "id",
            sa.UUID(as_uuid=True),
            nullable=False,
            index=True,
            primary_key=True,
        ),
        sa.Column("user_id", sa.UUID(as_uuid=True)),
        sa.Column("moment_id", sa.UUID(as_uuid=True)),
    )


def downgrade() -> None:
    op.drop_table("cherish_relation")
