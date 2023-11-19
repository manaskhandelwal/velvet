"""create moment table

Revision ID: 76dd9d343d6e
Revises: 336c9f3d72d0
Create Date: 2023-11-19 00:11:15.625461

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '76dd9d343d6e'
down_revision: Union[str, None] = '336c9f3d72d0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "moments",
        sa.Column(
            "id",
            sa.UUID(as_uuid=True),
            nullable=False,
            index=True,
            primary_key=True,
        ),
        sa.Column(
            "user_id",
            sa.UUID(as_uuid=True),
            nullable=False,
            index=True,
        ),
        sa.Column("message", sa.String(), nullable=True),
        sa.Column("photo", sa.String(), nullable=True),
    )


def downgrade() -> None:
    op.drop_table("moments")
