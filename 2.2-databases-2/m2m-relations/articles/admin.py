from django.contrib import admin
from .models import Article, Tag, Relationship
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):

        count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main') == True:
                count += 1
        if count > 1:
            raise ValidationError('Основным может быть только один раздел')
        elif count == 0:
            raise ValidationError('Укажите основной раздел')
        return super().clean()  # вызываем базовый код переопределяемого метода


class RelationshipInline(admin.TabularInline):
    model = Relationship
    formset = RelationshipInlineFormset
    verbose_name = 'Тематика статьи'
    verbose_name_plural = 'Тематики статьи'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    # list_filter = ['id']
    inlines = [RelationshipInline,]


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title',  'text', 'published_at', 'image']
    # list_filter = ['id']
    inlines = [RelationshipInline,]
