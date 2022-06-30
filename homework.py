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

Структура программы
Каждый вид спортивной активности в модуле описан соответствующим классом:
- Бег → class Running ;
- Спортивная ходьба → class SportsWalking ;
- Плавание → class Swimming .

Конструктор каждого из классов получает информацию с датчиков:
- action, тип int — количество совершённых действий (число шагов
при ходьбе и беге либо гребков — при плавании);
- duration, тип float — длительность тренировки;
- weight, тип float — вес спортсмена.

Методы классов, которые отвечают за обработку данных:
- расчёт дистанции, которую пользователь преодолел за тренировку get_distance()
- расчёт средней скорости движения во время тренировки: get_mean_speed();
- расчёт количества потраченных калорий за тренировку: get_spent_calories();
- создание объекта сообщения о результатах тренировки: show_training_info().
"""


class InfoMessage:
    # Класс для создания объектов сообщений.
    # get_message() - метод для вывода сообщений на экран.
    # Объекты этого класса создаются вызовом метода show_training_info()
    # для классов тренировок.
    """Информационное сообщение о тренировке."""
    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float,
                 ) -> None:
        # имя класса тренировки
        self.training_type: str = training_type
        # длительность тренировки в часах
        self.duration: float = duration
        # дистанция в километрах, которую преодолел пользователь
        # за время тренировки
        self.distance: float = distance
        # средняя скорость, с которой двигался пользователь
        self.speed: float = speed
        # количество килокалорий, которое израсходовал пользователь
        # за время тренировки
        self.calories: float = calories

    # возвращает строку сообщения
    # числовые значения округляются при выводе до тысячных долей с помощью
    # format specifier
    # .3f обозначает фиксированные 3 знака после запятой
    def get_message(self) -> str:
        """Метод возвращает строку сообщения"""
        return (f"Тип тренировки: {self.training_type}; "
                f"Длительность: {self.duration:.3f} ч.; "
                f"Дистанция: {self.distance:.3f} км; "
                f"Ср. скорость: {self.speed:.3f} км/ч; "
                f"Потрачено ккал: {self.calories:.3f}.")


class Training:
    # Содержит все основные свойства и методы для тренировок.
    # Каждый класс, описывающий определённый вид тренировки, будет
    # дополнять и расширять этот базовый класс.
    """Базовый класс тренировки."""
    # расстояние, которое спортсмен преодолевает
    # за один шаг 0.65 метра (или гребок 1.38 метра когда переопределим)
    LEN_STEP: float = 0.65
    # константа для перевода значений из метров в километры. Её значение — 1000
    M_IN_KM: float = 1000
    # константа для перевода времени. Её значение — 60
    TIME_CONST = 60

    def __init__(self,                  # конструктор класса `Training`
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        # количество совершённых действий (число шагов при ходьбе и беге
        # либо гребков — при плавании)
        self.action: int = action
        # длительность тренировки
        self.duration: float = duration
        # вес спортсмена
        self.weight: float = weight

    # возвращает дистанцию (в километрах), которую преодолел пользователь
    # за время тренировки.
    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        # формула из задания - action * LEN_STEP / M_IN_KM
        return self.action * self.LEN_STEP / self.M_IN_KM

    # возвращает значение средней скорости движения во время тренировки в км/ч
    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        # формула из задания
        # преодоленная_дистанция_за_тренировку / время_тренировки
        return self.get_distance() / self.duration

    # расчёт количества потраченных калорий за тренировку
    # метод определяется в дочерних классах, расчет калорий отличается
    # в зависимости от тренировки
    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        raise NotImplementedError("Требуется определить метод для калорий")

    # метод возвращает объект класса сообщения о результатах тренировки
    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(self.__class__.__name__,
                           self.duration,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories()
                           )


# Все свойства и методы класса `Running` без изменений
# наследуются от базового класса.
# Исключение составляет только метод расчёта калорий, он переопределён.
class Running(Training):
    """Тренировка: бег."""

    coeff_calorie_1 = 18
    coeff_calorie_2 = 20

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        # формула из задания
        # (18 * средняя_скорость - 20) * вес_спортсмена / M_IN_KM
        # * время_тренировки_в_минутах
        return ((self.coeff_calorie_1 * self.get_mean_speed()
                - self.coeff_calorie_2) * self.weight
                / self.M_IN_KM * self.duration * self.TIME_CONST)


# Конструктор этого класса `SportsWalking` принимает
# дополнительный параметр height — рост спортсмена.
# Плюс метод расчёта калорий класса переопределён.
class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    coeff_calorie_1 = 0.035
    coeff_calorie_2 = 0.029

    def __init__(
            self,
            action: int,
            duration: float,
            weight: float,
            height: float) -> None:
        super().__init__(action, duration, weight)
        # Конструктор этого класса принимает дополнительный параметр
        # height — рост спортсмена
        self.height: float = height

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        # формула из задания
        # (0.035 * вес + (средняя_скорость**2 // рост) * 0.029 * вес)
        # * время_тренировки_в_минутах
        return ((self.coeff_calorie_1
                * self.weight
                + (self.get_mean_speed() ** 2 // self.height)
                * self.coeff_calorie_2 * self.weight)
                * self.TIME_CONST * self.duration)

# Конструктор класса `Swimming`, кроме свойств базового класса,
# принимает еще два параметра:
# - length_pool — длина бассейна в метрах;
# - count_pool — сколько раз пользователь переплыл бассейн.
# Переопределёны методы:
# - get_spent_calories() - расчета калорий
# - get_mean_speed()- рассчитывает среднюю скорость
# Переопределен параметр, атрибут базового класса LEN_STEP, потому что
# расстояние преодолеваемое за один гребок, отличается от длины шага.


class Swimming(Training):
    """Тренировка: плавание."""

    # расстояние, которое спортсмен преодолевает за один гребок 1.38 метра
    LEN_STEP: float = 1.38
    coeff_calorie_1 = 1.1
    coeff_calorie_2 = 2

    # Конструктор класса Swimming, кроме свойств базового класса,
    # принимает еще два параметра
    def __init__(
            self,
            action: int,
            duration: float,
            weight: float,
            length_pool: float,         # длина бассейна в метрах
            count_pool: float) -> None:
        super().__init__(action, duration, weight)
        self.length_pool: float = length_pool
        self.count_pool: float = count_pool

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        # формула из задания
        # длина_бассейна * count_pool / M_IN_KM / время_тренировки
        return (self.length_pool * self.count_pool
                / self.M_IN_KM / self.duration)

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        # формула из задания
        # (средняя_скорость + 1.1) * 2 * вес
        return ((self.get_mean_speed() + self.coeff_calorie_1)
                * self.coeff_calorie_2 * self.weight)


# Функция read_package() принимает на вход код тренировки
# и список её параметров
# В теле функции словарь, который сопоставляет коды тренировок и классы,
# которые нужно вызвать для каждого типа тренировки
# Функция определяет тип тренировки и создаёт объект соответствующего класса,
# передав ему на вход параметры, полученные во втором аргументе.
# Функция возвращает этот объект.
def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    workout: dict = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
    }
    if workout_type not in workout:
        raise ValueError(f"Такой тренировки - {workout_type}, не найдено")
    return workout[workout_type](*data)


# Функция main() принимает на вход экземпляр класса `Training`.
# для этого экземпляра вызван метод show_training_info()
# результат выполнения метода - объект класса InfoMessage,
# сохранённый в переменную info.
# Для объекта InfoMessage, сохранённого в переменной info,
# вызван метод get_message(),
# который возвращает строку сообщения с данными о тренировке
def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
