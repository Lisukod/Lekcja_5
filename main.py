import sys

max_box_capacity = int(sys.argv[1])
box_counter = 0
current_box = 0 
empty_kilos = 0
sent_kilos = 0
empty_kilos_max = 0

print("Podaj wage towaru do zapakowania. \nMin. 1kg \nMax. 10kg")

while True:
    weight_of_element = int(input())
    if weight_of_element == 0:
        if current_box > 0:
            box_counter += 1
            sent_kilos += current_box
            empty_kilos += (max_box_capacity - current_box)
            if empty_kilos_max < (max_box_capacity - current_box):
                empty_kilos_max = (max_box_capacity - current_box)  
        break
    elif weight_of_element < 0:
        print("Podales ujemną wartosć paczki. Proszę podac faktyczna wartosc")
        continue
    elif weight_of_element < 1 or weight_of_element > 10:
        print("Waga towaru do zapakowania wychodzi poza zakres")
        continue
    
    if (current_box + weight_of_element) > max_box_capacity:
        box_counter += 1
        sent_kilos += current_box
        empty_kilos += (max_box_capacity - current_box)
        if empty_kilos_max < (max_box_capacity - current_box):
            empty_kilos_max = (max_box_capacity - current_box)
        current_box = weight_of_element
    else:
        current_box += weight_of_element

print("Wysłane paczki: {}".format(box_counter))
print("Wysłane kilogramy: {}".format(sent_kilos))
print("Puste kilogramy: {}".format(empty_kilos))
print("Najwięcej wysłanych pustych kilogramów: {}".format(empty_kilos_max))


