from django.shortcuts import render, redirect
from .models import Topic, Entry, ErrorLog
from .forms import TopicForm, EntryForm, FeedbackForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404
import sys
import traceback
from django.contrib import messages

def index(request):
    """The home page for Learning Logs."""
    return render(request, 'learning_logs_app/index.html')

# noinspection PyUnusedLocal
@login_required
def topics(request):
    """The page that show all topics."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics, 'user': request.user}
    return render(request, 'learning_logs_app/topics.html', context)

@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = get_object_or_404(Topic, id=topic_id)
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    quantity = entries.count()
    create_time = topic.date_added
    context = {'topic': topic, 'entries': entries,
               'quantity': quantity, 'create_time': create_time}
    return render(request, 'learning_logs_app/topic.html', context)

@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs_app:topics')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'learning_logs_app/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = get_object_or_404(Topic, id=topic_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            _new_entry = form.save(commit=False)
            _new_entry.topic = topic
            _new_entry.save()
            return redirect('learning_logs_app:topic', topic_id=topic_id)

    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs_app/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = get_object_or_404(Entry, id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs_app:topic', topic_id=topic.id)

    # Display a blank or invalid form.
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs_app/edit_entry.html', context)


# noinspection PyUnusedLocal
@login_required
def delete_entry(request, entry_id):
    """Delete an existing entry."""
    entry = get_object_or_404(Entry, id=entry_id)
    if entry.topic.owner != request.user:
        raise Http404
    topic_id = entry.topic.id
    entry.delete()

    return redirect('learning_logs_app:topic', topic_id=topic_id)


# noinspection PyUnusedLocal
@login_required
def delete_topic(request, topic_id):
    """Delete an existing topic and all its entries."""
    if topic.owner != request.user:
        raise Http404
    topic = get_object_or_404(Topic, id=topic_id)
    topic.delete()

    return redirect('learning_logs_app:topics')

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback_obj = form.save(commit=False)
            if request.user.is_authenticated:
                feedback_obj.username = request.user.username
            feedback_obj.save()
            messages.success(request, 'Thank you for your feedback!')
            return redirect('learning_logs_app:feedback_ok')
        else:
            messages.error(request, 'There was an error with your submission. Please check the form and try again.')
    else:
        if request.user.is_authenticated:
            initial = {'username': request.user.username}
            form = FeedbackForm(initial=initial)
            form.fields['username'].disabled = True
        else:
            form = FeedbackForm()
            form.fields['username'].required = True

    context = {'form': form}
    return render(request, 'learning_logs_app/feedback.html', context)

def feedback_ok(request):
    return render(request, 'learning_logs_app/feedback_ok.html')

# noinspection PyUnusedLocal
def custom_404(request, exception):
    """Custom 404 error page."""
    return render(request, '404.html', status=404)

def custom_500(request):
    """Custom 500 error page."""

    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback_str = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))

    ErrorLog.objects.create(
        path=request.path,
        method=request.method,
        status=500,
        exception_type=str(exc_type.__name__),
        exception_message=str(exc_value),
        traceback=traceback_str,
        is_resolved=False
    )
    return render(request, '500.html', status=500)