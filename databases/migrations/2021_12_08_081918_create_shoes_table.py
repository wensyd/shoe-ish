"""CreateShoesTable Migration."""

from masoniteorm.migrations import Migration


class CreateShoesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("shoes") as table:
            table.increments("id")
            table.string("image")
            table.string("title")
            table.string("description")
            table.integer("price")
            table.integer("size")
            table.boolean("purchased").default(False)
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("shoes")
