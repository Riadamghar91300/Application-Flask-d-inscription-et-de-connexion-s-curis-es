// Fonction pour réinitialiser le formulaire de connexion
function resetForm() {
  document.getElementById("loginForm").reset();
}



// Fonction pour réinitialiser le formulaire d'inscription
function resetInscriptionForm() {
  document.getElementById("inscriptionForm").reset();
}



// Fonction pour rediriger vers la page d'inscription
function redirectToInscription() {
  window.location.href = "/inscription"; // Utilisation de l'URL complète pour la redirection
}



// Fonction pour rediriger vers la page de connexion
function redirectToLogin() {
  window.location.href = "/connexion"; // Utilisation de l'URL complète pour la redirection
}



// Fonction pour vérifier si le mot de passe répond aux critères requis
function checkPassword(password) {
  // Expression régulière pour vérifier la présence d'au moins un chiffre
  const hasNumber = /\d/.test(password);
  // Expression régulière pour vérifier la présence d'au moins une majuscule
  const hasUppercase = /[A-Z]/.test(password);
  // Expression régulière pour vérifier la présence d'au moins un caractère spécial
  const hasSpecialChar = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]+/.test(password);
  // Vérification de la longueur du mot de passe
  const isLongEnough = password.length >= 8;

  // Vérification si toutes les conditions sont remplies
  if (hasNumber && hasUppercase && hasSpecialChar && isLongEnough) {
      return true;
  } else {
      return false;
  }
}

// Fonction de soumission du formulaire d'inscription
function submitInscriptionForm() {
  const password = document.getElementById("motDePasse").value;
  // Vérifier si le mot de passe répond aux critères requis
  if (!checkPassword(password)) {
      alert("Le mot de passe doit contenir au moins un chiffre, une majuscule, un caractère spécial et avoir une longueur d'au moins 8 caractères.");
      return false; // Empêcher la soumission du formulaire si le mot de passe ne répond pas aux critères
  }
  // Si le mot de passe est valide, le formulaire sera soumis normalement
  return true;
}
