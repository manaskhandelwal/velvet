"""create initial user table

Revision ID: 336c9f3d72d0
Revises: 
Create Date: 2023-11-18 02:25:43.688501

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "336c9f3d72d0"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column(
            "id",
            sa.UUID(as_uuid=True),
            nullable=False,
            index=True,
            primary_key=True,
        ),
        sa.Column("full_name", sa.String(), nullable=False, index=True, unique=True),
        sa.Column("username", sa.String(), nullable=False, index=True, unique=True),
        sa.Column("pronouns", sa.String(), nullable=True),
        sa.Column("bio", sa.String(), nullable=True),
        sa.Column("profile_photo", sa.String(), nullable=True),
        sa.Column("email", sa.String(), nullable=False, unique=True),
        sa.Column("email_verified", sa.Boolean(), default=False),
        sa.Column("email_otp", sa.Integer(), nullable=True),
        sa.Column("hashed_password", sa.String(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("users")
