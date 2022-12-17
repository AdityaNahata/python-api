"""adding foreign key to posts table

Revision ID: 42fd637bf185
Revises: eed3679bf7ee
Create Date: 2022-12-17 17:37:04.872161

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42fd637bf185'
down_revision = 'eed3679bf7ee'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table='posts', referent_table='users', local_cols=[
                          'user_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts','user_id')
    pass
