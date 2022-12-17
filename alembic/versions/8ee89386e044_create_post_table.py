"""create post table

Revision ID: 8ee89386e044
Revises:
Create Date: 2022-12-16 18:09:42.263390

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ee89386e044'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(),
                    nullable=False, primary_key=True),
                    sa.Column('title', sa.String(),
                    nullable=False)
                    )
    pass


def downgrade():
    op.drop_table('posts')
    pass
