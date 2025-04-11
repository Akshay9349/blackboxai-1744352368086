document.getElementById('searchForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const regNumber = document.getElementById('regNumber').value.trim();
    const errorMessage = document.getElementById('errorMessage');
    const spinner = document.querySelector('.spinner');

    // Clear previous error message
    errorMessage.classList.add('hidden');

    // Validate registration number format (example regex for Indian registration numbers)
    const regEx = /^[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{4}$/;
    if (!regEx.test(regNumber)) {
        errorMessage.textContent = "Invalid registration number format. Example: KA01AB1234";
        errorMessage.classList.remove('hidden');
        return;
    }

    // Show loading spinner
    spinner.classList.add('active');

    // Simulate API call
    setTimeout(() => {
        // Simulated RC details (replace with actual API call in production)
        const rcDetails = {
            regNumber: regNumber,
            ownerName: "John Doe",
            vehicleModel: "Toyota Corolla",
            regDate: "2020-01-15",
            vehicleClass: "Sedan",
            fuelType: "Petrol",
            engineNumber: "EN123456789",
            chassisNumber: "CH123456789"
        };

        // Hide loading spinner
        spinner.classList.remove('active');

        // Redirect to result page with RC details
        localStorage.setItem('rcDetails', JSON.stringify(rcDetails));
        window.location.href = 'result.html';
    }, 2000); // Simulate 2 seconds delay for API call
});

// On result.html, populate the RC details
if (window.location.pathname.endsWith('result.html')) {
    const rcDetails = JSON.parse(localStorage.getItem('rcDetails'));
    if (rcDetails) {
        document.getElementById('regNumber').textContent = rcDetails.regNumber;
        document.getElementById('ownerName').textContent = rcDetails.ownerName;
        document.getElementById('vehicleModel').textContent = rcDetails.vehicleModel;
        document.getElementById('regDate').textContent = rcDetails.regDate;
        document.getElementById('vehicleClass').textContent = rcDetails.vehicleClass;
        document.getElementById('fuelType').textContent = rcDetails.fuelType;
        document.getElementById('engineNumber').textContent = rcDetails.engineNumber;
        document.getElementById('chassisNumber').textContent = rcDetails.chassisNumber;
    } else {
        document.getElementById('errorCard').classList.remove('hidden');
        document.getElementById('errorText').textContent = "No RC details found. Please try again.";
    }
}
