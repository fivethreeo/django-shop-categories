from treeadmin.admin import TreeAdmin

class ProductCategoryAdmin(TreeAdmin):
    exclude = ('path', 'name_path')
    list_display = ('name', 'active', 'path')
    prepopulated_fields = {"slug": ("name",)}    
