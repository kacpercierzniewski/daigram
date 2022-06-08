# dAIgram

- tutaj trzymamy kod związany z OCR diagramowym.

# Jak zacząć
- instalujemy pythona
- w pliku requirements.txt są zależności.  Instalujemy je komendą
```
pip3 install -r requirements.txt
```


# moduły 
## image processing
 Moduł do przetwarzania obrazu. Aktualnie mamy w nim 2 główne ficzerki:
 - procesowanie obrazu (process_image.py) który odpowiada za przerobienie zdjęcia na obraz "binarny" tzn czarno biały. W procesie tym występuje też odszumianie obrazu przez co diagramy narysowane na kartce w kratkę np. powinny być również rozpoznane
 - dodawanie labelek (add_labels_to_shapes.py) który odpowiada za dodanie losowego tekstu do znalezionych kształtów. 


