from sqlalchemy import Table, Column, Integer, String, Date, ForeignKeyConstraint

batches = Table(
    "batches",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("product_id", Integer, nullable=False),
    Column("quantity", Integer, nullable=False),
    Column("purchase_date", Date, nullable=False),
    Column("expiry_date", Date, nullable=True),
    ForeignKeyConstraint(
        name="fk_batches_product",
        columns=["product_id"],
        refcolumns=["products.id"]
    )
)

stock_movements = Table(
    "stock_movements",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("product_id", Integer, nullable=False),
    Column("purchase_date", Date, nullable=False),
    Column("quantity", Integer, nullable=False),
    Column("movement_type", String, nullable=False),  # "IN" / "OUT"
    ForeignKeyConstraint(
        name="fk_stock_movements_product",
        columns=["product_id"],
        refcolumns=["products.id"]
    )
)
