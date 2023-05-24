"""add published column to posts table

Revision ID: 6833562f6f7a
Revises: 63de200d970b
Create Date: 2023-05-24 12:59:49.256539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6833562f6f7a'
down_revision = '63de200d970b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='True'))
    pass


def downgrade():
    op.drop_table('posts', 'published')
    pass
