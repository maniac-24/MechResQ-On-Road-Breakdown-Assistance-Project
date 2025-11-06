// Import Firebase scripts
importScripts('https://www.gstatic.com/firebasejs/9.6.0/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/9.6.0/firebase-messaging-compat.js');

// Initialize Firebase
firebase.initializeApp({
  apiKey: "AIzaSyC0nam8QexsAyzaazH0Tz66kmzTDt80pDM",
  authDomain: "mechresq.firebaseapp.com",
  projectId: "mechresq",
  storageBucket: "mechresq.firebasestorage.app",
  messagingSenderId: "704898419224",
  appId: "1:704898419224:web:746456b544ce2fa988d16d"
});

// Retrieve an instance of Firebase Messaging
const messaging = firebase.messaging();

// Handle background messages
messaging.onBackgroundMessage(function (payload) {
  console.log('[firebase-messaging-sw.js] Received background message ', payload);
  const notificationTitle = payload.notification.title;
  const notificationOptions = {
    body: payload.notification.body,
    icon: '/static/images/icon.png' // optional, assuming an icon in static/images
  };
  self.registration.showNotification(notificationTitle, notificationOptions);
});
