"""empty message

Revision ID: 16c4c1f7480d
Revises: 7302a24c95ae
Create Date: 2023-04-21 23:42:06.278679

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16c4c1f7480d'
down_revision = '7302a24c95ae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('lastname', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'lastname')
    # ### end Alembic commands ###
