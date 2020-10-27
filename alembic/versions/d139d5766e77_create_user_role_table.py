from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd139d5766e77'
down_revision = '5dae9a17f9d6'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "user_role",

        sa.Column("user_id", sa.BigInteger(), nullable=False, primary_key=True),
        sa.Column("role_id", sa.BigInteger(), nullable=False, primary_key=True),

        sa.ForeignKeyConstraint(["user_id"], ["user.id"], ),
        sa.ForeignKeyConstraint(["role_id"], ["role.id"], ),
    )

    op.create_index(op.f("index_user_role_user_id"), "user_role", ["user_id"])
    op.create_index(op.f("index_user_role_role_id"), "user_role", ["role_id"])


def downgrade():
    op.drop_index("index_user_role_user_id", table_name="user_role")
    op.drop_index("index_user_role_role_id", table_name="user_role")
    op.drop_table("user_role")

