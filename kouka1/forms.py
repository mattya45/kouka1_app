from django import forms


class Kouka1Form(forms.Form):
    name = forms.CharField(labal='お名前', max_length=30)
    age = forms.CharField(label='年齢')
    number = forms.CharField(label='電話番号', max_length=11)
    email = forms.EmailField(label='メールアドレス')
    address = forms.CharField(label='住所', max_length=100)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'お名前をここに入力してください。'

        self.fields['age'].widget.attrs['class'] = 'form-control'
        self.fields['age'].widget.attrs['placeholder'] = '年齢をここに入力してください。'

        self.fields['number'].widget.attrs['class'] = 'form-control'
        self.fields['number'].widget.attrs['placeholder'] = '電話番号をここに入力してください。'

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスをここに入力してください。'

        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['placeholder'] = '住所をここに入力してください。'