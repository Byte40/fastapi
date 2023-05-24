"""add foreign-key to posts table

Revision ID: 23fa94d5d890
Revises: 82950b9b6ea0
Create Date: 2023-05-24 13:58:40.441946

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23fa94d5d890'
down_revision = '82950b9b6ea0'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE", onupdate="CASCADE")
    pass


def downgrade():
    op.drop_constraint('posts_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
