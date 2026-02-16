// Revue de Mémoires - JavaScript

document.addEventListener('DOMContentLoaded', function () {
    // --- Review form: spinner on submit ---
    const reviewForm = document.getElementById('reviewForm');
    if (reviewForm) {
        reviewForm.addEventListener('submit', function () {
            const spinner = document.getElementById('spinner');
            const submitBtn = document.getElementById('submitBtn');
            if (spinner) spinner.classList.remove('d-none');
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Analyse en cours...';
            }
        });
    }

    // --- Auto-dismiss flash alerts after 5s ---
    document.querySelectorAll('.alert-dismissible').forEach(function (alert) {
        setTimeout(function () {
            var bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
            bsAlert.close();
        }, 5000);
    });
});
