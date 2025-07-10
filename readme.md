# 🌦️ Weather Forecast Web App

A responsive and interactive **Weather Forecast Web Application** built using **Flask**, styled with **HTML/CSS**, and containerized using **Docker**. The application fetches live weather data from a public API and can be deployed locally or on the cloud using **IBM Cloud Container Registry**.

---

## 📌 Features

- 🔍 Search weather by **city name**
- 📱 Fully **responsive** UI for mobile & desktop
- 🌤️ Real-time weather info: temperature, humidity, wind, precipitation
- 🐳 Dockerized for smooth deployment
- ☁️ Ready to push to IBM Cloud Container Registry

---

## 🖼️ Preview

<p align="center">
  <img src="static\images\image1.png" width="600"/>
  <br/>
  <img src="static\images\image2.png" width="600"/>
  <i>Figure 2: UI OF application</i>
</p>
 <!-- Replace with your image path -->

---

## ⚙️ Technologies Used

- **Frontend:** HTML, CSS, Icons, Animations
- **Backend:** Python, Flask
- **API:** OpenWeatherMap or similar
- **Containerization:** Docker
- **Cloud (Optional):** IBM Cloud Container Registry

---

## 🚀 Getting Started

### 📦 Prerequisites

- Python 3.x
- Docker installed
- (Optional) IBM Cloud CLI

### 🧪 Local Setup


    git clone https://github.com/ArisuAbhilash/weather-application-.git

    cd weather-app

    pip install -r requirements.txt

    python app.py
   
    http://localhost:4449


### 🐳 Docker Instructions

### 🏗️ Build Docker Image

    docker build -t weather-app .

▶️ Run Docker Container

    docker run -p 4449:4449 weather-app

☁️ IBM Cloud Deployment (Optional)

Install IBM CLI plugins:

    ibmcloud plugin install container-registry -f

Set target and region:

    ibmcloud login

    ibmcloud target -g Default

    ibmcloud cr region-set eu-central

Push to IBM Cloud Container Registry:

    ibmcloud cr login

    ibmcloud cr namespace-add abhilash-sec88

    docker tag weather-app de.icr.io/abhilash-sec88/weather-app:1.0

    docker push de.icr.io/abhilash-sec88/weather-app:1.0

### 📁 Project Structure

weather-app/</br>
│</br>
├── static/</br>
│   └── css/</br>
│       └── style.css</br>
├── templates/</br>
│   └── index.html</br>
├── app.py</br>
├── requirements.txt</br>
├── Dockerfile</br>
└── README.md</br>

### 🙋‍♂️ Author

Abhilash Maurya

🌐 Live Demo

(Optional: Add Code Engine or localhost tunnel URL if deployed)

