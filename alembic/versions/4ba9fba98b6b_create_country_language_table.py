"""create country language table

Revision ID: 4ba9fba98b6b
Revises: f43ca57f0770
Create Date: 2020-11-02 20:08:41.841355

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ba9fba98b6b'
down_revision = 'f43ca57f0770'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "country_language",

        sa.Column("country_id", sa.BigInteger(), nullable=False, primary_key=True),
        sa.Column("language_id", sa.BigInteger(), nullable=False, primary_key=True),

        sa.ForeignKeyConstraint(["country_id"], ["country.id"], ),
        sa.ForeignKeyConstraint(["language_id"], ["language.id"], ),
    )

    op.create_index(op.f("index_country_language_country_id"), "country_language", ["country_id"])
    op.create_index(op.f("index_country_language_language_id"), "country_language", ["language_id"])


def downgrade():
    op.drop_index("index_country_language_country_id", table_name="country_language")
    op.drop_index("index_country_language_language_id", table_name="country_language")
    op.drop_table("country_language")
