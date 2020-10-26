from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50d2e4a63143'
down_revision = 'd139d5766e77'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "user_permission",

        sa.Column("user_id", sa.BigInteger(), nullable=False),
        sa.Column("permission_id", sa.BigInteger(), nullable=False),

        sa.ForeignKeyConstraint(["user_id"], ["user.id"], ),
        sa.ForeignKeyConstraint(["permission_id"], ["permission.id"], ),
    )

    op.create_index(op.f("index_user_permission_user_id"), "user_permission", ["user_id"])
    op.create_index(op.f("index_user_permission_permission_id"), "user_permission", ["permission_id"])


def downgrade():
    op.drop_index("index_user_permission_user_id", table_name="user_permission")
    op.drop_index("index_user_permission_user_id", table_name="user_permission")
    op.drop_table("user_permission")

