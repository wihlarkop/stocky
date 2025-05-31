from sqlalchemy import Table, Column, Integer, String, ForeignKeyConstraint

products = Table(
    "products",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False)
)

barcode_data = Table(
    "barcode_data",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("product_id", Integer, nullable=False),
    Column("barcode", String, unique=True, nullable=False),
    Column("source", String, nullable=True),
    ForeignKeyConstraint(
        name="fk_barcode_data_product",
        columns=["product_id"],
        refcolumns=["products.id"]
    )
)
