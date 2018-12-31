"""initial migration

Revision ID: d6cd648e49a5
Revises: 
Create Date: 2018-12-30 20:46:26.872288

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd6cd648e49a5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('comment', 'name',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
    op.alter_column('post', 'title',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
    op.alter_column('tag', 'title',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
    op.create_unique_constraint(None, 'tag', ['title'])
    op.alter_column('user', 'username',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.alter_column('user', 'username',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)
    op.drop_constraint(None, 'tag', type_='unique')
    op.alter_column('tag', 'title',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)
    op.alter_column('post', 'title',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)
    op.alter_column('comment', 'name',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)
    # ### end Alembic commands ###
