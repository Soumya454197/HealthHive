document.getElementById('doctorBtn').addEventListener('click', function() {
    document.getElementById('buttonContainer').style.display = 'none';
    document.getElementById('doctorForm').style.display = 'flex';
});

document.getElementById('patientBtn').addEventListener('click', function() {
    document.getElementById('buttonContainer').style.display = 'none';
    document.getElementById('patientForm').style.display = 'flex';
});
