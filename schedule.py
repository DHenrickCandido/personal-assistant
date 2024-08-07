# TODO: calculo de prioridade com base nas datas de entrega
import json

class Tarefa:
    def __init__(self, nome, prioridade, area_vida ,feita=False):
        self.nome = nome
        self.prioridade = prioridade
        self.area_vida = area_vida
        self.feita = feita
        


areas_vida = {"Faculdade":2,
              "Apple_academy":1,
              "Trabalho":0,
              "PIBITI":3,
              "Autocuidado":"",
              "Codettes":5,
              "Flashly":4,
              "AI_Code_Analyzer":5,
              "Random_Projects":6
              }


class Calendar:
    def __init__(self):
        with open('calendar.json', 'r', encoding='utf-8') as file:
            self.calendar = json.load(file)

    def print_calendar(self):
        for day, hours in self.calendar.items():
            print(f"{day}:")
            for hour, value in hours.items():
                print(f"  {hour}: {value}")

    def adicionar_tarefa(self, dias, horarios, nome_tarefa):
        for dia in dias:
            for horario in horarios:
                self.calendar[dia][horario] = nome_tarefa


if __name__ == "__main__":
    calendar = Calendar()

    calendar.adicionar_tarefa(["Segunda","Terça", "Sexta"], ["14:00", "15:00", "17:00"], "Apple Academy")
    calendar.print_calendar()


