"""Initial migration

Revision ID: e0b29b1345fe
Revises: f7e853df757f
Create Date: 2025-01-31 14:45:08.236247

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e0b29b1345fe'
down_revision: Union[str, None] = 'f7e853df757f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
