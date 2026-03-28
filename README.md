# 📘 Dispense Struttura della Materia

Repository per la scrittura collaborativa delle dispense di **Struttura della Materia** in LaTeX.

---

## 🚀 Setup iniziale

Clonare il repository:

```bash
git clone https://github.com/arpino-pixel/DispenseStrutturaDellaMateria.git
cd DispenseStrutturaDellaMateria
```

---

## 🔁 Workflow di lavoro

### ⚠️ Regola fondamentale

Prima di iniziare a lavorare:

```bash
git pull
```

---

### ✏️ Dopo aver modificato i file

```bash
git add .
git commit -m "descrizione modifiche"
git push
```

---

## 🧠 Regole di collaborazione

* Fare sempre `git pull` prima di iniziare
* Scrivere commit chiari (es. `aggiunta tabella capitolo 2`)
* Evitare di modificare la stessa parte di file contemporaneamente
* Dividersi il lavoro per sezioni/capitoli
* NON caricare file temporanei di LaTeX (`.aux`, `.log`, ecc.)

---

## 📁 Struttura del progetto

```text
DispenseStrutturaDellaMateria/
├── main.tex              # file principale
├── sections/             # capitoli o sezioni
│   ├── introduzione.tex
│   ├── capitolo1.tex
│   └── capitolo2.tex
├── images/               # immagini
├── bibliography.bib      # bibliografia (opzionale)
├── .gitignore
└── README.md
```

---

## 🧩 Uso consigliato di LaTeX

Nel file principale (`main.tex`):

```latex
\input{sections/introduzione}
\input{sections/capitolo1}
```

👉 In questo modo ogni persona lavora su file diversi → meno conflitti

---

## ⚙️ Compilazione

### Metodo semplice:

```bash
pdflatex main.tex
```

### Metodo consigliato:

```bash
latexmk -pdf main.tex
```

---

## ⚠️ Gestione conflitti

Se Git segnala un conflitto:

```text
<<<<<<< HEAD
tuo testo
=======
testo altro
>>>>>>> main
```

👉 Modificare manualmente scegliendo la versione corretta, poi:

```bash
git add .
git commit -m "risolto conflitto"
git push
```

---

## 📌 Buone pratiche

* Usare `booktabs` per le tabelle
* Tenere le immagini in `images/`
* Usare label coerenti (`fig:`, `tab:`)
* Scrivere codice LaTeX pulito e leggibile

---

## 💬 Note

Questo progetto è pensato per essere:

* collaborativo
* modulare
* facilmente espandibile (tipo appunti → dispense → quasi tesi)

---

## 👨‍💻 Autori

* Mattia Arpino
* Collaboratori del corso

