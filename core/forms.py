from django import forms
from .models import Review, ServiceRequest, User, Mechanic # Import User and Mechanic

class ReviewForm(forms.ModelForm):
    rating = forms.IntegerField(widget=forms.HiddenInput(), required=True)
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), required=True)
    
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rating'].label = "Rating"
        self.fields['comment'].label = "Your Comments"
        self.fields['rating'].help_text = "Click on the stars to rate your experience"
        self.fields['comment'].help_text = "Please share your experience with the service"

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['vehicle_type', 'issue_description', 'issue_image', 'issue_video', 'issue_file', 'location', 'latitude', 'longitude']
        widgets = {
            'issue_description': forms.Textarea(attrs={'rows': 4}),
        }

class OtpForm(forms.Form):
    otp = forms.CharField(max_length=6, required=True)

class NewPasswordForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput, label="New Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if new_password and confirm_password and new_password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'profile_picture', 'preferred_language']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
        }

class MechanicProfileForm(forms.ModelForm):
    class Meta:
        model = Mechanic
        fields = ['specialization', 'experience_years', 'workshop_address', 'latitude', 'longitude', 'available', 'preferred_language']
        widgets = {
            'workshop_address': forms.Textarea(attrs={'rows': 3}),
        }
