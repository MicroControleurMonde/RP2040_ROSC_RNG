# RP2040 ROSC RNG 🇫🇷


![Image locale](https://github.com/MicroControleurMonde/RP2040-RNG/blob/main/Reports/RP2040-resizeimage3.png)

Une bibliothèque Micro-python qui fournit une interface pour générer un nombre aléatoire en utilisant la méthode recommandée (lecture du ROSC) par Raspberry.
- Bibliothèque : `rosc_random_generator.py` - Bibliothèque Python pour générer des nombres aléatoires
- Script de test : `test_rosc_random_generator.py` - Script d'exemple montrant comment utiliser la bibliothèque.

##### (Mise à jour du 22.12.2024)
- `Test_ROSC.py` - Le code initial que j'ai utilisé pour tester le RP2040 ROSC.
---

## Index

1. [Contexte](#contexte)
2. [Description du projet](#description-du-projet)
3. [Prérequis](#prérequis)
4. [Utilisation](#utilisation)
5. [Exemple de sortie](#exemple-de-sortie)
6. [Fonctionnement](#fonctionnement)
7. [Test de performance](#test-de-performance)
8. [Tests statistiques et de qualité](#tests-statistiques-et-de-qualité)
9. [Remerciements](#remerciements)
10. [Avertissement](#avertissement)
11. [Hommage spécial](#hommage-spécial)

---

## Contexte

La fondation Raspberry a récemment mis à jour la fiche technique de leur Pico :
`Datasheet - Build-date: 2024-10-15 / Build-version: eec2b0c-clean`

[Fiche technique RP2040 Pico (Chapitre 2.17)](https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf)

**Page 222. Chapitre 2.17. Oscillateur à anneau (ROSC)**, voici ce que l'on peut y lire :

    2.17.5. Générateur de nombres aléatoires
    
    Si les horloges système fonctionnent à partir du XOSC et/ou des PLL, le ROSC peut être utilisé pour générer des nombres
    aléatoires. Il suffit d'activer le ROSC et de lire le registre RANDOMBIT pour obtenir un nombre aléatoire sur 1 bit,
    et de le lire n fois pour obtenir une valeur sur n bits. Cela ne répond pas aux exigences de randomisation pour les
    systèmes de sécurité car il peut être compromis, mais cela peut être utile dans des applications moins critiques.
    Si les cœurs fonctionnent à partir du ROSC, la valeur ne sera pas aléatoire car le timing de la lecture du registre
    sera corrélé à la phase du ROSC.

Le générateur de nombres aléatoires utilise le ROSC (Oscillateur à résonance) pour produire des bits aléatoires.

---

## Description du projet

Ce projet implémente un générateur de nombres aléatoires véritablement aléatoires (TRNG) utilisant le microcontrôleur RP2040. Le générateur utilise l'oscillateur à anneau comme recommandé dans la fiche technique.

## Prérequis

- Microcontrôleur basé sur RP2040.
- Firmware MicroPython installé sur la carte.
- **`machine`**, **`time`** (intégrés avec MicroPython).

## Utilisation

1. **rosc_random_generator.py – Bibliothèque pour générer des nombres aléatoires**

Cette bibliothèque Python fournit une classe `ROSCRandomGenerator` qui génère des nombres aléatoires basés sur le ROSC du RP2040.

2. **test_rosc_random_generator.py – Script d'exemple**

Ce script importe la classe `ROSCRandomGenerator` depuis rosc_random_generator.py et génère des nombres aléatoires.

### Installation
- Sauvegardez ces codes dans des fichiers nommés `rosc_random_generator.py` et `test_rosc_random_generator.py`.
- Pour utiliser cette bibliothèque dans un autre projet, importez-la comme n'importe quel module Python.

### Exemple de sortie :

Le générateur de nombres aléatoires RP2040 ROSC génère des nombres entiers aléatoires sous forme de **valeurs sur 32 bits**.

        ROSC stable. Début de la génération des nombres aléatoires...

        Valeur aléatoire # 1 :	 2880935910
        Valeur aléatoire # 2 :	 3756622924
        Valeur aléatoire # 3 :	 4041343900
        Valeur aléatoire # 4 :	 41689329
        Valeur aléatoire # 5 :	 1860732466
        Valeur aléatoire # 6 :	 2376253135
        Valeur aléatoire # 7 :	 2057898098
        Valeur aléatoire # 8 :	 3392796777
        Valeur aléatoire # 9 :	 1501861143
        Valeur aléatoire # 10 :	 238555703

## Fonctionnement

- 1 - Le programme déclare les variables et constantes nécessaires pour interagir avec le ROSC.
- 2 - Il vérifie l'état du ROSC pour s'assurer qu'il est stable.
- 3 - Si le ROSC est stable, il génère des valeurs aléatoires sur 32 bits, affichant chaque valeur et vérifiant régulièrement la stabilité du ROSC.
- 4 - En cas d'instabilité détectée, le programme réinitialise le ROSC et attend qu'il se stabilise avant de continuer.
- 5 - Une fois les valeurs générées, il affiche un message de fin.

De cette manière, ce processus assure que le ROSC est correctement initialisé et stable avant de générer des valeurs aléatoires, et gère la réinitialisation en cas de problème de stabilité pendant le processus.

## Test de performance

**Avertissement** : `sans écriture` sur mémoire flash !

- Temps estimé pour générer 1'425'424 valeurs : **2'143 secondes** (environ 35 minutes)
- Temps moyen par valeur : **0.0015 sec**
- Débit : **2660 octets/sec**
- Nombre de valeurs générées par seconde : **665 valeurs/sec**

- [Échantillon de données](https://github.com/MicroControleurMonde/RP2040_ROSC_RNG/blob/main/Reports/rp2040_rosc_rng_1425424.bin)

## Tests statistiques et de qualité

**Note** : Suite à un rappel de Scruss [(Lien)](https://github.com/scruss), j'ai changé le format du fichier de sortie d'ASCII en binaire.

        Lorsque les entiers aléatoires sont convertis en chaînes ASCII, il y a une perte d'entropie ! Un entier de 32 bits 
        représente une valeur qui peut être exprimée dans une plage de 4'294'967'296 valeurs possibles (de 0 à 2^32 - 1). 
        Cette plage contient 32 bits d'entropie.
        
        En raison de la manière dont les caractères ASCII sont représentés (par exemple, les chiffres ou les lettres), 
        une partie de l'entropie est perdue du fait du nombre limité de caractères possibles. Chaque caractère en ASCII 
        contient environ 3,45 bits d'entropie au lieu des 8 bits d'entropie possibles pour un octet complet. 
        (Log₂ 11 ≈ 3.459)

### 1. Rapport de test `Ent`
#### (Mise à jour du 22.12.2024)

([www.fourmilab.ch](https://www.fourmilab.ch/random/)) John Walker
- Taille de l'échantillon : **5.43 Mo**
- Total généré : **1'425'424 valeurs**
- Entropie = **7.973888** bits par octet (mesure de l'aléa - Max = **8**)

- [Rapport Ent - Brut](https://github.com/MicroControleurMonde/RP2040_ROSC_RNG/blob/main/Reports/Ent_rp2040_rosc_rng_1425424.txt)
- [Analyse du rapport Ent](https://github.com/MicroControleurMonde/RP2040_ROSC_RNG/blob/main/Reports/Ent_1Mil_Report_Analyse.md)

[Représentation en nuage de points](https://github.com/MicroControleurMonde/RP2040_ROSC_RNG/blob/main/Reports/Scatter%20Plot.png) [Grande taille]

![Scatter](https://github.com/MicroControleurMonde/RP2040_ROSC_RNG/blob/main/Reports/Webp.net-resizeimage2.png)

[Histogramme des valeurs](https://github.com/MicroControleurMonde/RP2040_ROSC_RNG/blob/main/Reports/Histogram%20of%20Random%20Numbers.png) [Grande taille]

![Histogramme](https://github.com/MicroControleurMonde/RP2040_ROSC_RNG/blob/main/Reports/Webp.net-resizeimage.png)

### 2. Rapport de test `Dieharder`
##### (Mise à jour du 22.12.2024)
(https://webhome.phy.duke.edu/~rgb/General/dieharder.php) Robert G. Brown

- Taille de l'échantillon : **5.43 Mo**
- Total généré : **1'425'424 valeurs**

- [Rapport Dieharder - Brut](https://github.com/MicroControleurMonde/RP2040_ROSC_RNG/blob/main/Reports/Dieharder_rp2040_rosc_rng_1425424.txt)
- [Analyse du rapport Dieharder](https://github.com/MicroControleurMonde/RP2040_ROSC_RNG/blob/main/Reports/Dieharder_1Mil_Report_Analyse.md)

### 3. `TestU01` (Batterie Rabbit)
##### (Mise à jour du 24.12.2024)
(https://simul.iro.umontreal.ca/testu01/tu01.html)
- Extrait de code C (seulement le Main) :

        int main() {
            // Chemin du fichier binaire
            const char *filename= "/home/user_name/rp2040_rosc_rng_1425424.bin";
            // Créer un générateur à partir du fichier
            unif01_Gen *gen = create_gen(filename);
            if (gen == NULL) {
             return 1;
            }
            // Exemple avec la batterie Rabbit
            printf("Début des tests à partir du fichier\n");
            bbattery_Rabbit(gen, 1000); // Test sur 1000 bits

            // Libération de la mémoire
            close(global_gen->file);
            free(global_gen); // Libérer l'état du générateur
            free(gen); // Libérer le générateur
            
            return 0;
  
[Rapport TestU01 Brut](https://github.com/MicroControleurMonde/RP2040_ROSC_RNG/blob/main/Reports/TestU01_results_test.txt)
  
[Analyse du Rapport TestU01](https://github.com/MicroControleurMonde/RP2040_ROSC_RNG/blob/main/Reports/TestU01_Rabbit.md)

- Certains p-values faibles suggèrent que le générateur peut avoir des _**structures ou motifs non aléatoires**_ détectés par ces tests.

### 4. `rngtest` (Validation FIPS 140-2)
##### (Mise à jour du 24.12.2024)
(https://salsa.debian.org/hmh/rng-tools/)
- Résultat du test : **tous les tests FIPS ont échoué** :warning:
  
  Ce qui implique un traitement post-générateur...

[Rapport `rngtest`](https://github.com/MicroControleurMonde/RP2040_ROSC_RNG/blob/main/Reports/rngtest_rp2040_rosc_rng_1425424.txt)

[Analyse du Rapport `rngtest`](https://github.com/MicroControleurMonde/RP2040_ROSC_RNG/blob/main/Reports/rngtest_rp2040_rosc_rng_1425424.md)

### 5. `djent` (David Johnston - Random Number Generators―Principles and Practices)  ISBN 978-1501515132
##### (Updated 25.12.2024)
- `djent` : Une réimplémentation du programme de test de nombres aléatoires (Ent) de feu John Walker/Fourmilab, avec plusieurs améliorations.

(https://github.com/dj-on-github/djent)

:warning:  N'oubliez pas d'installer MPFR (dépendances):
`sudo apt-get install libmpfr-dev libgmp-dev` :warning:

Et de mettre à jour le `Makefile` en conséquence avant la compilation !

[`djent` Raw Report](https://github.com/MicroControleurMonde/RP2040_ROSC_RNG/blob/main/Reports/djent_raw_report.txt)

[`djent` report Analysis](https://github.com/MicroControleurMonde/RP2040_ROSC_RNG/blob/main/Reports/djent_report_analysis.md)


## Référence

Le projet est basé sur le microcontrôleur RP2040, et son firmware MicroPython.
- `Waveshare RP2040-Plus: MicroPython ef518cbf2-dirty du 2023-03-24 ;`
- `XIAO seed studio: MicroPython v1.22.1 du 2024-01-05 ;`

## Avertissement

Le code contenu dans ce dépôt est fourni "tel quel", sans aucune garantie de performance, précision ou résultat. L'auteur ne saurait être tenu responsable des dommages directs ou indirects pouvant résulter de l'utilisation de ce code, y compris, mais sans s'y limiter, la perte de données ou l'interruption de service.

L'utilisation de ce code est entièrement à vos risques et périls. Veuillez vous assurer de bien comprendre le code avant de l'utiliser dans un environnement de production ou de l'intégrer dans vos projets.

## Hommage spécial :

### Décès de John Walker

Nous sommes profondément attristés par le décès de John Walker, l'un des fondateurs d'Autodesk. Il est décédé chez lui en Suisse, le 2 février 2024, à l'âge de 74 ans.

[L'annonce a été partagée ici.](https://www.engineering.com/a-cad-legend-passes-autodesk-founder-john-walker-1949-to-2024/)

