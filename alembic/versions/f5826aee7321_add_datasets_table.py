"""Add datasets table

Revision ID: f5826aee7321
Revises: 05e80bef822c
Create Date: 2025-01-14 19:19:51.811494

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision: str = 'f5826aee7321'
down_revision: Union[str, None] = '05e80bef822c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'datasets',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, default=sa.text('uuid_generate_v4()'), index=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('images', sa.String(), nullable=False)
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('datasets')
    # ### end Alembic commands ###
