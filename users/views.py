from django.contrib.sites import requests
from rest_framework.response import Response
from rest_framework.views import APIView


class UserActivationView(APIView):
    def ActivateUserAccount(request, uidb64=None, token=None):
        # print(force_text(urlsafe_base64_decode(uidb64)))
        # print(token)
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            # print(type(uid),uid)
            user = User.objects.get(pk=uid)
            print(user)
        except User.DoesNotExist:
            user = None
        if user and default_token_generator.check_token(user, token):
            user.is_email_verified = True
            user.is_active = True
            user.save()
            login(request, user)
            print("Activaton done")
        else:
            print("i dont know ")