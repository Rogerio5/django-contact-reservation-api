// ===============================
// Script principal do PetCare
// ===============================

document.addEventListener("DOMContentLoaded", function () {
  console.log("🐾 Bem-vindo ao sistema PetCare!");

  // -------------------------------
  // 1. Toast de boas-vindas
  // -------------------------------
  const toast = document.createElement("div");
  toast.innerText = "🐾 Bem-vindo ao PetCare!";
  toast.style.position = "fixed";
  toast.style.bottom = "20px";
  toast.style.right = "20px";
  toast.style.background = "#0d6efd";
  toast.style.color = "#fff";
  toast.style.padding = "10px 20px";
  toast.style.borderRadius = "8px";
  toast.style.boxShadow = "2px 2px 6px rgba(0,0,0,0.3)";
  toast.style.zIndex = "9999";
  toast.style.opacity = "0";
  toast.style.transition = "opacity 0.5s ease-in-out";

  document.body.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = "1";
  }, 500);

  setTimeout(() => {
    toast.style.opacity = "0";
    setTimeout(() => toast.remove(), 500);
  }, 4000);

  // -------------------------------
  // 2. Interação com cards
  // -------------------------------
  const cards = document.querySelectorAll(".card");
  cards.forEach((card) => {
    card.addEventListener("click", () => {
      card.classList.add("highlight");
      setTimeout(() => card.classList.remove("highlight"), 1000);
    });
  });

  // -------------------------------
  // 3. Máscara de telefone
  // -------------------------------
  const telefoneInput = document.querySelector("#id_telefone");
  if (telefoneInput) {
    telefoneInput.addEventListener("input", function (e) {
      let value = e.target.value.replace(/\D/g, ""); // remove tudo que não é número

      if (value.length > 11) value = value.slice(0, 11);

      if (value.length <= 10) {
        // Formato (xx) xxxx-xxxx
        value = value.replace(/^(\d{2})(\d{4})(\d{0,4})$/, "($1) $2-$3");
      } else {
        // Formato (xx) xxxxx-xxxx
        value = value.replace(/^(\d{2})(\d{5})(\d{0,4})$/, "($1) $2-$3");
      }

      e.target.value = value;
    });
  }
});
