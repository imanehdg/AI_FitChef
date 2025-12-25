// static/js/planning.js - Script pour générer le planning dynamiquement

document.addEventListener('DOMContentLoaded', function() {
    const generateBtn = document.getElementById('generate-planning');
    const loadingDiv = document.getElementById('loading');
    const planningGrid = document.getElementById('planning-grid');
    
    generateBtn.addEventListener('click', async function() {
        console.log('🔥 Bouton cliqué !');
        
        // Afficher le loading
        loadingDiv.classList.add('active');
        generateBtn.disabled = true;
        generateBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Génération en cours...';
        
        try {
            // Appel à l'API Flask
            const response = await fetch('/api/generate_planning', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            
            if (!response.ok) {
                throw new Error('Erreur lors de la génération du planning');
            }
            
            const data = await response.json();
            console.log('📦 Données reçues:', data);
            
            if (data.success) {
                // Remplir le planning avec les données de l'IA
                afficherPlanning(data.planning);
            } else {
                alert('Erreur : ' + data.error);
            }
            
        } catch (error) {
            console.error('Erreur:', error);
            alert('Impossible de générer le planning. Vérifie ta connexion.');
        } finally {
            // Cacher le loading
            loadingDiv.classList.remove('active');
            generateBtn.disabled = false;
            generateBtn.innerHTML = '<i class="fas fa-magic"></i> Régénérer mon planning';
        }
    });
});

function afficherPlanning(planning) {
    console.log('🎨 Affichage du planning...');
    const jours = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche'];
    
    jours.forEach(jour => {
        const jourData = planning[jour];
        
        // Petit-déjeuner
        document.getElementById(`${jour}-breakfast-title`).textContent = jourData.petit_dejeuner.nom;
        document.getElementById(`${jour}-breakfast-desc`).textContent = jourData.petit_dejeuner.description;
        document.getElementById(`${jour}-breakfast-cal`).textContent = `${jourData.petit_dejeuner.calories} kcal`;
        
        // Snack matin
        document.getElementById(`${jour}-snack1-title`).textContent = jourData.snack_matin.nom;
        document.getElementById(`${jour}-snack1-desc`).textContent = jourData.snack_matin.description;
        document.getElementById(`${jour}-snack1-cal`).textContent = `${jourData.snack_matin.calories} kcal`;
        
        // Déjeuner
        document.getElementById(`${jour}-lunch-title`).textContent = jourData.dejeuner.nom;
        document.getElementById(`${jour}-lunch-desc`).textContent = jourData.dejeuner.description;
        document.getElementById(`${jour}-lunch-cal`).textContent = `${jourData.dejeuner.calories} kcal`;
        
        // Snack après-midi
        document.getElementById(`${jour}-snack2-title`).textContent = jourData.snack_apres_midi.nom;
        document.getElementById(`${jour}-snack2-desc`).textContent = jourData.snack_apres_midi.description;
        document.getElementById(`${jour}-snack2-cal`).textContent = `${jourData.snack_apres_midi.calories} kcal`;
        
        // Dîner
        document.getElementById(`${jour}-dinner-title`).textContent = jourData.diner.nom;
        document.getElementById(`${jour}-dinner-desc`).textContent = jourData.diner.description;
        document.getElementById(`${jour}-dinner-cal`).textContent = `${jourData.diner.calories} kcal`;
        
        // Total calories du jour
        const totalCal = jourData.petit_dejeuner.calories + 
                        jourData.snack_matin.calories + 
                        jourData.dejeuner.calories + 
                        jourData.snack_apres_midi.calories + 
                        jourData.diner.calories;
        
        document.getElementById(`${jour}-total`).textContent = `Total : ${totalCal} kcal`;
    });
    
    // Scroll vers le planning
    document.getElementById('planning-grid').scrollIntoView({ 
        behavior: 'smooth',
        block: 'start'
    });
}

// Fonction pour afficher les détails d'un repas (optionnel)
function afficherDetailsRepas(jour, repas, data) {
    const modal = document.createElement('div');
    modal.className = 'modal';
    modal.innerHTML = `
        <div class="modal-content">
            <span class="close">&times;</span>
            <h2>${data.nom}</h2>
            <p><strong>Ingrédients :</strong> ${data.description}</p>
            <p><strong>Calories :</strong> ${data.calories} kcal</p>
        </div>
    `;
    document.body.appendChild(modal);
    
    modal.querySelector('.close').addEventListener('click', () => {
        modal.remove();
    });
}