import firebase_admin
from firebase_admin import credentials, messaging
import os

# Path to your service account key file
# Ensure this file is kept secure and not committed to public repositories
SERVICE_ACCOUNT_KEY_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'serviceAccountKey.json')

if not firebase_admin._apps:
    try:
        cred = credentials.Certificate(SERVICE_ACCOUNT_KEY_PATH)
        firebase_admin.initialize_app(cred)
        print("Firebase Admin SDK initialized successfully.")
    except FileNotFoundError:
        print(f"Error: serviceAccountKey.json not found at {SERVICE_ACCOUNT_KEY_PATH}. Please ensure it's in the project root.")
    except Exception as e:
        print(f"Error initializing Firebase Admin SDK: {e}")

def send_notification(fcm_token, title, body, data=None):
    """Sends a push notification to a specific FCM token."""
    if not firebase_admin._apps:
        print("Firebase Admin SDK not initialized. Cannot send notification.")
        return

    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body,
        ),
        data=data,
        token=fcm_token,
    )

    try:
        response = messaging.send(message)
        print(f"Successfully sent message: {response}")
        return True
    except Exception as e:
        print(f"Error sending message: {e}")
        return False
