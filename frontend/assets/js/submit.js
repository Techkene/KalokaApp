document.addEventListener("DOMContentLoaded", function() {
    const submitButton = document.querySelector(".btn.btn-b");
  
    submitButton.addEventListener("click", async function(event) {
      event.preventDefault();

      const stockQty = document.getElementById("stock-qty").value;
      const feedType = document.getElementById("feed-type").value;
      const morningMortality = document.getElementById("mmortality").value;
      const eveningMortality = document.getElementById("emortality").value;
      const feedQty = document.getElementById("feed_qty").value;
      const unusualObservation = document.getElementById("observation").value;
      const medicationUsed = document.getElementById("medication").value;

      const farmData = {
        stock_qty: stockQty,
        feed_type: feedType,
        morning_mortality: morningMortality,
        evening_mortality: eveningMortality,
        feed_qty: feedQty,
        unusual_observation: unusualObservation,
        medication_used: medicationUsed
      };

      const postData = await fetch("https://kalokaapp-production.up.railway.app/submit", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(farmData)
      });
      if (postData.ok) {
        window.location.href = "/frontend/output.html";
      }
    });
  });
  
