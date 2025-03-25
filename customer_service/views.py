from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Customer, ServiceRequest, TimelineEvent,ServiceRequestType
from .forms import ServiceRequestForm
# Adjust the import path to match the correct module structure
from .models import ServiceRequestType
from .forms import ServiceRequestForm


@login_required
def dashboard(request):
    try:
        customer = request.user.customer  # Assuming you have a one-to-one relationship
        service_requests = ServiceRequest.objects.filter(customer=customer).order_by('-created_at')
    except Customer.DoesNotExist:
        # Handle the case where the user doesn't have a customer profile
        customer = None
        service_requests = []
    
    context = {
        'customer': customer,
        'service_requests': service_requests
    }
    return render(request, 'customer_service/dashboard.html', context)

@login_required
def create_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user.customer
            service_request.type = request.POST.get('type')  # Capture the type from the form
            service_request.save()
            
            # Handle attachments if needed
            if 'attachment' in request.FILES:
                for file in request.FILES.getlist('attachment'):
                    # Save file logic here
                    pass
            
            return redirect('service_request_detail', pk=service_request.pk)
    else:
        form = ServiceRequestForm()
        service_request_types = ServiceRequestType.objects.all()  # Fetch available types
    
    return render(request, 'customer_service/create_service_request.html', {
        'form': form,
        'service_request_types': service_request_types  # Pass types to the template
    })

@login_required
def service_request_detail(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    
    # Security check - ensure user can only see their own requests
    if request.user.is_staff or service_request.customer.user == request.user:
        timeline_events = TimelineEvent.objects.filter(service_request=service_request).order_by('timestamp')
        return render(request, 'customer_service/service_request_detail.html', {
            'service_request': service_request,
            'timeline_events': timeline_events,
        })
    else:
        return redirect('dashboard')

@login_required
def my_service_requests(request):
    try:
        customer = request.user.customer
        service_requests = ServiceRequest.objects.filter(customer=customer).order_by('-created_at')
    except Customer.DoesNotExist:
        customer = None
        service_requests = []
    
    return render(request, 'customer_service/my_service_requests.html', {
        'service_requests': service_requests
    })

@login_required
def update_service_request_status(request, pk):
    if not request.user.is_staff:
        return redirect('dashboard')
    
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        service_request.status = new_status
        service_request.save()
    
    return redirect('service_request_detail', pk=pk)

@login_required
def cancel_service_request(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    
    # Security check - ensure user can only cancel their own requests
    if service_request.customer.user == request.user:
        if request.method == 'POST':
            service_request.status = 'cancelled'
            service_request.save()
    
    return redirect('service_request_detail', pk=pk)