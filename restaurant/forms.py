from django import forms
from .models import Booking
from datetime import date

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['first_name', 'last_name', 'reservation_date', 'reservation_slot']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}),
            'reservation_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'reservation_slot': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'reservation_date': 'Reservation Date',
            'reservation_slot': 'Reservation Slot',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['reservation_date'].initial = date.today()

    def clean_reservation_date(self):
        reservation_date = self.cleaned_data['reservation_date']
        if reservation_date < date.today():
            raise forms.ValidationError("Cannot book dates in the past.")
        return reservation_date

    def clean(self):
        cleaned_data = super().clean()
        reservation_date = cleaned_data.get('reservation_date')
        reservation_slot = cleaned_data.get('reservation_slot')
        if reservation_date and reservation_slot:
            if Booking.objects.filter(reservation_date=reservation_date, reservation_slot=reservation_slot).exists():
                raise forms.ValidationError("This slot is already booked.")
        return cleaned_data