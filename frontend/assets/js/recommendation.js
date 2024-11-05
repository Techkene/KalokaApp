async function fetchRecommendation() {
    try {
      const response = await fetch("https://kalokaapp-production.up.railway.app/recommendation", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      });

      if (!response.ok) {
        throw new Error("Failed to fetch the latest recommendation");
      }
      const recommendation = await response.json();
      const obs = document.getElementById("observation");
      if (obs) {
        obs.value = recommendation.recommendation_text
      }
    } catch (error) {
      console.error("Error fetching recommendation:", error);
    }
}

document.addEventListener("DOMContentLoaded", fetchRecommendation);
  
