# 📸 localCam

**Peer-to-peer webcam streaming using WebRTC and a local Python HTTPS server**

---

## 🚀 Quick Start

1. **Start the HTTPS server:**

   ```bash
   python3 https_server.py
   ```

2. **Open the app in browsers on two devices:**

   ```
   https://your_IP:8000/
   ```

   > ⚠️ Accept the self-signed certificate if prompted. Make sure both devices are on the same local network.

3. **Establish WebRTC connection:**

   - On the **Server** (Device A):
     - Start the stream.
     - Click **"Create Offer"**
     - Copy the generated **offer JSON**

   - On the **Client** (Device B):
     - Paste the offer JSON
     - Click **"Paste Offer"**
     - This will generate the **answer JSON**

   - Back on the **Server**:
     - Paste the answer JSON
     - Click **"Confirm"**

   ✅ Video stream should now appear on the client side.

---

## 🌐 Try Online (experimental)

You may also try the interface via GitHub Pages:

```
https://andriitishchenko.github.io/localCam/
```

> ⚠️ Online version may not work due to browser security policies and lack of local server.

---

## 📁 Project Structure

```
localCam/
├── https_server.py       # HTTPS server for local testing
├── cert.pem              # SSL certificate (self-signed)
├── key.pem               # SSL key
├── index.html            # Main frontend page
├── script.js             # WebRTC logic and UI handlers
└── style.css             # Basic styling
```

---

## 🛠 Requirements

- Python 3
- OpenSSL (if you need to generate your own SSL cert/key)

To generate a self-signed certificate:

```bash
openssl req -new -x509 -keyout key.pem -out cert.pem -days 365 -nodes
```

---

## 📄 License

MIT License — free to use, modify, and share.