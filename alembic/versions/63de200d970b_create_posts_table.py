"""create posts table

Revision ID: 63de200d970b
Revises: 
Create Date: 2023-05-24 12:34:51.329014

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63de200d970b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False),
                    sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
