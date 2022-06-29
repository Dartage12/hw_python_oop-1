"""
Программный модуль фитнес-трекера, 
который обрабатывает данные для трех видов тренировок: 
для бега, спортивной ходьбы и плавания.

Этот модуль
- принимает от блока датчиков информацию о прошедшей тренировке,
- определяет вид тренировки,
- рассчитывает результаты тренировки,
- выводит информационное сообщение о результатах тренировки.

Информационное сообщение включает такую информацию как:
- тип тренировки (бег, ходьба или плавание);
- длительность тренировки
- дистанция, которую преодолел пользователь, в километрах;
- среднюю скорость на дистанции, в км/ч;
- расход энергии, в килокалориях.
"""

class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float,
                 ) -> None:
        self.training_type: str = training_type
        self.duration: float = duration
        self.distance: float = distance
        self.speed: float = speed
        self.calories: float = calories
    
    def get_message(self) -> str:
        """Метод возвращает строку сообщения"""
        return (f"Тип тренировки: {self.training_type:.3f};"
                f"Длительность: {self.duration:.3f} ч.;"
                f"Дистанция: {self.distance:.3f} км;"
                f"Ср. скорость: {self.speed:.3f} км/ч;"
                f"Потрачено ккал: {self.calories:.3f}.")


class Training:
    """Базовый класс тренировки."""
    
    LEN_STEP: float = 0.65  # расстояние, которое спортсмен преодолевает за один шаг 0.65 метра (или гребок 1.38 метра когда переопределим)
    M_IN_KM: float = 1000   # константа для перевода значений из метров в километры. Её значение — 1000
    TIME_CONST = 60         # константа для перевода времени

    def __init__(self,                  # конструктор класса `Training`
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action: int = action       # количество совершённых действий (число шагов при ходьбе и беге либо гребков — при плавании)
        self.duration: float = duration # длительность тренировки
        self.weight: float = weight     # вес спортсмена

    # расчёт дистанции, которую пользователь преодолел за тренировку
    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        # action * LEN_STEP / M_IN_KM 
        return (self.action * self.LEN_STEP / self.M_IN_KM)

    # расчёт средней скорости движения во время тренировки
    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        # преодоленная_дистанция_за_тренировку / время_тренировки 
        return (self.get_distance() / self.duration)
    
    # расчёт количества потраченных калорий за тренировку
    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        raise NotImplementedError("Требуется определить метод для калорий")
    
    # создание объекта сообщения о результатах тренировки
    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        pass


class Running(Training):
    """Тренировка: бег."""

    coeff_calorie_1 = 18
    coeff_calorie_2 = 20

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        # (18 * средняя_скорость - 20) * вес_спортсмена / M_IN_KM * время_тренировки_в_минутах 
        return ((self.coeff_calorie_1 * self.get_mean_speed() - self.coeff_calorie_2) 
                * self.weight / self.M_IN_KM * self.duration * self.TIME_CONST)



class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    
    coeff_calorie_1 = 0.035
    coeff_calorie_2 = 0.029

    def __init__(self,
            action: int,
            duration: float,
            weight: float,
            ) -> None:
    super().__init__(action, duration, weight)
    # Конструктор этого класса принимает дополнительный параметр height — рост спортсмена
    self.height: float = height

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        # (0.035 * вес + (средняя_скорость**2 // рост) * 0.029 * вес) * время_тренировки_в_минутах
        return ((self.coeff_calorie_1 
                * self.weight 
                + (self.get_mean_speed() ** 2 // self.height)
                self.coeff_calorie_2 * self.weight))


class Swimming(Training):
    """Тренировка: плавание."""

    LEN_STEP: float = 1.38 # расстояние, которое спортсмен преодолевает за один гребок 1.38 метра
    coeff_calorie_1 = 1.1
    coeff_calorie_2 = 2

    # Конструктор класса Swimming, кроме свойств базового класса, принимает еще два параметра
    def __init__(self,
            action: int,
            duration: float,
            weight: float,
            length_pool: float, # длина бассейна в метрах
            count_pool: float,  # сколько раз пользователь переплыл бассейн
            ) -> None:
    super().__init__(action, duration, weight)
    self.length_pool: float = length_pool
    self.count_pool: float = count_pool

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        # длина_бассейна * count_pool / M_IN_KM / время_тренировки
        return (self.length_pool * self.count_pool / self.M_IN_KM / self.duration)

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        # (средняя_скорость + 1.1) * 2 * вес
        return ((self.get_mean_speed() + self.coeff_calorie_1) * self.coeff_calorie_2 * self.weight)


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

