from abc import ABC, abstractmethod
from functools import cache

from catboost import CatBoostRegressor
import numpy as np

class IParticleSwarmOptimization(ABC):
    model: CatBoostRegressor # Function for optimisation
    
    dimensions: int
    num_particles: int
    max_iter: int

    # PSO params
    w: float # Particle innertion
    c1: float  # Own best direction
    c2: float  # Best diection of other points

    @abstractmethod
    def predict(self):
        raise NotImplementedError


class ParticleSwarmOptimization:
    dimensions = 9
    num_particles = 30
    max_iter = 100

    w = 0.7
    c1 = 1.5
    c2 = 1.5

    def __init__(self, model: CatBoostRegressor) -> None:
        self.model = model

    
    @cache
    def predict(self, max_banners: int):
        def objective_function(x):
            return -1 if sum(x) > max_banners else self.model.predict(x)

        # Инициализация частиц
        particles = np.random.randint(0, max_banners, size=(self.num_particles, self.dimensions))
        velocities = np.random.randint(-1, 2, size=(self.num_particles, self.dimensions))
        personal_best_positions = particles.copy()
        personal_best_scores = np.apply_along_axis(objective_function, 1, particles)
        global_best_position = personal_best_positions[np.argmax(personal_best_scores)]
        global_best_score = np.max(personal_best_scores)

        # Основной цикл PSO
        for t in range(self.max_iter):
            for i in range(self.num_particles):
                # Обновление скорости
                r1 = np.random.rand(self.dimensions)
                r2 = np.random.rand(self.dimensions)
                velocities[i] = (self.w * velocities[i] +
                                self.c1 * r1 * (personal_best_positions[i] - particles[i]) +
                                self.c2 * r2 * (global_best_position - particles[i]))
                # Ограничение скорости, чтобы она оставалась целочисленной и не слишком большой
                velocities[i] = np.clip(np.round(velocities[i]), -1, 1)
                # Обновление позиции
                particles[i] = particles[i] + velocities[i]
                # Оценка новой позиции
                score = objective_function(particles[i])
                # Обновление личных лучших позиций
                if score > personal_best_scores[i]:
                    personal_best_positions[i] = particles[i].copy()
                    personal_best_scores[i] = score
                # Обновление глобальной лучшей позиции
                if score > global_best_score:
                    global_best_position = particles[i].copy()
                    global_best_score = score
        return global_best_position, global_best_score
