document.addEventListener('DOMContentLoaded', function() {
    // Example: Add any client-side functionality for the staff dashboard
    const requestRows = document.querySelectorAll('.service-requests-section tbody tr');
    
    requestRows.forEach(row => {
        row.addEventListener('mouseover', function() {
            this.style.backgroundColor = '#f1f1f1';
        });
        
        row.addEventListener('mouseout', function() {
            this.style.backgroundColor = '';
        });
    });
});