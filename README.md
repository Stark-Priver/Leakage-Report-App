💧 Water Leakage Reporting System

  

📌 Project Overview

The Water Leakage Reporting System is a Streamlit web application that allows users to capture images of water leakages and automatically report them with location coordinates. It uses IP-based geolocation and integrates with PyDeck for interactive mapping.

🚀 Features

✅ Capture leakage image using a built-in camera feature 📸✅ Automatic location tracking via IP-based geolocation 🌍✅ Interactive map view to visualize reported leakages 🗺️✅ User-friendly UI with an aesthetic, responsive design 🎨✅ Prevents excessive reports (maximum of 3 per session) 🛑

🏗️ Tech Stack

Frontend: Streamlit

Backend: Python

Libraries: streamlit, geocoder, pandas, pydeck, PIL

📸 Screenshot



🛠️ Installation & Setup

Clone the Repository

git clone https://github.com/your-username/water-leakage-reporting.git
cd water-leakage-reporting

Create a Virtual Environment (Optional but recommended)

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

Install Dependencies

pip install -r requirements.txt

Run the Streamlit App

streamlit run app.py

🎯 How to Use

Open the web app.

Take a picture of the leakage.

Click Report Leakage.

The app automatically fetches your location and displays the reported leakage on the map.

You can report up to 3 leakages per session.

📜 License

This project is licensed under the MIT License.

🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.

📞 Contact

For any queries, feel free to reach out:
📧 Email: your-email@example.com🌍 GitHub: your-username

