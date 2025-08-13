# 🚆 Train Search Web Application (Django)

A single-page train search web application built with **Django** and **Django templates**.  
Users can select **source** and **destination** stations, sort results by **price** or **time**, and view available trains in a clean, responsive UI.

---

## 📌 Features
- Dropdown selection for **source** and **destination** stations.
- Display train details: name, departure time, arrival time, distance, and ticket price.
- Price automatically calculated based on distance (₹1.25/km).
- Sort results by **price** or **time**.
- AJAX-based search — no page reloads.
- Test data generator to quickly populate the database.

---

## 🛠️ Tech Stack
- **Backend:** Django (Python)
- **Frontend:** Django Templates + Bootstrap + JavaScript (fetch API)
- **Database:** SQLite (default, can be swapped with PostgreSQL/MySQL)
- **Others:** Django Management Command for data generation

---

## 📂 Project Structure
train_search/
│
├── trains/ # App
│ ├── templates/trains/ # HTML templates
│ │ ├── home.html
│ │ ├── results_partial.html
│ ├── management/commands/ # Custom commands
│ │ └── generate_test_data.py
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│
├── train_search/ # Django project settings
│ ├── settings.py
│ ├── urls.py
│
├── requirements.txt
├── manage.py
└── README.md

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone <your-repo-url>
cd train_search
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Apply Migrations
python manage.py migrate
5️⃣ Generate Test Data
python manage.py generate_test_data
6️⃣ Run the Development Server
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser.
🔄 Usage
Select source and destination stations from the dropdown.

Choose sort by price or sort by time.

Click Search — results load instantly without reloading the page.
