from django.core.validators import RegexValidator

phone_regex = RegexValidator('09([0-9][0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}', message='لطفا شناره تلفن صحیح وارد کنید شماره تلفن شما اشتباه است دوست من ')
