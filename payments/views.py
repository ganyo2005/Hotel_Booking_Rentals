from django.shortcuts import get_object_or_404, render, redirect
from django.conf import settings
import requests


def initialize_payment(request):

    try:
        url = "https://api.paystack.co/transaction/initialize"

        headers = {
            "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
            "Content-Type": "application/json",
        }

        data = {
            "email": "customer@email.com",
            "amount": 500,  # 5 GHS in pesewas
            "currency": "GHS",
            "callback_url": "http://localhost:8000/"
        }

        response = requests.post(
            url,
            json=data,
            headers=headers,
            timeout=30
        )

        # HANDLE BAD STATUS CODES
        response.raise_for_status()

        res_data = response.json()

        # HANDLE PAYSTACK FAILURE
        if not res_data.get("status"):

            return render(request, "payment_error.html", {
                "error": res_data.get("message", "Payment initialization failed.")
            })

        # HANDLE MISSING DATA
        if "data" not in res_data:

            return render(request, "payment_error.html", {
                "error": "Invalid response from Paystack."
            })

        payment_url = res_data["data"].get("authorization_url")

        # HANDLE EMPTY PAYMENT URL
        if not payment_url:

            return render(request, "payment_error.html", {
                "error": "No payment link returned by Paystack."
            })

        return redirect(payment_url)

    except requests.exceptions.ConnectionError:

        return render(request, "payment_error.html", {
            "error": "Unable to connect to Paystack. Check your internet connection."
        })

    except requests.exceptions.Timeout:

        return render(request, "payment_error.html", {
            "error": "Paystack request timed out. Please try again."
        })

    except requests.exceptions.HTTPError as e:

        return render(request, "payment_error.html", {
            "error": f"HTTP Error: {str(e)}"
        })

    except requests.exceptions.RequestException as e:

        return render(request, "payment_error.html", {
            "error": f"Payment request failed: {str(e)}"
        })

    except Exception as e:

        return render(request, "payment_error.html", {
            "error": f"Something went wrong: {str(e)}"
        })




