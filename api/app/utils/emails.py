import requests

from core.config import settings

async def send_email(data):
  headers = {
      "accept": "application/json",
      "api-key": settings.BREVO_API_KEY,
      "content-type": "application/json",
  }

  requests.post(settings.BREVO_API_ENDPOINT, headers=headers, json=data)

async def send_otp_email(to, otp):
  data = {
      "to": [to],
      "templateId": 1,
      "params": {"OTP": otp},
  }

  await send_email(data)