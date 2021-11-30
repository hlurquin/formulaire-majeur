# demande et encode le nom, le prénom et l’âge d’une personne
# retourne le nom et le prénom de la personne suivi du fait qu’elle soit majeur ou mineur

def rep_val_alpha(reponse, question):
    while not reponse.isalpha():
        reponse = input("erreur : carractère(s) invalide(s)\n{}".format(question))
    return reponse

def rep_val_age(reponse, question):
    while not reponse.isnumeric():
        reponse = input("erreur : carractère(s) invalide(s)\n{}".format(question))
    return reponse


q_nom =("quel est votre nom\n")
nom = input(q_nom)
nom = rep_val_alpha(nom, q_nom)

q_prenom =("quel est votre prenom\n")
prenom = input(q_prenom)
prenom= rep_val_alpha(prenom, q_nom)


q_age = ("quel est age\n")
age = input(q_age)
age = rep_val_age(age, q_age)
c=int(age)


if c >= 18:
    print("vous êtes", nom, prenom, "vous avez", age, "ans", "vous êtes donc majeur")
else:
    if c < 18:
        print("vous êtes",nom,prenom,"vous avez",age,"ans","vous êtes donc mineur")
