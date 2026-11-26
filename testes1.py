'''

Scrivi un prgoramma che riceva un nome obbligatorio e stmapi un saluto.
1. Definisci il posizionale nome. Aggiungi un testo help che spieghi che cosa inserire 
2. Leggi gli argomenti con parse_args() e stampa Ciao, seguito dal nome e da!, come 
'''

from argparse import ArgumentParser

p = ArgumentParser(description="Saluta una persona")
p.add_argument(
    "nome", 
    help="Inserisci il nome della persona da salutare"
)
p.add_argument(
    "-n", "--ripeti",
    type=int,
    nargs="?",
    default=1,
    help="Numero di volte da ripetere il saluto"
)
p.add_argument(
    "-m", "--maiuscolo",
    action="store_true",
    help="Stampa il saluto in maiuscolo"
)
p.add_argument(
    "--lingua",
    choices=["it", "en"],
    default="it",
    help="Lingua del saluto (it per italiano, en per inglese)"
)
args = p.parse_args()
messaggio = f"Ciao, {args.nome}!"
print(messaggio)

'''
ES 2
Un'opzione con valore e default. Aggiungi al saluto l'opzione -n/-n ripeti '''
for _ in range(args.ripeti -1):
    print(messaggio)

'''
ES 3
flag booleano che se -m o --maiuscolo, fa la stampa in maiuscolo
'''
if args.maiuscolo:
    messaggio = messaggio.upper()

'''
es 4
Il saluto deve supprotare --lingua it oppure en '''
if args.lingua == "en":
    messaggio = f"Hello, {args.nome}!"