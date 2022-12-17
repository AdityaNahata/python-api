"""add content column to posts table

Revision ID: 11a9564a38ea
Revises: 8ee89386e044
Create Date: 2022-12-17 17:22:13.654476

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11a9564a38ea'
down_revision = '8ee89386e044'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
