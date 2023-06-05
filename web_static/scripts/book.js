const bookingForm = document.getElementById('booking-form');
  const confirmationMessage = document.getElementById('confirmation');

  bookingForm.addEventListener('submit', (event) => {
    event.preventDefault();
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const date = document.getElementById('date').value;
    const service = document.getElementById('service').value;

    // Simulating form submission (you can replace this with your own logic)
    setTimeout(() => {
      confirmationMessage.innerText = `Appointment booked successfully for ${name} on ${date} for ${service}.`;
      confirmationMessage.style.display = 'block';
      bookingForm.reset();
    }, 2000);
  });