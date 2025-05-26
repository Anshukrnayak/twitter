from .models import Post, Comment,Profile
from django import forms

from django import forms
from .models import Profile
from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'bio', 'profile_pic']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Last Name'
            }),
            'bio': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Tell us about yourself...',
                'rows': 4
            }),
            'profile_pic': forms.FileInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-md bg-white text-gray-700 cursor-pointer focus:outline-none'
            }),
        }



from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'post_image']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full mt-2 p-2 border border-gray-200 rounded-lg resize-none focus:outline-none focus:ring-2 focus:ring-blue-500',
                'rows': 3,
                'placeholder': "What's happening?",
                'maxlength': 280
            }),

        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = ""
        self.fields['post_image'].label = ""

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content or len(content.strip()) < 20:
            raise forms.ValidationError('Content must be at least 20 characters long.')
        return content


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={
                'class': 'w-full mt-2 p-2 border border-gray-200 rounded-lg resize-none focus:outline-none focus:ring-2 focus:ring-blue-500',
                'rows': 2,
                'placeholder': "Write a comment..."
            }),
            'post': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['comment'].label = ""

    def clean_comment(self):
        comment = self.cleaned_data.get('comment')
        if not comment or len(comment.strip()) <= 10:
            raise forms.ValidationError('Comment must be more than 10 characters.')
        return comment
