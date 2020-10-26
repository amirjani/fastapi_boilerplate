from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb46825a41d9'
down_revision = 'f0850bce3024'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "role",
        sa.Column("id", sa.Integer(), nullable=False),

        sa.Column("is_primary", sa.Boolean(), nullable=False, default=False),
        sa.Column("name", sa.VARCHAR(32), nullable=False),

        sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("deleted_at", sa.TIMESTAMP(timezone=True), nullable=True),

        sa.PrimaryKeyConstraint("id")
    )

    op.create_index(op.f("index_role_is_primary"), "role", ["is_primary"])
    op.create_index(op.f("index_role_name"), "role", ["name"])
    op.create_index(op.f("index_role_created_at"), "role", ["created_at"])
    op.create_index(op.f("index_role_deleted_at"), "role", ["deleted_at"])


def downgrade():
    op.drop_index("index_role_is_primary", table_name="role")
    op.drop_index("index_role_name", table_name="role")
    op.drop_index("index_role_created_at", table_name="role")
    op.drop_index("index_role_deleted_at", table_name="role")
    op.drop_table("role")
