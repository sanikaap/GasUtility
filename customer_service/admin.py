from django.contrib import admin
from .models import Customer, ServiceRequestType, ServiceRequest, Attachment, Comment

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'user', 'phone_number')
    search_fields = ('customer_id', 'user__username', 'user__first_name', 'user__last_name')

@admin.register(ServiceRequestType)
class ServiceRequestTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'estimated_completion_time')

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'customer', 'request_type', 'status', 'created_at', 'assigned_to')
    list_filter = ('status', 'request_type')
    search_fields = ('title', 'description', 'customer__user__username')
    date_hierarchy = 'created_at'

@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('service_request', 'uploaded_at')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('service_request', 'user', 'created_at')