"""create user_country table

Revision ID: 49985c956d8a
Revises: 29d26721f3d0
Create Date: 2020-11-13 18:41:52.155673

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49985c956d8a'
down_revision = '29d26721f3d0'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "user_country",

        sa.Column("user_id", sa.BigInteger(), nullable=False),
        sa.Column("country_id", sa.BigInteger(), nullable=False),
        sa.Column("is_primary", sa.Boolean(), nullable=False, default=False),

        sa.ForeignKeyConstraint(["user_id"], ["user.id"], ),
        sa.ForeignKeyConstraint(["country_id"], ["country.id"], ),
    )

    op.create_index(op.f("index_user_country_user_id"), "user_country", ["user_id"])
    op.create_index(op.f("index_user_country_country_id"), "user_country", ["country_id"])


def downgrade():
    op.drop_index("index_user_country_user_id", table_name="user_country")
    op.drop_index("index_user_country_country_id", table_name="user_country")
    op.drop_table("user_country")
