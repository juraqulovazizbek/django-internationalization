# 🌐 Personal Portfolio & Blog System

Template-based Django Project

---

## 🎯 Loyihaning Maqsadi

Ushbu loyiha shaxsiy portfolio va blog tizimi bo‘lib, foydalanuvchining:

* O‘zi haqida ma’lumot
* Qilgan ishlarini (portfolio)
* Yangiliklari / blog postlari
* Aloqa ma’lumotlari

ni boshqarish imkonini beradi.

Loyiha Django + Template asosida qurilgan va production-ready arxitekturaga ega.

---

## ⚠ Muhim Cheklovlar

❌ REST API yo‘q
❌ Django Rest Framework yo‘q
❌ Authentication tizimi yo‘q (faqat admin)
✅ Faqat Django + Templates
✅ Faqat CRUD + Basic logic
✅ Admin orqali kontent boshqaruvi

---

## 🧠 O‘rganiladigan Asosiy Ko‘nikmalar

* Django project/app strukturasi
* Model dizayni
* ForeignKey munosabat
* Media fayllar bilan ishlash
* Template rendering
* URL → View → Template flow
* CRUD operatsiyalar
* Basic validatsiya
* Ko‘p tilli tizim (i18n – tayyor)

---

# 🏗 Loyiha Strukturasi

```
personal_site/
├── config/               # Django project settings
├── apps/
│   ├── core/             # Home, About, Contact
│   ├── blog/             # Postlar
│   ├── portfolio/        # Qilingan ishlar
│   └── pages/            # Statik sahifalar (ixtiyoriy)
├── templates/
│   ├── base.html
│   ├── core/
│   ├── blog/
│   └── portfolio/
├── static/
├── media/
└── manage.py
```

---

# 📦 Ma’lumotlar Bazasi Modellari

---

## 1️⃣ Profile Model (core/models.py)

Shaxsiy ma’lumotlar.

| Field      | Type           | Majburiy |
| ---------- | -------------- | -------- |
| full_name  | CharField(150) | ✅        |
| bio        | TextField      | ❌        |
| avatar     | ImageField     | ❌        |
| created_at | DateTimeField  | auto     |

Qoidalar:

* `__str__()` → full_name

---

## 2️⃣ Post Model (blog/models.py)

Yangiliklar / hayot postlari.

| Field        | Type           | Majburiy |
| ------------ | -------------- | -------- |
| title        | CharField(200) | ✅        |
| content      | TextField      | ✅        |
| image        | ImageField     | ❌        |
| created_at   | DateTimeField  | auto     |
| is_published | BooleanField   | ✅        |

Qoidalar:

* is_published = False bo‘lsa front’da chiqmaydi
* `__str__()` → title

---

## 3️⃣ Project Model (portfolio/models.py)

Portfolio / qilgan ishlar.

| Field       | Type           | Majburiy |
| ----------- | -------------- | -------- |
| title       | CharField(200) | ✅        |
| description | TextField      | ✅        |
| tech_stack  | CharField(255) | ❌        |
| image       | ImageField     | ❌        |
| link        | URLField       | ❌        |
| created_at  | DateTimeField  | auto     |

Qoidalar:

* `__str__()` → title

---

# 🌐 URL & VIEW TALABLARI

---

## 🏠 Core Pages

### 1. Bosh sahifa

GET /

Ko‘rsatadi:

* Profil ma’lumotlari
* Oxirgi 3 ta post
* Oxirgi 3 ta project

---

### 2. About sahifasi

GET /about/

---

### 3. Contact sahifasi

GET /contact/

---

# 📰 Blog Pages

### 1. Postlar ro‘yxati

GET /blog/

Ko‘rsatadi:

* title
* created_at
* qisqa preview
* detail tugma

---

### 2. Post detail

GET /blog/<id>/

Ko‘rsatadi:

* to‘liq post
* rasm (agar mavjud bo‘lsa)

---

# 💼 Portfolio Pages

### 1. Project ro‘yxati

GET /portfolio/

Ko‘rsatadi:

* project nomi
* texnologiyalar
* detail tugma

---

### 2. Project detail

GET /portfolio/<id>/

---

# 🧩 Template TALABLARI

* base.html bo‘lishi shart
* Barcha sahifalar extends base.html
* Navbar (Home, Blog, Portfolio, Contact)
* Minimal styling
* Card dizayn
* Error message ko‘rinishi aniq bo‘lishi kerak

---

# 🌍 Ko‘p tilli qo‘llab-quvvatlash

Tillar:

* Uzbek
* Russian
* English

Buyruqlar:

```
python manage.py makemessages -l en
python manage.py makemessages -l ru
python manage.py compilemessages
```

---

# 📊 Baholash Mezoni

| Criteria           | Ball |
| ------------------ | ---- |
| Models to‘g‘ri     | 20   |
| URL & Views to‘liq | 25   |
| CRUD ishlashi      | 25   |
| Template logikasi  | 15   |
| Validatsiya        | 15   |
| Jami               | 100  |

---

# 👨‍💻 Muallif

Azizbek
Backend Developer
