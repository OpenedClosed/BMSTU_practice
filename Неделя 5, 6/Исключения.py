import datetime
import json

from api import register_booking


class Booking:
    def __init__(self, room_name, start, end):
        self.room_name = room_name
        self.start = start
        self.end = end
        if self.start > self.end:
            raise ValueError('Некорректное время')
        
    @property
    def start_date(self):
        return self.start.strftime('%Y-%m-%d')

    @property
    def end_date(self):
        return self.end.strftime('%Y-%m-%d') 

    @property
    def start_time(self):
        return self.start.time().strftime('%H:%M')

    @property
    def end_time(self):
        return self.end.time().strftime('%H:%M')

    @property
    def duration(self):
        return int(((self.end - self.start).total_seconds()) / 60)


        

def create_booking(room_name, start, end):
    print('Начинаем создание бронирования')
    booking_obj = Booking(room_name, start, end)
    try:
        system_answer = register_booking(booking_obj)
        if system_answer is True:
            msg = 'Бронирование создано'
        elif system_answer is False:
            msg = 'Комната занята'
    except KeyError:
        system_answer = False
        msg = 'Комната не найдена'
    finally:
        print('Заканчиваем создание бронирования')
    result = json.dumps({
        'created': system_answer,
        'msg': msg,
        'booking': {
            'room_name': booking_obj.room_name,
            'start_date': booking_obj.start_date,
            'start_time': booking_obj.start_time,
            'end_date': booking_obj.end_date,
            'end_time': booking_obj.end_time,
            'duration': booking_obj.duration
        }
    }, ensure_ascii=False)
    return result


if __name__ == "__main__":
    result = create_booking(
        "Вагнер",
        datetime.datetime(2022, 9, 1, 14),
        datetime.datetime(2022, 9, 1, 15, 15)
    )
    print(result)
