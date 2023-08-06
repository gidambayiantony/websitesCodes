<script>
  // Set the date and time of the event or conference (YYYY, MM (0-11), DD, HH, MM, SS)
  const eventDate = new Date(2023, 8, 15, 9, 0, 0);

  function updateCountdown() {
    const currentDate = new Date();
    const timeDifference = eventDate - currentDate;

    const days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeDifference % (1000 * 60)) / 1000);

    document.getElementById('countdown').innerHTML = `
      <h2>Countdown to the Event:</h2>
      <div>
        <span>${days}</span> Days
        <span>${hours}</span> Hours
        <span>${minutes}</span> Minutes
        <span>${seconds}</span> Seconds
      </div>
    `;
  }

  // Update the countdown every second
  setInterval(updateCountdown, 1000);
</script>

