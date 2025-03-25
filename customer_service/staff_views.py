from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.urls import reverse
from .models import ServiceRequest, Comment
from .forms import CommentForm

def is_staff(user):
    """Check if user is staff"""
    return user.is_staff

@login_required
@user_passes_test(is_staff)
def staff_dashboard(request):
    """Staff dashboard showing all service requests"""
    pending_requests = ServiceRequest.objects.filter(status='pending').order_by('-created_at')
    in_progress_requests = ServiceRequest.objects.filter(status='in_progress').order_by('-created_at')
    resolved_requests = ServiceRequest.objects.filter(status='resolved').order_by('-created_at')
    
    return render(request, 'customer_service/staff/dashboard.html', {
        'pending_requests': pending_requests,
        'in_progress_requests': in_progress_requests,
        'resolved_requests': resolved_requests,
    })

@login_required
@user_passes_test(is_staff)
def staff_service_request_detail(request, pk):
    """Staff view for handling a service request"""
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    attachments = service_request.attachments.all()
    comments = service_request.comments.all().order_by('created_at')
    
    if request.method == 'POST':
        if 'update_status' in request.POST:
            new_status = request.POST.get('status')
            if new_status in [s[0] for s in ServiceRequest.STATUS_CHOICES]:
                service_request.status = new_status
                if new_status == 'in_progress' and not service_request.assigned_to:
                    service_request.assigned_to = request.user
                elif new_status == 'resolved' and not service_request.resolved_at:
                    service_request.resolve()
                else:
                    service_request.save()
                messages.success(request, f"Request status updated to {new_status}")
        elif 'add_comment' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.service_request = service_request
                new_comment.user = request.user
                new_comment.save()
                messages.success(request, "Comment added successfully")
        
        return redirect('staff_service_request_detail', pk=service_request.pk)
    
    comment_form = CommentForm()
    
    return render(request, 'customer_service/staff/service_request_detail.html', {
        'service_request': service_request,
        'attachments': attachments,
        'comments': comments,
        'comment_form': comment_form,
    })