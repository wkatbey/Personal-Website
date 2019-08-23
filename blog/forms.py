from django import forms
from django.forms import ModelForm
from blog.models import BlogEntry, Category
from datetime import datetime

class BlogEntryForm(ModelForm):
    class Meta:
        model = BlogEntry
        fields = (
            'title',
            #'primary_image',
            'text_entry',
            'category'
        )

        widgets = {
            'text_entry': forms.TextInput(
                attrs = {
                    'type': 'hidden',
                }
            ),
            'title': forms.TextInput(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'category': forms.Select(
                attrs = {
                    'class': 'form-control'
                },
                choices = Category.objects.all()
            )
        }

    def save(self, commit=True):
        blog_instance = super(BlogEntryForm, self).save(commit=False)
        blog_instance.date_of_submission = datetime.now()
        blog_instance.date_updated = datetime.now()

        return blog_instance
