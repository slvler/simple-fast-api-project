"""Create Saved Wallet Table

Revision ID: f3a57c2dfcea
Revises: 327d4854bedb
Create Date: 2025-01-11 16:14:55.213218

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ENUM
from enums.general_status import Status

status_enum = ENUM(Status.USER.value, Status.COMPANY.value, name='general_status', create_type=False)

# revision identifiers, used by Alembic.
revision: str = 'f3a57c2dfcea'
down_revision: Union[str, None] = '327d4854bedb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "saved_wallets",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column("address", sa.String(50), nullable=False),
        sa.Column("asset_id", sa.Integer(), nullable=False),
        sa.Column("network_id", sa.Integer(), nullable=False),
        sa.Column('type', status_enum, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, server_default=sa.func.now(), onupdate=sa.func.now())
    )


def downgrade() -> None:
    op.drop_table('saved_wallets')
    status_enum.drop(op.get_bind())
