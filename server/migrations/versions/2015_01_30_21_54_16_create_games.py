"""create games

Revision ID: 3813dda101c4
Revises: None
Create Date: 2015-01-30 21:54:16.595818

"""

# revision identifiers, used by Alembic.
revision = '3813dda101c4'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('games',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('team1defense', sa.String(), nullable=True),
    sa.Column('team1offense', sa.String(), nullable=True),
    sa.Column('team1score', sa.Integer(), nullable=True),
    sa.Column('team2offense', sa.String(), nullable=True),
    sa.Column('team2defense', sa.String(), nullable=True),
    sa.Column('team2score', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('games')
