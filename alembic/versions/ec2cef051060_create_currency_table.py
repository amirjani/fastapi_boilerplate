"""create currency table

Revision ID: ec2cef051060
Revises: 9c76a78e9720
Create Date: 2020-10-20 18:17:03.037708

"""
from datetime import datetime
from time import time

from sqlalchemy import text

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec2cef051060'
down_revision = '9c76a78e9720'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "currency",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("code", sa.VARCHAR(3), nullable=False, unique=True),
        sa.Column("name", sa.VARCHAR(64), nullable=False),
        sa.Column("symbol", sa.VARCHAR(16), nullable=False, unique=True),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("deleted_at", sa.TIMESTAMP(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id")
    )

    op.create_index(op.f("index_currency_code"), "currency", ["code"])
    op.create_index(op.f("index_currency_name"), "currency", ["name"])
    op.create_index(op.f("index_currency_symbol"), "currency", ["symbol"])
    op.create_index(op.f("index_currency_created_at"), "currency", ["created_at"])
    op.create_index(op.f("index_currency_deleted_at"), "currency", ["deleted_at"])


def downgrade():
    op.drop_index("index_currency_code", table_name="currency")
    op.drop_index("index_currency_name", table_name="currency")
    op.drop_index("index_currency_symbol", table_name="currency")
    op.drop_index("index_currency_created_at", table_name="currency")
    op.drop_index("index_currency_deleted_at", table_name="currency")
    op.drop_table("currency")
