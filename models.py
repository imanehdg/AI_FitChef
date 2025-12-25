from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

db = SQLAlchemy()

# ========================================
# 📊 TABLE UTILISATEURS
# ========================================
class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relations
    profile = db.relationship('UserProfile', backref='user', uselist=False, cascade='all, delete-orphan')
    motivation = db.relationship('UserMotivation', backref='user', uselist=False, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<User {self.username}>'


# ========================================
# 👤 TABLE PROFIL UTILISATEUR
# ========================================
class UserProfile(db.Model):
    __tablename__ = 'user_profiles'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    # Informations personnelles
    age = db.Column(db.Integer)
    weight = db.Column(db.Float)  # en kg
    height = db.Column(db.Float)  # en cm
    gender = db.Column(db.String(20))
    
    # Objectifs
    goal = db.Column(db.String(100))  # perte de poids, prise de masse, maintien...
    activity_level = db.Column(db.String(50))  # sédentaire, actif, très actif...
    target_calories = db.Column(db.Integer)
    
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<UserProfile user_id={self.user_id}>'


# ========================================
# 🔥 TABLE MOTIVATION (NOUVEAU!)
# ========================================
class UserMotivation(db.Model):
    __tablename__ = 'user_motivation'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    # Jours consécutifs
    streak_count = db.Column(db.Integer, default=0)  # Nombre de jours consécutifs
    last_activity_date = db.Column(db.Date, default=datetime.utcnow().date)  # Dernière activité
    
    # Challenge du jour
    current_challenge = db.Column(db.Text)  # Challenge actuel
    challenge_progress = db.Column(db.Integer, default=0)  # Progression 0-100
    challenge_completed = db.Column(db.Boolean, default=False)  # Complété aujourd'hui?
    challenge_date = db.Column(db.Date, default=datetime.utcnow().date)  # Date du challenge
    
    # Statistiques globales
    total_challenges_completed = db.Column(db.Integer, default=0)
    best_streak = db.Column(db.Integer, default=0)  # Meilleur série de jours
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<UserMotivation user_id={self.user_id} streak={self.streak_count}>'
    
    # 🎯 MÉTHODES UTILES
    
    def update_streak(self):
        """
        Met à jour le streak (jours consécutifs)
        - Si activité aujourd'hui : maintient le streak
        - Si activité hier : +1 au streak
        - Si plus de 1 jour : reset à 1
        """
        today = datetime.utcnow().date()
        
        if self.last_activity_date == today:
            # Déjà actif aujourd'hui, ne rien faire
            return
        
        yesterday = today - timedelta(days=1)
        
        if self.last_activity_date == yesterday:
            # Activité hier, on continue le streak
            self.streak_count += 1
        elif self.last_activity_date < yesterday:
            # Plus d'un jour sans activité, reset
            self.streak_count = 1
        
        # Mettre à jour le meilleur streak
        if self.streak_count > self.best_streak:
            self.best_streak = self.streak_count
        
        self.last_activity_date = today
        self.updated_at = datetime.utcnow()
    
    def complete_challenge(self):
        """Marque le challenge du jour comme complété"""
        if not self.challenge_completed:
            self.challenge_completed = True
            self.challenge_progress = 100
            self.total_challenges_completed += 1
            self.update_streak()
            db.session.commit()
    
    def reset_daily_challenge(self):
        """Reset le challenge si on est un nouveau jour"""
        today = datetime.utcnow().date()
        
        if self.challenge_date < today:
            self.challenge_completed = False
            self.challenge_progress = 0
            self.challenge_date = today
            db.session.commit()


# ========================================
# 📅 TABLE HISTORIQUE DES CHALLENGES
# ========================================
class ChallengeHistory(db.Model):
    __tablename__ = 'challenge_history'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    challenge_text = db.Column(db.Text, nullable=False)
    completed = db.Column(db.Boolean, default=False)
    completion_date = db.Column(db.Date)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<ChallengeHistory user_id={self.user_id} completed={self.completed}>'