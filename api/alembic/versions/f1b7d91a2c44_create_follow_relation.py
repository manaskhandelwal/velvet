"""create follow relation

Revision ID: f1b7d91a2c44
Revises: 70084934b6ec
Create Date: 2023-11-19 08:14:38.477530

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f1b7d91a2c44"
down_revision: Union[str, None] = "70084934b6ec"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "follow_relation",
        sa.Column(
            "id",
            sa.UUID(as_uuid=True),
            nullable=False,
            index=True,
            primary_key=True,
        ),
        sa.Column("user_id", sa.UUID(as_uuid=True)),
        sa.Column("followed_user_id", sa.UUID(as_uuid=True)),
    )

    op.add_column("users", sa.Column("total_following", sa.Integer(), default=0))
    op.add_column("users", sa.Column("total_followers", sa.Integer(), default=0))


def downgrade() -> None:
    op.drop_table("follow_relation")
    op.drop_column("users", "total_following")
    op.drop_column("users", "total_followers")
