"""rename_players_initials_to_nickname

Revision ID: 29ab15218b9a
Revises: 2852e76673dd
Create Date: 2015-02-19 12:28:21.963347

"""

# revision identifiers, used by Alembic.
revision = '29ab15218b9a'
down_revision = '2852e76673dd'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('players', 'initials', new_column_name='nickname')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('players', 'nickname', new_column_name='initials')
    ### end Alembic commands ###
