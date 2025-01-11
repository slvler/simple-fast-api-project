"""Create Bank Account Table

Revision ID: 327d4854bedb
Revises: 4cdc4965f8f3
Create Date: 2025-01-11 16:14:43.873545

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ENUM
from enums.general_status import Status

status_enum = ENUM(Status.USER.value, Status.COMPANY.value, name='general_status', create_type=False)

# revision identifiers, used by Alembic.
revision: str = '327d4854bedb'
down_revision: Union[str, None] = '4cdc4965f8f3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "bank_accounts",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("currency_id", sa.Integer(), nullable=False),
        sa.Column("label", sa.String(50), nullable=False),
        sa.Column("iban", sa.String(50), nullable=False),
        sa.Column("bank_name", sa.String(50), nullable=False),
        sa.Column("bank_account", sa.String(50), nullable=False),
        sa.Column("swift_number", sa.String(50), nullable=False),
        sa.Column('type', status_enum, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, server_default=sa.func.now(), onupdate=sa.func.now())
    )


def downgrade() -> None:
    op.drop_table('bank_accounts')
    status_enum.drop(op.get_bind())
