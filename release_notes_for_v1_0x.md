# Learning Log Project Version Iteration Log (v1.0.0 ~ v1.0.4)

## 🟢 v1.0.0 — Core Framework & Cloud Revival
**Functionality Completed**
- Built the foundational Django framework (`Topic` and `Entry` models, relational queries).
- Integrated the user authentication system (Registration, Login, Permission verification via `@login_required`).
- Completed local debugging (`runserver`) and self-testing of core features.

**Deployment Milestones**
- **Successfully deployed to PythonAnywhere cloud**, configured `ALLOWED_HOSTS`, and executed static file collection (`collectstatic`).
- Rebuilt the native development environment on a clean hard drive after surviving a complete system BitLocker lockout.

---

## 🔵 v1.0.1 — User Feedback Module
**New Features**
- Added the `Feedback` model and its corresponding `FeedbackForm`.
- Developed the user feedback submission page (`/feedback/`), achieving full interaction between the frontend and the database.

---

## 🟡 v1.0.2 — System Notifications & Error Logging Module
**New Features**
- Established the `Notification` model, supporting personalized system messages for specific users.
- Implemented the homepage `index` view to display **unread notification counts** (`is_read=False`).
- Integrated an `ErrorLog` model within the Django Admin panel to capture and record 500 internal server errors, facilitating real-time post-deployment debugging.

**UI Enhancements**
- Refined the `notifications.html` template, adding card-based layouts and timestamp filters.

---

## 🔴 v1.0.3 — Full-Server Broadcast & Admin Panel (Secret Broadcast)
**New Features**
- Developed the **"Full-Server Broadcast Terminal"** (`broadcast` view).
- Utilized **`User.objects.all()` and `bulk_create` methods** to efficiently send system-wide announcements to every registered user with a single click.
- **Security & Easter Egg**: Designed a completely hidden access route (utilizing a URL based on the first and second groups of the Periodic Table). Implemented strict access control using `@staff_member_required` to ensure only administrators can access this panel.

**UI Adjustments**
- Added a warning alert box to the broadcast page with a heavy, authoritative tone, emphasizing the "irreversible" nature of the action and the "administrator's responsibility".

---

## 🟣 v1.0.4 — Production Environment Stability & Maintenance Fixes
**DevOps & Maintenance**
- **Resolved Git Merge Conflicts**: Fixed branch divergence errors on the PythonAnywhere terminal (`Need to specify how to reconcile divergent branches`).
- **Cleaned up untracked files**: Configured `.gitignore` to exclude `venv/`, `*.json`, and `staticfiles/`, preventing irrelevant test data from polluting the GitHub repository.

**Security Hardening**
- Fixed the `ValueError` in `NotificationForm` (caused by unbound `Model`), refactoring it from a `ModelForm` to a standard `Form` to ensure the broadcast form functions correctly.
- Polished the Admin warning text to reinforce the sense of responsibility and trust.

---

## 📌 Current Development Status & Next Steps (v1.1.0 Preview)
- **Current Completion Status**: Core features + Feedback system + Notifications + Admin Full-server Broadcast. The project now has the robust foundation of a small-scale social Web App.
- **Next Development Phase (v1.1.0)**: **Social Friend System**.
  - Sending friend requests, Accepting/Rejecting requests, Friend list management, and integrating them with the existing Notification system.

---

> **Final Note:** This version log was forged through a grueling "three-day system war" involving a hard drive format, graphics driver chaos, and endless network connection hiccups. You've built a rock-solid foundation with `v1.0.4`. Time to enjoy the rest of the day! 😎