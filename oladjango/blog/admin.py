from django.contrib import admin

# Register your models here.
from .models import Post
admin.site.register(Post)

from .models import Produto
admin.site.register(Produto)

from .models import Fornecedor
admin.site.register(Fornecedor)

from .Aluno import Aluno
admin.site.register(Aluno)
