# Flower Detection using YOLOv8

Ovaj projekat predstavlja implementaciju sistema za detekciju i klasifikaciju cvetova primenom modela YOLOv8. Cilj projekta je razvoj modela koji može da prepozna i lokalizuje različite vrste cvetova na fotografijama, uz analizu njegovih performansi kroz standardne evaluacione metrike.

## Funkcionalnosti

* Detekcija cvetova na ulaznim slikama.
* Klasifikacija detektovanih objekata u tri klase:

  * Rose
  * Daisy
  * Tulip
* Treniranje modela na sopstveno pripremljenom i anotiranom skupu podataka.
* Evaluacija modela korišćenjem metrika Precision, Recall i mAP.
* Vizuelni prikaz rezultata detekcije na novim slikama.

## Struktura projekta

```text
flower_detection/
│
├── data/
│   ├── train/
│   ├── valid/
│   ├── test/
│   ├── data.yaml
│   └── data_config.yaml
│
├── src/
│   ├── split_dataset.py
│   ├── train_colab.py
│   ├── evaluate.py
│   └── predict.py
│
├── models/
├── results/
├── runs/
└── README.md
```

## Tok izrade projekta

1. Prikupljanje i priprema skupa podataka.
2. Anotacija slika u Supervisely okruženju.
3. Podela podataka na trening, validacioni i test skup.
4. Treniranje YOLOv8 modela.
5. Evaluacija performansi modela.
6. Testiranje modela na novim slikama i analiza dobijenih rezultata.

## Pokretanje projekta

### Treniranje modela

```bash
python src/train_colab.py
```

### Evaluacija modela

```bash
python src/evaluate.py
```

### Predikcija na novim slikama

```bash
python src/predict.py
```

## Napomena

Dataset korišćen u ovom projektu pripremljen je i anotiran posebno za potrebe detekcije cvetova. Tokom razvoja modela izvršena je optimizacija skupa podataka kroz dopunu klasa i ponovno treniranje modela radi postizanja boljih performansi.

## Autor

Danica Jovanović, Uroš Popović
