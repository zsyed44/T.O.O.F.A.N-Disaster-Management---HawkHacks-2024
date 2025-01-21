# TOOFAN - AI-Powered Disaster Response Rover

## Overview
TOOFAN is an AI-powered Arduino car designed for disaster response and survivor assistance. Equipped with danger zone detection and a helper chat feature, TOOFAN leverages sensors and machine learning to identify hazards, navigate disaster-stricken areas, and provide real-time communication with survivors. This innovative project integrates advanced technology into a compact and versatile platform, enhancing search and rescue operations.

## 🔗 Links
- [TOOFAN Webpage](#)
- [GitHub Repository](#)

---

## 🌍 Inspiration
As engineers from regions frequently affected by natural disasters—earthquakes, floods, and landslides—we understand the devastating impact these events have on communities. From the loss of property to tragic fatalities, the aftermath of disasters can be overwhelming.

Driven by our commitment to engineering solutions for social good, we developed TOOFAN to aid in disaster recovery. While we cannot prevent natural disasters, we aim to minimize their impact by improving resilience and providing immediate assistance to those in need.

---

## 🚀 What TOOFAN Does
TOOFAN is designed to operate in disaster-stricken environments, offering the following capabilities:
- **Rugged Navigation**: Built to traverse rough terrains and debris, TOOFAN operates within a 100-meter radius.
- **Hazard Detection**: Uses sensors and AI to assess structural integrity, detect human presence, and evaluate environmental conditions.
- **Survivor Assistance**:
  - Engages in conversations with survivors to provide comfort and guidance.
  - Sends distress signals if survivors require urgent rescue.
  - Uses a state machine-based ChatBot to interact empathetically.
- **Real-Time Communication**: Provides continuous monitoring and reporting to rescue teams via a secure network.

---

## 🛠 How We Built It
**MANY OF THESE ARE STILL BEING REFINED AND WORKED ON**
We divided the development into key components:
### **1️⃣ Rover Assembly**
- Started with an RC car chassis and upgraded it for durability.
- Used **two motor drivers** to enhance wheel power for rough terrain.
- Replaced the Arduino Uno with an **ESP32 Microcontroller** to enable Bluetooth, WiFi, and faster processing.
- Integrated **Dabble**, an open-source Bluetooth controller app, for easy control.

### **2️⃣ Radar System**
- Utilized an **ultrasonic sensor** mounted on a servo motor to scan the environment.
- Developed a **Java-based radar application**, displaying real-time obstacle detection.
- Integrated USB-based data transmission for smooth operation.

### **3️⃣ Facial Recognition Software**
- Leveraged **YoloWorld libraries** for object detection and facial recognition.
- Used **preloaded datasets and neural networks** to identify objects and detect distress signals.
- Implemented a notification system to alert operators when a phone or survivor is detected.

### **4️⃣ AI Neural Network for Hazard Mapping**
- Trained an AI model using **2,500 satellite images** of damaged and intact buildings.
- Achieved **96% accuracy** in predicting hazardous areas.
- Future goal: Integrate lower-view images for enhanced decision-making.

### **5️⃣ ChatBot for Survivor Interaction**
- Developed using a **State Machine Design Pattern** to enable structured conversations.
- Determines when to assist directly or escalate a distress signal.
- Future goal: Enhance with **Conversational AI** and integrate **GPS tracking** for precise survivor location reporting.

---

## 🎉 Accomplishments We're Proud Of
- Built an **autonomous rover** capable of traversing disaster zones.
- Integrated **AI-powered hazard detection** and **facial recognition**.
- Developed a **real-time ChatBot** for survivor assistance.
- Achieved **96% accuracy** in predicting hazardous zones.
- Created a **functional radar system** with a Java-based UI.

---

## 🔮 What's Next?
### **Car & Radar Improvements**
- Upgrade to **higher-precision ultrasonic sensors** for extended range and accuracy.
- Integrate **thermal cameras** for human detection in low-visibility environments.
- Implement **autonomous AI navigation** for better decision-making in disaster zones.

### **Neural Network Enhancements**
- Expand dataset with **ground-level images** to improve prediction accuracy.

### **ChatBot Evolution**
- Transition from a **state machine model to a Conversational AI system**.
- Integrate **GPS tracking** for precise survivor location identification.

---

## 👥 Team
We are a group of four engineers from **The University of Western Ontario**, dedicated to using technology for humanitarian impact. Our expertise spans AI, embedded systems, and robotics, enabling us to build a solution with real-world applications.

---

🚀 **Together, let's build technology that saves lives!**

