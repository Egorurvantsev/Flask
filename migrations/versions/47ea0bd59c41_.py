"""empty message

Revision ID: 47ea0bd59c41
Revises: bed8f0772cc4
Create Date: 2023-04-26 20:12:35.763383

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47ea0bd59c41'
down_revision = 'bed8f0772cc4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('articles', sa.Column('title', sa.String(length=255), nullable=True))
    op.add_column('articles', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('articles', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.alter_column('articles', 'author_id',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.Integer(),
               nullable=False)
    op.alter_column('articles', 'text',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.Text(),
               existing_nullable=True)
    op.drop_constraint(None, 'articles', type_='foreignkey')
    op.create_foreign_key(None, 'articles', 'authors', ['author_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'articles', type_='foreignkey')
    op.create_foreign_key(None, 'articles', 'users', ['author_id'], ['id'])
    op.alter_column('articles', 'text',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=255),
               existing_nullable=True)
    op.alter_column('articles', 'author_id',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(length=255),
               nullable=True)
    op.drop_column('articles', 'updated_at')
    op.drop_column('articles', 'created_at')
    op.drop_column('articles', 'title')
    # ### end Alembic commands ###
