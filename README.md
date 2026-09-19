# Learning Log — Comprehensive Project Summary

## Project Overview

**Learning Log** is a Django-based web application deployed on **[PythonAnywhere](https://carbonchemistry.pythonanywhere.com)**. It began as a textbook exercise from *Python Crash Course* and has grown into a small-scale social platform. Users can create learning topics, record entries, track progress, connect with friends, and receive system notifications. The site is hosted at `carbonchemistry.pythonanywhere.com` and maintained via Git on [GitHub](https://github.com/carbon0425/Web_learning_log---python_anywhere).

---

## Technical Stack

| Layer              | Technology                                                 |
|--------------------|------------------------------------------------------------|
| Backend framework  | Django 5.2.11                                              |
| Language           | Python 3.11                                                |
| Database           | SQLite                                                     |
| Frontend           | Bootstrap 4, Font Awesome, custom CSS                      |
| Markdown rendering | `mistune` + `bleach` (XSS filtering)                       |
| Deployment         | PythonAnywhere (WSGI + virtualenv + environment variables) |
| Version control    | Git + GitHub                                               |
| Package publishing | PyPI (`django-action-type`)                                |

---

## Architecture & App Structure

The project is split into two Django applications.

### `learning_logs_app`
Core content application, containing:
- `Topic` and `Entry` models with ownership
- `ErrorLog` model for 500 errors
- CRUD views for topics and entries
- Broadcast view protected by `@staff_member_required`
- Custom 404 and 500 handlers
- Markdown rendering with XSS filtering
- Hacker trap pages (`hacker.html`, `hacker_fake_normal.html`)
- Templates: `index`, `topics`, `topic`, `new_topic`, `new_entry`, `edit_entry`, `base`, `broadcast`, `markdown_help`, `hacker`, `hacker_fake_normal`

### `user_app`
User-centric application, containing:
- Custom `User` model extending `AbstractUser` with `friends` many-to-many field
- `Feedback` model
- `Notification` model with `action_type` and `action_data` (JSONField)
- `actions.py` defining `namedtuple`s and `ACTION_MAP`
- Forms: `FeedbackForm`, `NotificationForm`, `MyUserCreationForm`, `FriendApplyForm`
- Views: `register`, `notifications`, `feedback`, `search_users`, `add_user`, `apply_message`
- Templates: `notifications`, `feedback`, `feedback_ok`, `login`, `register`, `logout`, `search_users`, `send_apply`, `apply_message`

---

## Version History (Summary)

- **v1.0.0** — Core framework, authentication, deployment to PythonAnywhere.
- **v1.0.1** — Feedback module.
- **v1.0.2** — Notifications and error logging.
- **v1.0.3** — Full-server broadcast with hidden periodic-table URL.
- **v1.0.4** — Production stability, Git conflict resolution, `.gitignore` cleanup.
- **v1.1.0** — Users app separation, URL namespacing.
- **v1.1.1** — Frontend component restructure (plus button, dropdown menus, three-dot entry menu, user dropdown).
- **v1.1.2** — User center left sidebar layout.
- **v1.1.3** — Friend permission interception and comment logic differentiation.
- **v1.1.4** — Financial-style dashboard with triple-mode slider.

---

## Key Features

1. **User Authentication** — Custom user model, registration, login, logout, `@login_required`.

2. **Topics & Entries** — Full CRUD. Entries support Markdown with live preview (Code/Preview tabs), rendered by `mistune` and sanitized by `bleach`.

3. **Notification System** — Extensible via `action_type` + `action_data` and `namedtuple`s in `actions.py`. Supports `normal`, `friend_apply`, and `apply_check` types.

4. **Friend System (In Progress)** — Search users, send friend request with custom message, receive notification. `friend_apply` notifications show accept/reject buttons. `apply_check` notifications show status (`PENDING`, `ACCEPTED`, `REJECTED`). Permission checks allow friends to view each other's topics.

5. **Full-Server Broadcast** — Staff-only hidden URL (`/hlinakrbcsfrbemgcasrbara/`) sends a notification to every user.

6. **Error Logging** — `ErrorLog` records 500 errors with full traceback. Admin can view and resolve.

7. **Custom 404/500 Pages** — Friendly error pages with links to home and feedback.

8. **Hacker Trap (Easter Egg)** — Suspicious input triggers a fake terminal with random logs, endless progress bar, and sarcastic messages. A second layer (`hacker_fake_normal.html`) simulates a normal entry page but injects glitches, fake logs, and visual noise.

9. **Markdown Help Panel** — Collapsible question-mark button shows Markdown syntax cheat sheet.

---

## Deployment Notes

Deployed on PythonAnywhere free tier:
- `venv/` with dependencies
- `SECRET_KEY` in environment variables
- `DEBUG=False`, `ALLOWED_HOSTS` set
- `collectstatic` run
- WSGI points to `learning_logs_settings.settings`
- Deployment via `git pull`, `migrate`, `collectstatic`, Reload

---

## Design Philosophy

- **Flat over nested** — `action_type` + `action_data` instead of many models
- **Interface over implementation** — `@property` returns `namedtuple`
- **Data-driven** — `ACTION_MAP` registers behavior
- **Extensible** — adding a line, not rewriting views
- **Readable and maintainable**

Published as `django-action-type` on PyPI.

---

## Current Status & Next Steps

**Current:** Core features + Feedback + Notifications + Admin Broadcast + Friend viewing permissions + Dashboard with triple-mode slider.

**Next:** Friend request acceptance/rejection workflow, friend list management, privacy tiers, shared-study groups.

---

## Final Note

This project survived hard drive formats, network interruptions, Git conflicts, and database recoveries. It is a personal record of what one developer can build when they refuse to stop at "it works."