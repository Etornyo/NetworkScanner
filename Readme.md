# **Office Network IP Tracker**

## **Overview**
A Python tool to monitor and log devices on your office LAN. Tracks IP addresses, timestamps, and hostnames, validates naming conventions, and provides geolocation data for public IPs.

---

## **Features**
- Tracks devices joining the network in real time.
- Validates device naming conventions.
- Logs IP addresses, hostnames, timestamps, and geolocations.
- Generates visual reports of device activity.

---

## **Setup**
1. Enable SNMP on your network devices.
2. Clone the repository:
   ```bash
   git clone https://github.com/username/office-network-ip-tracker.git
   cd office-network-ip-tracker
   ```
3. Install dependencies:
   ```bash
   pip install pysnmp requests geoip2 sqlalchemy pandas matplotlib
   ```
4. Configure `config.json` with your network details.

---

## **Run the Application**
Start monitoring:
```bash
python main.py
```

---

## **Reports**
Generate and view device activity reports:
```bash
python reporting.py
```

---

## **License**
MIT License

---