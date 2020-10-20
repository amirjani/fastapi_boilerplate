"""create country table

Revision ID: 9c76a78e9720
Revises: 01796e80fda3
Create Date: 2020-10-10 22:14:03.452465

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
from app.models.country import RegionEnum
from datetime import datetime

revision = '9c76a78e9720'
down_revision = '01796e80fda3'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "country",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column("code", sa.VARCHAR(3), nullable=True),
        sa.Column("calling_code", sa.Integer(), nullable=True),
        sa.Column("region", sa.VARCHAR(20), nullable=True),
        sa.Column("translation", sa.JSON(), nullable=True),
        sa.Column("flag", sa.String(), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(), nullable=False, default=datetime.now().timestamp()),
        sa.Column("updated_at", sa.TIMESTAMP(), nullable=True),
        sa.Column("deleted_at", sa.TIMESTAMP(), nullable=True),
        sa.PrimaryKeyConstraint("id")
    )

    op.create_index(op.f("index_country_code"), "country", ["code"], unique=True)
    op.create_index(op.f("index_country_calling_code"), "country", ["calling_code"], unique=True)
    op.create_index(op.f("index_country_id"), "country", ["id"], unique=True)


def downgrade():
    op.drop_index("index_country_id", table_name="country")
    op.drop_index("index_country_calling_code", table_name="country")
    op.drop_index("index_country_code", table_name="country")
    op.drop_table("country")

