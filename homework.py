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
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        pass
    def show_training_info(self) -> str:
        """Метод для вывода сообщений на экран"""
        pass
    def get_message(self) -> str:
        """Метод возвращает строку сообщения"""
        # print(f'Тип тренировки: {training_type}; Длительность: {duration} ч.;' 
        # f'Дистанция: {distance} км; Ср. скорость: {speed} км/ч; Потрачено ккал: {calories}.')
        pass
    pass


class Training:
    """Базовый класс тренировки."""
    
    LEN_STEP: float = 0.65  # расстояние, которое спортсмен преодолевает за один шаг 0.65 метра (или гребок 1.38 метра когда переопределим)
    M_IN_KM: float = 1000   # константа для перевода значений из метров в километры. Её значение — 1000

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
        return self.action * self.LEN_STEP / self.M_IN_KM

    # расчёт средней скорости движения во время тренировки
    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        # преодоленная_дистанция_за_тренировку / время_тренировки 
        return self.get_distance() / self.duration
    
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

    def __init__(self,
                action: int,
                duration: float,
                weight: float,
                ) -> None:
        super().__init__(action, duration, weight)

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        # coeff_calorie_1 = 18
        # coeff_calorie_2 = 20 
        # (18 * средняя_скорость - 20) * вес_спортсмена / M_IN_KM * время_тренировки_в_минутах 
        pass


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    
    def __init__(self,
                action: int,
                duration: float,
                weight: float,
                ) -> None:
        pass

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        # coeff_calorie_1 = 0.035
        # coeff_calorie_2 = 0.029 
        # (0.035 * вес + (средняя_скорость**2 // рост) * 0.029 * вес) * время_тренировки_в_минутах
        pass


class Swimming(Training):
    """Тренировка: плавание."""

    def __init__(self,
            action: int,
            duration: float,
            weight: float,
            ) -> None:
        pass
    pass

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        # distance = action * LEN_STEP / M_IN_KM 
        pass

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        # длина_бассейна * count_pool / M_IN_KM / время_тренировки
        pass

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        # coeff_calorie_1 = 0.035
        # coeff_calorie_2 = 0.029 
        # (средняя_скорость + 1.1) * 2 * вес  
        pass




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

