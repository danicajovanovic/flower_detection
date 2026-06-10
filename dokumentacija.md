# Detekcija i klasifikacija cvetova primenom YOLOv8 modela

## Tema

Tema ovog projekta je razvoj sistema za automatsku detekciju i klasifikaciju cvetova korišćenjem modela **YOLOv8 (You Only Look Once)**. Sistem kao ulaz prihvata fotografiju koja može sadržati jedan ili više cvetova, dok je izlaz skup detektovanih objekata sa odgovarajućim klasama i koordinatama bounding box-ova.

U okviru projekta razmatrane su tri klase:

* Rose
* Daisy
* Tulip

Cilj projekta je razvoj modela koji može pouzdano da prepozna i lokalizuje cvetove na novim slikama, kao i analiza performansi modela korišćenjem standardnih evaluacionih metrika.

---

# Priprema podataka

Za potrebe projekta korišćen je sopstveno pripremljen i anotiran skup podataka. Slike su prikupljene iz javno dostupnih izvora, a anotacija je izvršena u okruženju **Supervisely**, gde je svakom objektu dodeljena odgovarajuća klasa i bounding box.

Ukupan broj slika u dataset-u iznosi **498**.

Nakon anotacije izvršena je podela na:

* trening skup – **348 slika**
* validacioni skup – **99 slika**
* test skup – **51 slika**

Podaci su eksportovani u YOLO formatu i korišćeni za treniranje modela.

---

# Balansiranje skupa podataka

Analizom dataseta primećeno je da klase nisu ravnomerno zastupljene. Klasa **Rose** sadržala je veći broj uzoraka u odnosu na klase Daisy i Tulip, što je moglo dovesti do favorizovanja jedne klase tokom procesa treniranja.

Kako bi se smanjio uticaj disbalansa:

* prikupljene su dodatne slike klasa Daisy i Tulip,
* izvršena je nova anotacija i eksportovanje dataseta,
* model je ponovo treniran na ažuriranom skupu podataka.

Na ovaj način poboljšana je sposobnost modela da ravnomerno prepoznaje sve klase.

---

# Model

Za realizaciju projekta korišćen je model **YOLOv8n**, razvijen od strane kompanije Ultralytics.

YOLO pripada grupi jednoprohodnih (single-stage) detektora objekata, što znači da tokom jednog prolaza kroz neuronsku mrežu istovremeno vrši:

* detekciju objekata,
* određivanje njihovih koordinata,
* klasifikaciju objekata.

Ovakav pristup omogućava visok stepen tačnosti uz veoma brzo izvršavanje.

---

# Arhitektura YOLOv8 modela

YOLOv8 model sastoji se iz tri osnovna dela.

## Backbone

Backbone predstavlja deo mreže zadužen za izdvajanje karakteristika sa ulazne slike.

Kroz niz konvolucionih slojeva model prepoznaje:

* ivice,
* teksture,
* oblike,
* složenije vizuelne karakteristike.

Rezultat rada backbone dela su feature mape koje sadrže informacije potrebne za detekciju objekata.

---

## Neck

Neck povezuje backbone i završni deo mreže.

Njegova uloga je objedinjavanje karakteristika različitih nivoa, čime se omogućava uspešna detekcija objekata različitih veličina.

Kombinovanjem informacija sa više nivoa model postiže bolje rezultate pri prepoznavanju sitnijih i složenijih objekata.

---

## Detection Head

Detection Head predstavlja završni deo neuronske mreže.

Za svaki pronađeni objekat određuje:

* koordinate bounding box-a,
* verovatnoću postojanja objekta,
* pripadnost jednoj od definisanih klasa.

Na osnovu ovih podataka generiše se konačna predikcija.

---

# Proces treniranja

Model je treniran korišćenjem biblioteke **Ultralytics YOLOv8** i PyTorch okruženja.

Prilikom treniranja korišćeni su sledeći parametri:

* model: YOLOv8n
* veličina ulazne slike: 640 × 640
* batch size: 8
* patience: 10
* broj epoha: prilagodljiv u zavisnosti od eksperimenta

Najbolji model automatski se čuva u fajlu `best.pt`, dok se model iz poslednje epohe čuva u fajlu `last.pt`.

---

# Podešavanje težina modela

Na početku procesa treniranja koriste se početne težine modela.

Tokom svake epohe izvršava se sledeći postupak:

1. Slika prolazi kroz neuronsku mrežu.
2. Model daje predikciju.
3. Predikcija se poredi sa stvarnom anotacijom.
4. Izračunava se greška modela (loss).
5. Backpropagation algoritam računa kako treba promeniti težine.
6. Optimizacioni algoritam ažurira težine mreže.

Ponavljanjem ovog procesa model postepeno uči karakteristike koje razlikuju pojedine vrste cvetova.

---

# Evaluacija modela

Za procenu kvaliteta modela korišćene su standardne metrike za detekciju objekata.

## Precision

Predstavlja odnos tačno detektovanih objekata i ukupnog broja detekcija koje je model napravio.

Visoka vrednost ove metrike ukazuje na mali broj lažnih detekcija.

---

## Recall

Predstavlja odnos pronađenih objekata i ukupnog broja stvarnih objekata na slikama.

Veća vrednost Recall metrike znači da model propušta manji broj objekata.

---

## mAP50

Mean Average Precision pri IoU pragu od 50%.

Predstavlja jednu od najvažnijih metrika za procenu kvaliteta modela za detekciju objekata.

---

## mAP50-95

Predstavlja strožu procenu performansi modela jer računa prosečnu preciznost kroz više IoU pragova.

Ova metrika daje realniju sliku ukupnih performansi sistema.

---

# Analiza izazova i poteškoća

Tokom razvoja projekta identifikovano je više izazova koji su uticali na performanse sistema.

### Disbalans klasa

Različita zastupljenost pojedinih klasa rešena je proširenjem dataseta i ponovnim treniranjem modela.

### Problemi pri eksportovanju dataseta

Prilikom izvoza iz Supervisely okruženja pojavili su se problemi sa praznim label fajlovima zbog neodgovarajuće geometrije anotacija.

Problem je rešen konverzijom anotacija u odgovarajući bounding box format i ponovnim eksportovanjem dataseta.

### Različita razvojna okruženja

Za treniranje modela korišćen je Google Colab, dok su lokalni razvoj, testiranje i evaluacija realizovani u Visual Studio Code okruženju.

Zbog različitih putanja bilo je potrebno prilagoditi konfiguracione fajlove za lokalno i cloud okruženje.

### Analiza predikcija

Najveći broj grešaka javljao se u slučajevima:

* preklapanja cvetova,
* lošeg osvetljenja,
* veoma sličnih vizuelnih karakteristika između pojedinih klasa.

---

# Zaključak

Razvijeni sistem uspešno demonstrira mogućnost automatske detekcije i klasifikacije cvetova primenom savremenih metoda dubokog učenja.

Rezultati projekta pokazuju da pravilna priprema i balansiranje dataseta imaju značajan uticaj na performanse modela. Primenom YOLOv8 arhitekture ostvarena je efikasna detekcija objekata uz relativno malu računarsku zahtevnost.

Ovako realizovan sistem predstavlja dobru osnovu za dalja unapređenja, kao što su proširenje broja klasa, povećanje skupa podataka i dodatna optimizacija hiperparametara radi poboljšanja tačnosti modela.

---

**Danica Jovanović, Uroš Popović**

**Fakultet tehničkih nauka, Novi Sad**
