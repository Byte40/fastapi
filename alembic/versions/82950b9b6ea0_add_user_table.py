"""add user table

Revision ID: 82950b9b6ea0
Revises: 6833562f6f7a
Create Date: 2023-05-24 13:44:12.872224

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82950b9b6ea0'
down_revision = '6833562f6f7a'
branch_labels = None
depends_on = None


def upgrade():
    
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
