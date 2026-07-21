# Learning Log Project v1.1.x Release Notes (Detailed)

## v1.1.0 – Users App Infrastructure & File Migration
**Goal:** Refactor the project to separate user-centric features into a dedicated `users` application for better modularity and code maintainability.

- **App Separation:** Migrated `Notification` and `Feedback` models, forms, views, and URL routing from the core `learning_logs_app` into the newly created `users` application.
- **Model Movement:** Cut and pasted the database model classes into the new app and handled the database reset (dropping the local `db.sqlite3` and running fresh `makemigrations` and `migrate`) to ensure the new app structure takes effect.
- **URL Namespacing:** Set up `app_name = 'users'` in `users/urls.py` and configured the root `urls.py` to include it, allowing navigation like `/users/dashboard/` and `/users/notifications/`.

---

## v1.1.1 – Frontend Interaction Components Restructure
**Goal:** Implement four essential interactive UI components directly into the existing templates to establish a more modern and user-friendly feel.

- **Plus Button on Topic Page:** Placed an "Add New Entry" button (`btn btn-primary btn-sm`) on the right side of the Topic title using the Bootstrap flexbox classes `d-flex justify-content-between align-items-center`. This creates a perfect left-right alignment.
- **Minus Delete Button on Topics List:** Replaced the simple text link with a safe `<form method="post">` containing a `{% csrf_token %}`. The button is styled as a purely red text link (`btn btn-link text-danger p-0`) to prevent search engine crawlers from accidentally deleting topics.
- **Three-Dot Dropdown Menu on Entry Cards:** Removed the raw `Edit Entry` and `Delete Entry` text links from the card header. Replaced them with a Bootstrap `dropdown` trigger button (three dots `⋮`) and a `dropdown-menu`. Added `dropdown-menu-right` to ensure the menu pops out leftwards and doesn't get cut off by the screen edge.
- **Top Navbar User Dropdown Menu:** Consolidated the crowded top navigation bar links (`Topics`, `Feedback`, `Notifications`) into a single dropdown menu triggered by the logged-in user's username (`Hello, username`) using `dropdown`, `dropdown-toggle`, and `dropdown-menu`.

---

## v1.1.2 – User Center Left Sidebar Layout
**Goal:** Build the structural foundation for a fully functional User Dashboard by implementing a `users_base.html` with a persistent left navigation sidebar.

- **Layout Architecture:** Created `users_base.html` which directly extends `base.html` (retaining the top navigation bar). Used `d-flex flex-shrink-0` (for the fixed 260px wide left menu) and `flex-grow-1` (for the auto-expanding right content area) to create a clean "Left Sidebar + Right Content" split screen layout.
- **Vertical Navigation Menu:** Used `nav-pills flex-column` to build the left-side capsule-style menu containing `Topics`, `Feedback`, `Notifications`, and `Log out`.
- **Dynamic Active Highlighting:** Integrated Django's `{% if request.path == '/users/topics/' %}active-menu{% endif %}` statement into the `<a>` tags. In combination with a custom `active-menu` CSS class (`background-color: #e9ecef;`), this enables the selected menu item to turn visually gray/highlighted without writing any frontend JavaScript.

---

## v1.1.3 – Friend Permission Interception & Comment Logic Differentiation
**Goal:** Break the "self-only" content silo to allow users to view their friends' topics, while dynamically rendering different UI components for self-owned entries versus friends' entries.

- **View Permission Expansion:** Updated the `topic` view in `views.py`. Instead of `if topic.owner != request.user: raise Http404`, we now use: `if topic.owner != request.user and topic.owner not in request.user.friends.all(): raise Http404`. This allows the topic owner's friends to access the details page while still keeping it private from strangers.
- **UI Branching for Entries:** Introduced a logic check `{% if entry.owner == request.user %}` in `topic.html`'s entry loop.
    - `If True (Self)`: The entry displays the three-dot dropdown menu containing `Edit` and `Delete` options.
    - `If False (Friend)`: The entry instead displays a `Comment` button and a list of existing comments, visually distinguishing the ownership and interaction style.

---

## v1.1.4 – Financial-style Dashboard with Triple-Mode Slider
**Goal:** Develop a professional-grade Dashboard entry point with a smooth animated slider to segregate statistics, friend activity, and quick actions.

- **Triple-Mode Tabs Slider:** Built the top component using Bootstrap `nav-tabs` linked to three distinct `<div>` content areas (`id="mode1"`, `id="mode2"`, `id="mode3"`). Added a custom blue `slider-indicator` bar with `transition: all 0.3s ease;` and a small jQuery script that listens to the `shown.bs.tab` event, calculating the clicked tab's position and width to animate the slider bar smoothly underneath it.
- **Mode 1 – Statistics Panel:** Aggregated backend data from `views.py` to display three core metrics in a card format: Total Topics, Total Journal Entries, and Total Friends Count.
- **Mode 2 – Friend Activity Feed:** Fetched recent comments from friends using the `request.user.friends.all()` query set in `views.py`. Displayed them in a reverse chronological list showing the friend's username, the comment preview, and the timestamp (`order_by('-created_at')[:5]`).
- **Mode 3 – Quick Action Buttons:** Provided three prominent shortcut buttons in a separate block for fast access: `Create New Topic`, `View Friend List`, and `View All Notifications`.