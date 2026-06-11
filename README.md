# Flower Detection using YOLOv8

Ovaj projekat predstavlja implementaciju sistema za automatsku detekciju i klasifikaciju cvetova primenom modela **YOLOv8**. Cilj projekta je razvoj modela koji može da prepozna i lokalizuje različite vrste cvetova na fotografijama, kao i analiza njegovih performansi korišćenjem standardnih evaluacionih metrika.

## Funkcionalnosti

* Detekcija cvetova na ulaznim slikama.
* Klasifikacija detektovanih objekata u tri klase:

  * Rose
  * Daisy
  * Tulip
* Treniranje modela na sopstveno pripremljenom i anotiranom skupu podataka.
* Evaluacija modela korišćenjem metrika Precision, Recall i mAP.
* Vizuelni prikaz rezultata detekcije na novim slikama.
* Jednostavan korisnički interfejs razvijen u Streamlit okruženju.
* Upravljanje Python okruženjem i zavisnostima korišćenjem `uv` alata.

---

## Struktura projekta

```text
flower_detection/
│
├── app/
│   └── ui.py
│
├── data/
│   ├── train/
│   ├── valid/
│   ├── test/
│   ├── data_colab.yaml
│   ├── data_local.yaml
│   └── data_config.yaml
│
├── models/
│   └── best.pt
│
├── src/
│   ├── split_dataset.py
│   ├── train_colab.py
│   ├── evaluate.py
│   └── predict.py
│
├── dokumentacija.md
├── README.md
├── .gitignore
├── .python-version
├── pyproject.toml
└── uv.lock
```

---

## Tok izrade projekta

1. Prikupljanje i priprema skupa podataka.
2. Anotacija slika u Supervisely okruženju.
3. Podela dataseta na trening, validacioni i test skup.
4. Treniranje YOLOv8 modela.
5. Evaluacija performansi modela.
6. Testiranje modela na novim slikama.
7. Razvoj Streamlit korisničkog interfejsa.
8. Organizacija i verzionisanje projekta korišćenjem Git i GitHub alata.

---

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

### Pokretanje Streamlit aplikacije

```bash
streamlit run app/ui.py
```

---

## Upravljanje okruženjem

Projekat koristi **uv** za upravljanje Python okruženjem i zavisnostima.

Za kreiranje okruženja i instalaciju potrebnih biblioteka dovoljno je pokrenuti:

```bash
uv sync
```

---

## Napomena

Dataset korišćen u ovom projektu pripremljen je i anotiran posebno za potrebe detekcije cvetova. Tokom razvoja modela izvršena je optimizacija skupa podataka kroz dopunu klasa i ponovno treniranje modela radi postizanja boljih performansi.

Detaljniji opis arhitekture modela, pripreme podataka, procesa treniranja i evaluacije nalazi se u fajlu **dokumentacija.md**.

---

## Autori

Danica Jovanović
Uroš Popović

Fakultet tehničkih nauka, Novi Sad
