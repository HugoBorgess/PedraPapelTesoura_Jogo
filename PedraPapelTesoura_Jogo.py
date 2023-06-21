
import random

my_dict={'1':"Pedra",'2':"Papel",'3':"Tesoura"}
user_count=0
comp_count=0

games=int(input("\nInsira a quantidade de vezes que você quer jogar: "))

while(comp_count+user_count<games):

	flag=0

	user_input=input("\nEscolha do jogador: ")[0]
	user_input=user_input.upper()

	for i in my_dict.keys():
		if(user_input==i):
			flag=1
			break
	if(flag!=1):
		print("Escolha inválida")
		continue

	comp_input=random.choice(list(my_dict.keys()))

	print("Escolha do computador: ", my_dict[comp_input])
	if ( user_input=='1' and comp_input=='2' ) or ( user_input=='2' and comp_input=='3' ) or ( user_input=='3' and comp_input=='1' ):
		comp_count=comp_count+1
	elif ( user_input=='1' and comp_input=='1' ) or ( user_input=='3' and comp_input=='2' ) or ( user_input=='1' and comp_input=='3' ):
		user_count=user_count+1
	else:
		print("Empate")

	print("\nPONTUACAO:")
	print("Pontuação do usuario:",user_count,"\tPontuação do computador:",comp_count,"\n")


print("\n\t\tPontuação FINAL:")
print("Pontuação do usuario:",user_count,"\t\t\tPontuação do computador:",comp_count,"\n")
if user_count>comp_count:
	print("\n\tPARABENS! VOCE VENCEU!")
elif user_count<comp_count:
	print("\n\t\tDESCULPE! VOCE PERDEU!")
else:
	print("\n\t\tOOPS! É UM EMPATE!")
