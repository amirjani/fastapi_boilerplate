"""create country currency table

Revision ID: 29d26721f3d0
Revises: 4ba9fba98b6b
Create Date: 2020-11-03 12:09:36.978270

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29d26721f3d0'
down_revision = '4ba9fba98b6b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "country_currency",

        sa.Column("country_id", sa.BigInteger(), nullable=False, primary_key=True),
        sa.Column("currency_id", sa.BigInteger(), nullable=False, primary_key=True),

        sa.ForeignKeyConstraint(["country_id"], ["country.id"], ),
        sa.ForeignKeyConstraint(["currency_id"], ["currency.id"], ),
    )

    op.create_index(op.f("index_country_currency_country_id"), "country_currency", ["country_id"])
    op.create_index(op.f("index_country_currency_language_id"), "country_currency", ["currency_id"])


def downgrade():
    op.drop_index("index_country_currency_country_id", table_name="country_currency")
    op.drop_index("index_country_currency_language_id", table_name="country_currency")
    op.drop_table("country_currency")
