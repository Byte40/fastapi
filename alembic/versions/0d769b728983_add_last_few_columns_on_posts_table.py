"""add last few columns on posts table

Revision ID: 0d769b728983
Revises: 23fa94d5d890
Create Date: 2023-05-24 14:17:41.391566

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d769b728983'
down_revision = '23fa94d5d890'
branch_labels = None
depends_on = None



def upgrade():
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'created_at')
    pass