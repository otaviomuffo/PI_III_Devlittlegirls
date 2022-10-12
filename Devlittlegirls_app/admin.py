from django.contrib import admin
from .models import *

# Register your models here.
#admin.site.register(Site)
#admin.site.register(Aluno)

@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ['codsite','nome_site', 'home_page','descricao','logo']
    list_editable = ['nome_site', 'home_page','descricao','logo']

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['codaluno','nome_aluno', 'curso_aluno', 'biografia', 'linkedin', 'foto']
    list_editable = ['nome_aluno', 'curso_aluno', 'biografia', 'linkedin', 'foto']

@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    list_display = ['CodForumItem', 'DescForum']
    list_editable = ['DescForum']