from django import forms
from .models import UploadedFile
import os

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ('file',)

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            # Get file extension
            ext = os.path.splitext(file.name)[1].lower()
            valid_extensions = ['.xls', '.xlsx', '.csv']
            if ext not in valid_extensions:
                raise forms.ValidationError('Only Excel and CSV files are allowed.')
        return file