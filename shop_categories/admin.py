from treeadmin.admin import TreeAdmin

class ProductCategoryAdmin(TreeAdmin):
    exclude = ('path',)
    list_display = ('name', 'active', 'path')
